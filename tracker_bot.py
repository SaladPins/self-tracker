from telegram import Bot

TOKEN = "8273792941:AAEkYSxkpazej9UCBSbNCCVVO-WDyUEMP50"

CHAT_ID = 8109589127

bot = Bot(token=TOKEN)

def send_message():
    bot.send_message(chat_id=CHAT_ID, text="Hello! this is a test")

send_message()







