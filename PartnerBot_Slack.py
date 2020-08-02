from prayersheet import *

import asyncio
import os
import slack

read_file = 'files/names.txt'
write_file = 'files/partners.csv'

commands = [
    'ping',
    'load',
    'add',
    'remove',
    'list',
    'pair',
    'pairings',
    'clear',
    'swap',
    'exit'
]

class PartnerBot:

    def __init__(self, token, rf, wf):

        # Create slack client
        self.client = slack.RTMClient(token=os.environ[token])

        # Create prayersheet object
        self.ps = PrayerSheet(rf,wf)

        # Clear any old data
        self.ps.clear()

        # Read in the list names from the file
        self.ps.read_names()

        # Setup slack connection
        if slack_client.rtm_connect(with_team_state=False):
            print('PartnerBot successfully started up.')
        else:
            print('Error starting up PartnerBot.')

        self.id = slack_client.api_call("auth.test")["user_id"]

        # Run the bot
        self.client.start()

    @slack.RTMClient.run_on(event='message')
    def ping(self, **payload):
        data = payload['data']
        text = data['text']
        
        print(text)

# Main function
if __name__ == '__main__':
    PartnerBot('Insert Token Here', read_file, write_file