from telethon.sync import TelegramClient
from dotenv import load_dotenv
import argostranslate.package, argostranslate.translate
from time import sleep
import datetime
import os
load_dotenv()

api_id=os.environ.get("API_ID")
api_hash=os.environ.get("API_HASH")
channels=[]
installed_languages = argostranslate.translate.get_installed_languages()
print(installed_languages)
#Add you Telegram channels here.....
channelChats=[]
def getText(channel):
    for chat in channel:
        with TelegramClient("researchu",api_id,api_hash) as client:
            for message in client.iter_messages(chat,offset_date=datetime.date.today(),reverse=True):
                channelChats.append(message.text)

def translateText(orig_lang,chats):
    installed_languages = argostranslate.translate.get_installed_languages()
    to_code="en"
    from_lang= list(filter(lambda x:x.code == orig_lang,installed_languages))[0]
    to_lang = list(filter(lambda x:x.code==to_code,installed_languages))[0]
    for message in chats:
        translation = from_lang.get_translation(to_lang)
        translatedText = translation.translate(message)
        print(translatedText)
        sleep(1)

   

getText(channels)
translateText("ru",channelChats)