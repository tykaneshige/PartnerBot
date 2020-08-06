from prayersheet import *

import asyncio
import os
import slack

token = 'Insert Token Here'

read_file = 'files/names.txt'
write_file = 'files/partners.csv'

ps = PrayerSheet(read_file, write_file)

article = 'https://medium.com/@ritikjain1272/how-to-make-a-slack-bot-in-python-using-slacks-rtm-api-335b393563cd'
classic = 'https://api.slack.com/apps?new_classic_app=1'

# Basic Connection Test
def ping(web_client, channel_id):
    web_client.chat_postMessage(channel=channel_id, text='pong!')

# Load all names available on the text file
def load(web_client, channel_id):

    try:
        # Check if file is empty
        if ps.read_names() == 1:
            response = 'Name file is empty!'
            web_client.chat_postMessage(channel=channel_id, text=response)
            return
        
        response = 'Names successfully loaded.'
    except:
        response = 'Error loading names.'
       
    web_client.chat_postMessage(channel=channel_id, text=response)

# Adds name to prayersheet object (but not to the txt file)
def add(web_client, channel_id, args):

    # Check for an empty arg list
    if len(args) == 0:
        response = 'Please pass 1 or more names.'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return
    
    # Add names to prayersheet object
    try:
        ps.add_names(args)
        response = 'Names successfully added.'
    except:
        response = 'Error adding names.'
    
    web_client.chat_postMessage(channel=channel_id, text=response)

# Remove names from prayersheet object (but not from the txt file)
def remove(web_client, channel_id, args):

    # Check for an empty arg list
    if len(args) == 0:
        response = 'Please pass 1 or more names.'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return

    # Check for an empty name list
    if len(ps.members) == 0:
        response = 'There are no members to remove.'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return

    # Remove names from prayersheet object
    try:
        ps.remove_names(args)
        response = 'Names successfully removed.'
    except:
        response = 'Error removing names.'
        
    web_client.chat_postMessage(channel=channel_id, text=response)

# List all members to be paired
def list_names(web_client, channel_id):

    # Check if the list is empty
    if len(ps.members) == 0:
        response = 'No members exist yet!'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return
    
    for name in ps.members:
        response = str(name) + '\n'
        web_client.chat_postMessage(channel=channel_id, text=response)

# Pair names
def pair(web_client, channel_id):

    # Verify that the number of members is greater than 0
    if len(ps.members) == 0:
        response = 'There are no members to pair!'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return

    try:
        ps.randomize()
        response = 'Names successfully paired.'
    except:
        response = 'Error pairing names.'
    
    web_client.chat_postMessage(channel=channel_id, text=response)

# List the pairings
def pairings(web_client, channel_id, send_file=''):

    # Verify that there are pairings
    if len(ps.partners) == 0:
        response = 'There are no pairings yet!'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return

    # Check if the user wants the pairings in file format
    if send_file == 'file':
        try:
            response = client.files_upload(channels=channel_id,file='partners.csv')
        except:
            response = 'Error sending file.'
        
        web_client.chat_postMessage(channel=channel_id, text=response)
        return

    try:
        for key in ps.members:
            response = '{}: {}'.format(key,ps.partners[key])
            web_client.chat_postMessage(channel=channel_id, text=response)
    except:
        response = 'Error listing pairings.'
        web_client.chat_postMessage(channel=channel_id, text=response)

# Clears all pairings (from both the object and file)
def clear(web_client, channel_id):

    try:
        ps.clear()
        response = 'Successfully cleared pairings.'
    except:
        response = 'Error clearing pairings.'

    web_client.chat_postMessage(channel=channel_id, text=response)

# Swaps two partners
def swap(web_client, channel_id, args):

    # Check if two names were passed
    if len(args) != 2:
        response = 'Please pass *two* names.'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return

    if len(ps.partners) == 0:
        response = 'There are no pairs yet.'
        web_client.chat_postMessage(channel=channel_id, text=response)
        return
    
    n1 = args[0]
    n2 = args[1]

    # Swap the names
    try:
        result = ps.swap(n1,n2)

        if result == 1:
            response = 'Name 1 is invalid.'
        elif result == 2:
            response = 'Name 2 is invalid.'
        else:
            response = 'Successfully swapped \'{}\' and \'{}\'.'.format(n1,n2)
    except:
        response = 'Error swapping names.'
    
    web_client.chat_postMessage(channel=channel_id, text=response)

# RTM Response System
@slack.RTMClient.run_on(event="message")
def parse_commands(**payload):

    # Gather relevant data on the message
    data = payload['data']
    web_client = payload['web_client']
    bot_id = data.get('bot_id', '')

    # Check if the message was sent by the bot
    if bot_id == '':
        channel_id = data['channel']

        # Extracting text
        text = data.get('text')

        # Parse the text
        parse = text.split()

        # Check for a valid command
        if parse[0] == '?ping' and len(parse) == 1:
            ping(web_client,channel_id)
        elif parse[0] == '?load' and len(parse) == 1:
            load(web_client,channel_id)
        elif parse[0] == '?add':

            # Parse and add any extra arguments
            if len(parse) == 1:
                args = []
            else:
                args = parse[1:]

            add(web_client,channel_id,args)
        elif parse[0] == '?remove':

            # Parse and add any extra arguments
            if len(parse) == 1:
                args = []
            else:
                args = parse[1:]

            remove(web_client,channel_id,args)
        elif parse[0] == '?list' and len(parse) == 1:
            list_names(web_client,channel_id)
        elif parse[0] == '?pair' and len(parse) == 1:
            pair(web_client,channel_id)
        elif parse[0] == '?pairings' and len(parse) <= 2:
            
            # Check for file option
            if len(parse) == 2:
                if parse[1] == 'file':
                    pairings(web_client,channel_id,send_file='file')
                else:
                    response = 'Unrecognized pairing option.'
                    web_client.chat_postMessage(channel=channel_id, text=response)
            else:
                pairings(web_client,channel_id)
        elif parse[0] == '?clear' and len(parse) == 1:
            clear(web_client,channel_id)
        elif parse[0] == '?swap':

            # Parse and add any extra arguments
            if len(parse) == 1:
                args = []
            else:
                args = parse[1:]

            swap(web_client,channel_id,args)
        elif parse[0] == '?exit' and len(parse) == 1:
            response = 'Shutting down.'
            web_client.chat_postMessage(channel=channel_id, text=response)
            exit(0)
        else:   
            response = 'Unrecognized command.'
            web_client.chat_postMessage(channel=channel_id, text=response)

# Main Function
if __name__ == '__main__':

    # Clear any old data
    ps.clear()

    # Read in the list names from the file
    ps.read_names()

    # Set up slack client
    try:
        client = slack.RTMClient(token=token)
        print('PartnerBot successfully started up.')
    except:
        print('Error starting up PartnerBot.')
        exit()

    # Run the bot
    client.start()