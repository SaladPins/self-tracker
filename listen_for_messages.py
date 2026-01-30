import asyncio
import csv
from datetime import datetime
from pathlib import Path
from telegram import Bot

BOT_TOKEN = '8273792941:AAEkYSxkpazej9UCBSbNCCVVO-WDyUEMP50'
CHAT_ID = 8109589127

bot = Bot(BOT_TOKEN)

MORNING_CSV = 'morning_logs.csv'
FOCUS_CSV = 'focus_log.csv'

def load_last_update_id():
    try:
        with open('last_update_id.txt', 'r') as f:
            content = int(f.read().strip())
            if content == '':
                return None
            return int(content)

    except (FileNotFoundError, ValueError):
        return None

def save_last_update_id(update_id):
    with open('last_update_id.txt', 'w') as f:
        f.write(str(update_id))

def save_to_csv(filename, row, headers=None):
    try:
        with open(filename, 'r') as f:
            pass
    except FileNotFoundError:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            if headers:
                writer.writerow(headers)

    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def parse_morning_message(text):
    sleep_hours, tiredness, medication = text.split(',')
    now = datetime.now()
    return [now.date(), now.strftime("$H:$M"), sleep_hours, tiredness, medication]

def parse_focus_message(text):
    now = datetime.now()
    return [now.date(), now.strftime("%H:%M"), text]

async def process_new_messages():
    last_update_id = load_last_update_id()

    updates = await bot.get_updates(offset=(last_update_id +1) if last_update_id else None)

    for update in updates:
        if not update.message or not update.message.text:
            continue

        last_update_id = update.update_id
        save_last_update_id(last_update_id)
        message = update.message
        if not message or not message.text:
            continue
            
        text = message.text.strip()

        if ',' in text:
            row = parse_morning_message(text)
            headers = ['date', 'time', 'sleep_hours', 'tiredness', 'medication']
            save_to_csv(MORNING_CSV, row, headers=headers)
            await bot.send_message(CHAT_ID, "Morning tracker saved!")
        else:

            row = parse_focus_message(text)
            headers = ['date', 'time', 'activity_summary']
            save_to_csv(FOCUS_CSV, row, headers=headers)
            await bot.send_message(CHAT_ID, "Focus tracker saved!")

if __name__ == "__main__":
    asyncio.run(process_new_messages())

        



