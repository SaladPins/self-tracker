import asyncio
import telegram

text = 'What have you done the past 2 hours?\nPlease respond with one word only.'

BOT_TOKEN = '8273792941:AAEkYSxkpazej9UCBSbNCCVVO-WDyUEMP50'
CHAT_ID = 8109589127

async def main():
    bot = telegram.Bot(BOT_TOKEN)

    await bot.send_message(chat_id=CHAT_ID, text=text)

if __name__ == "__main__":
    asyncio.run(main())