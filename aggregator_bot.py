#########################################################################################
# Importing required modules
from telethon import TelegramClient, events, sync
import telegram_send


#########################################################################################
# Defining required functions

# This function returns true if any of the key terms along with the joiner are found in the message
def keyFound(keys, message, joiner=""):        
    for i in keys:
        # The condition below ensures that the joiner MUST be present along with a key term
        if i.upper() in message.upper() and joiner.upper() in message.upper():
            return True
    return False

# This function returns true if not a single ban term was found in the message
def noBannedTerms(bannedTerms, message):
    for i in bannedTerms:
        if i.upper() in message.upper():
            return False
    return True


#########################################################################################
# Creating the client
# Enter your own id and hash
api_id = 9999999
api_hash = "6random35f1random1random80random"
client = TelegramClient('anon', api_id, api_hash)


#########################################################################################
# Defining the keys, joiner and ban terms
keys=["insert", "your", "keys"]
joiner="this term MUST be present"
bannedTerms=["~", "*", "spam", "terms"]


#########################################################################################
# Continously checks for new message
@client.on(events.NewMessage(incoming=True))
async def my_event_handler(event):
    message=event.raw_text

    # If any key is found and if no ban terms are present, then the message is added to the God Feed
    if keyFound(keys, message, joiner):
        if noBannedTerms(bannedTerms, message):
            try:
                chat_from = event.chat if event.chat else (await event.get_chat())
                chat_title = chat_from.title
            except:
               chat_title="private user" 
            telegram_send.send(messages=[message + " ~ " + chat_title])


#########################################################################################
# Starting the client
print("Script is starting!")
client.start()
client.run_until_disconnected()


#########################################################################################

