# Partner Bot

Created By: 
*Thomas Kaneshige (tykaneshige.work@gmail.com)*

A simple program used to create pairs from a list of names. 
The original purpose of this program was to make prayer partners from a list of names.

---

## Description

* PartnerBot is a simple bot that takes in a list of names and pairs them up.
  * Upon startup, the bot will upload a set of names from a txt file.
  * The bot will randomly pair names until finished, even if there are an odd number of names.

* This bot comes with two files by default.
  * 'names.txt': This file contains a list of names. 
    * These names will be read in initially when starting up the bot.
  * 'partners.csv': This file will contain the pairs after '?pair' is called.
    * This file will be sent when using the command '?pairings file'.

* Requirements
  * You must be using Python 3.5 or later.
  * (For Discord) You must have discord 1.3.4 installed on your system.
  * (For Slack) You must have slackclient 2.7.3 installed on your system.

---

## Instructions

### FOR DISCORD

1. Start by cloning the the repository using 'git clone'.
2. After cloning the repository, go to the Discord Developer site.
   1. This can be accessed by searching up 'Discord SDK' on Google.
3. After logging in, click on 'Applications' > 'New Application'.
   1. You may need to authrorize 2-Factor Authentication.
4. Give the bot a name, picture, and description (last two are optional).
5. After finishing the initial setup, create a new bot by going to 'Bot' > 'Add Bot'.
6. After creating a new bot, go to 'OAuth2' and fill out the following fields.
   1. In 'Scopes', identify this bot as a 'Bot'.
   2. In 'Bot Permissions', authorize (at least) 'Send Messages', 'Attach Files', and 'Read Message History'. This can be changed later.
7. A link should be generated in the center of the page. Follow the link to an authorization page.
8. Add the bot to your server of choice. You must have admin-level permissions to do this.
9. After adding the bot to your server, go back to the Discord Developer site.
10. Go back to the bot you created, and click on 'Bot'.
11. Scroll down to find the bot's token (which should be hidden).
12. Copy the token and insert it in PartnerBot_Discord.py where it says, "Insert Token Here".
13. Start the bot by running the command 'python3 PartnerBot_Discord.py' (python3 is necessary).
14. The command line should state that the bot is logged in. Verify by texting '?ping' in your server.
15. If the bot responds with 'pong!', then it is ready to be used!

### FOR SLACK

More detailed instructions can be found [here](https://medium.com/@ritikjain1272/how-to-make-a-slack-bot-in-python-using-slacks-rtm-api-335b393563cd).

1. Start by cloning the the repository using 'git clone'.
2. Go the Slack Developer site. Use [this link](https://api.slack.com/apps?new_classic_app=1).
   1. Note: The slack app we are creating is a 'classic app', which is different from the current slack apps. Using the link above is imperative.
3. Sign into your Slack account if neccessary and click on 'Create New App'.
4. Give the bot a name and add it to your desired workspace.
5. On the 'Basic Information' page, click on 'Bots', since we are creating a bot.
6. On 'App Home', click on 'Add Legacy Bot User'.
   1. If there is no option to do this, you are on the wrong site.
   2. Consult step 2 above if this happens.
7. Enter a 'Display Name' and a 'Default Username' for the bot.
8. After clicking 'Add', go to the 'OAuth & Permissions' tab.
9.  Copy the 'Bot User OAuth Access Token' (should be the second one down).
10. Paste the token PartnerBot_Slack.py where it says "Insert Token Here".
11. Start the bot by running the command 'python3 PartnerBot_Slack.py' (python3 is necessary).
12. The command line should state that the bot is logged in. Verify by texting '?ping' in your server.
13. If the bot responds with 'pong!', then it is ready to be used!

---

## Documentation

* Commands
  * All commands with begin with the prefix '?'.

```
-?ping: Simple command to test that for a working connection with the bot. 
        The bot should respond with "pong!".

-?load: This command reloads all the names from files/names.txt.

-?add <name1> <name2> ... : Adds a name to the member list.

-?remove <name1> <name2> ... : Removes a name from the member list.

-?list: Prints the member list.

-?pair: Randomly pairs the names.

-?pairings <file=optional>: Prints the list of pairs.
  -If passed with the argument 'file', PartnerBot will send the pairings as a csv file instead.

-?clear: Clears the pairings file.

-?swap <name1> <name2>: Swaps two members and their partners.

-?exit: Disconnects the bot.
```

---

## Open Issues

* (Major): Slack bot cannot send the pairings file.
* (minor): No specific disconnect API call in the slack bot.