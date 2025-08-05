import requests
import threading
import time  # ✅ FIX: Missing import
from datetime import datetime
from pong_bot import last_pong_timestamp

PING_BOT_TOKEN = "8129330649:AAFmSV4goGwE3Jhey5U9Zuq_bk6i09V1D3g"
CHAT_ID = "@keep_alive_ping"  # ✅ Replace with your actual public channel username

last_ping = None
ping_log = []
missed_pongs = []

def send_ping():
    global last_ping
    url = f"https://api.telegram.org/bot{PING_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": "ping"
    }
    res = requests.get(url, params=params)
    if res.ok:
        last_ping = datetime.now()
        ping_log.append(("ping", last_ping.strftime("%H:%M:%S")))
        if len(ping_log) > 10:
            ping_log.pop(0)
        print(f"[Ping Sent] {last_ping.strftime('%H:%M:%S')}")
        # ✅ Delay watchdog to wait for pong response
        threading.Timer(12, check_pong_watchdog).start()
    else:
        print("❌ Failed to send ping:", res.text)

def check_pong_watchdog():
    if last_ping is None or last_pong_timestamp is None:
        missed_pongs.append(last_ping.strftime("%H:%M:%S") if last_ping else "Unknown")
        if len(missed_pongs) > 5:
            missed_pongs.pop(0)
        print(f"⚠️ Missed Pong at {last_ping.strftime('%H:%M:%S') if last_ping else 'Unknown'}")
        return
    if last_pong_timestamp < last_ping:
        missed_pongs.append(last_ping.strftime("%H:%M:%S"))
        if len(missed_pongs) > 5:
            missed_pongs.pop(0)
        print(f"⚠️ Missed Pong (late) at {last_ping.strftime('%H:%M:%S')}")

def start_ping_loop(interval_sec=300):  # ⏱ Default: 5 minutes
    while True:
        send_ping()
        time.sleep(interval_sec)

def get_ping_log():
    return ping_log

def get_missed_pongs():
    return missed_pongs

def manual_ping():
    send_ping()
    return "📤 Manual ping sent!"
