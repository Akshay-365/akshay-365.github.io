import telebot
from datetime import datetime

PONG_BOT_TOKEN = "7863283721:AAFMIztRiQidfn5sVX-hWX-4kv9yK-tsKyQ"
bot = telebot.TeleBot(PONG_BOT_TOKEN)

pong_log = []
last_pong = None
last_pong_timestamp = None

@bot.channel_post_handler(func=lambda msg: msg.text and msg.text.lower() == "ping")
def respond_pong(message):
    global last_pong, last_pong_timestamp
    bot.send_message(message.chat.id, "pong")
    last_pong_timestamp = datetime.now()
    last_pong = last_pong_timestamp.strftime("%H:%M:%S")
    pong_log.append(("pong", last_pong))
    if len(pong_log) > 10:
        pong_log.pop(0)
    print(f"[Pong Sent] {last_pong}")

def run_pong_bot():
    bot.infinity_polling()

def get_pong_log():
    return pong_log

def get_last_pong():
    return last_pong if isinstance(last_pong, str) else "No pong yet"
