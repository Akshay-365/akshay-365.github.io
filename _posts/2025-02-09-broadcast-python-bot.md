---
layout: post
title: "Broadcast bot"
date: 2025-02-09 00:00:00 +0000
img: broadcast.jpg
tags: [broadcast, bot, python]
---

# The code to which can detect the users connected to bot and can send alerts to the users.

```python
import telebot
import threading
import time
import logging

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------

logging.basicConfig(
    level=logging.DEBUG,  # Capture all levels: DEBUG, INFO, WARNING, ERROR.
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ------------------------------------------------------------------------------
# Bot Initialization
# ------------------------------------------------------------------------------

TOKEN = "BOT_TOKEN"  # Replace with your actual token.
bot = telebot.TeleBot(TOKEN)

# ------------------------------------------------------------------------------
# Update Listener (Raw Update Logging)
# ------------------------------------------------------------------------------

def update_listener(updates):
    """
    Logs raw update data received by the bot. This logs the full JSON-like
    structure of the update, including callback queries, messages, etc.
    """
    for update in updates:
        try:
            # If the update object has a to_dict() method, use it.
            update_data = update.to_dict()
        except Exception:
            update_data = update.__dict__
        logging.debug(f"Received update: {update_data}")

# Register the update listener. This callback is called with every new update.
bot.set_update_listener(update_listener)

# ------------------------------------------------------------------------------
# Retrieve Bot Information
# ------------------------------------------------------------------------------

try:
    bot_info = bot.get_me()
    bot_id = bot_info.id
    logging.info(f"Bot info retrieved: id={bot_info.id}, username={bot_info.username}")
except Exception as e:
    logging.error(f"Error retrieving bot info: {e}")
    raise

# ------------------------------------------------------------------------------
# In-Memory State: Tracking the Last Sender in Each Chat
# ------------------------------------------------------------------------------
# Key: chat_id, Value: sender's id (user's id or the bot's id)
last_sender = {}

# ------------------------------------------------------------------------------
# Message Handler: Logs Detailed Message Data and Responds
# ------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    sender = message.from_user

    # Log detailed message data.
    logging.debug(
        f"Received message in chat {chat_id}: "
        f"message_id={message.message_id}, text='{message.text}', "
        f"from_user: id={sender.id}, username='{sender.username}', "
        f"first_name='{sender.first_name}', last_name='{sender.last_name}', "
        f"date={message.date}"
    )

    # Mark that the user was the last sender.
    last_sender[chat_id] = sender.id
    logging.info(f"Set last_sender for chat {chat_id} to user (id: {sender.id})")

    # Reply to the user.
    try:
        reply = bot.send_message(chat_id, "You are now subscribed to alerts!")
        logging.info(f"Sent subscription reply to chat {chat_id} (reply message_id={reply.message_id})")
    except Exception as e:
        logging.error(f"Error sending subscription reply to chat {chat_id}: {e}")

    # After replying, update the last sender to the bot.
    last_sender[chat_id] = bot_id
    logging.info(f"Updated last_sender for chat {chat_id} to bot (id: {bot_id})")

# ------------------------------------------------------------------------------
# Callback Query Handler: Logs Detailed Callback Data and Answers
# ------------------------------------------------------------------------------

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Some callback queries might not have an associated message.
    chat_id = call.message.chat.id if call.message else None
    sender = call.from_user

    # Log detailed callback query data.
    logging.debug(
        f"Received callback query: id={call.id}, data='{call.data}', "
        f"from_user: id={sender.id}, username='{sender.username}', "
        f"first_name='{sender.first_name}', last_name='{sender.last_name}', "
        f"chat_id={chat_id}"
    )

    # Optionally answer the callback query.
    try:
        bot.answer_callback_query(call.id, text="Callback received")
        logging.info(f"Answered callback query: id={call.id}")
    except Exception as e:
        logging.error(f"Error answering callback query: {e}")

# ------------------------------------------------------------------------------
# Alert Sender Thread: Periodically Sends Alerts to Chats
# ------------------------------------------------------------------------------

def alert_sender():
    """
    Background thread that sends an alert (here, a simple "test" message) to every chat
    where the last message was sent by the bot. The interval is adjustable.
    """
    alert_interval = 5  # Adjust the alert interval (in seconds) as needed.
    while True:
        logging.debug("Alert thread: Checking chats for alert dispatch...")
        for chat_id in list(last_sender.keys()):
            if last_sender.get(chat_id) == bot_id:
                try:
                    alert_msg = "test"
                    alert_response = bot.send_message(chat_id, alert_msg)
                    logging.info(f"Sent alert to chat {chat_id} (alert message_id={alert_response.message_id})")
                    # The alert message is sent by the bot, so last_sender remains unchanged.
                    last_sender[chat_id] = bot_id
                except Exception as e:
                    logging.error(f"Error sending alert to chat {chat_id}: {e}")
        logging.debug(f"Alert thread sleeping for {alert_interval} seconds...")
        time.sleep(alert_interval)

# Start the background alert thread.
alert_thread = threading.Thread(target=alert_sender, daemon=True)
alert_thread.start()
logging.info("Started alert_sender thread.")

# ------------------------------------------------------------------------------
# Start Polling for Updates
# ------------------------------------------------------------------------------

try:
    logging.info("Starting bot polling...")
    bot.polling(none_stop=True)
except Exception as e:
    logging.error(f"Bot polling error: {e}")
```

## The above code can detect the very last message, if the last message was sent by the user then the bot auto sends the alert.
- The bot only works for auto send if the last message in the conversation was from the user.
- It cannot send the message auto if the last reply/message was from the bot. (maybe because it cannot detect the user's chat ID from the last message to send the message). [More to explore!]


# This is the another robust code for broadcasting system.

```python
import os
import json
import time
import threading
import logging
import telebot

# ------------------------------------------------------------------------------
# Directories and File Paths
# ------------------------------------------------------------------------------

BOT_INFO_DIR = "bot_info"
CHAT_LOGS_DIR = os.path.join(BOT_INFO_DIR, "chat_logs")
SUBSCRIBERS_FILE = os.path.join(BOT_INFO_DIR, "subscribers.json")
UNSUBSCRIBE_REQUESTS_FILE = os.path.join(BOT_INFO_DIR, "request_unsubscribe.json")
LOG_FILE = os.path.join(BOT_INFO_DIR, "bot.log")

# Create required directories if not present.
for directory in [BOT_INFO_DIR, CHAT_LOGS_DIR]:
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")

# ------------------------------------------------------------------------------
# Logging Configuration: Console and File Logging
# ------------------------------------------------------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
try:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
except Exception as e:
    logging.error(f"Error setting up file logging: {e}")

# ------------------------------------------------------------------------------
# Bot Initialization and Owner Configuration
# ------------------------------------------------------------------------------

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your actual token.
bot = telebot.TeleBot(TOKEN)
OWNER_ID = 123456789  # Replace with your Telegram user ID (owner-only commands).

# ------------------------------------------------------------------------------
# Utility Functions: Subscribers, Unsubscribe Requests, and Chat Logging
# ------------------------------------------------------------------------------

def load_subscribers():
    """Load subscribers from file; create if missing."""
    if not os.path.exists(SUBSCRIBERS_FILE):
        logging.info(f"{SUBSCRIBERS_FILE} not found. Creating a new one.")
        save_subscribers([])
        return []
    try:
        with open(SUBSCRIBERS_FILE, "r") as f:
            subscribers = json.load(f)
        logging.debug(f"Loaded subscribers: {subscribers}")
        return subscribers
    except Exception as e:
        logging.error(f"Error loading subscribers: {e}")
        return []

def save_subscribers(subscribers):
    """Save the subscribers list to file."""
    try:
        with open(SUBSCRIBERS_FILE, "w") as f:
            json.dump(subscribers, f, indent=4)
        logging.debug("Saved subscribers.")
    except Exception as e:
        logging.error(f"Error saving subscribers: {e}")

def load_unsubscribe_requests():
    """Load unsubscribe requests from file; create if missing."""
    if not os.path.exists(UNSUBSCRIBE_REQUESTS_FILE):
        save_unsubscribe_requests([])
        return []
    try:
        with open(UNSUBSCRIBE_REQUESTS_FILE, "r") as f:
            reqs = json.load(f)
        return reqs
    except Exception as e:
        logging.error(f"Error loading unsubscribe requests: {e}")
        return []

def save_unsubscribe_requests(reqs):
    """Save unsubscribe requests to file."""
    try:
        with open(UNSUBSCRIBE_REQUESTS_FILE, "w") as f:
            json.dump(reqs, f, indent=4)
        logging.debug("Saved unsubscribe requests.")
    except Exception as e:
        logging.error(f"Error saving unsubscribe requests: {e}")

def log_chat_message(message):
    """Append each incoming message (in JSON Lines format) to its chat log file."""
    chat_id = message.chat.id
    log_file_path = os.path.join(CHAT_LOGS_DIR, f"{chat_id}.log")
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "message_id": message.message_id,
        "user_id": message.from_user.id if message.from_user else None,
        "username": message.from_user.username if message.from_user else None,
        "first_name": message.from_user.first_name if message.from_user else None,
        "last_name": message.from_user.last_name if message.from_user else None,
        "text": message.text,
        "chat_id": chat_id,
        "chat_type": message.chat.type
    }
    try:
        with open(log_file_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        logging.debug(f"Logged message for chat {chat_id}.")
    except Exception as e:
        logging.error(f"Error logging message for chat {chat_id}: {e}")

def ensure_subscriber(message):
    """
    Automatically add the user to subscribers if not already present.
    Each record contains basic info plus an 'unsubscribe_requested' flag.
    """
    chat_id = message.chat.id
    subscribers = load_subscribers()
    if not any(sub.get("chat_id") == chat_id for sub in subscribers):
        new_sub = {
            "chat_id": chat_id,
            "user_id": message.from_user.id if message.from_user else None,
            "username": message.from_user.username if message.from_user else "",
            "first_name": message.from_user.first_name if message.from_user else "",
            "last_name": message.from_user.last_name if message.from_user else "",
            "subscription_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "unsubscribe_requested": False
        }
        subscribers.append(new_sub)
        save_subscribers(subscribers)
        logging.info(f"Auto-added subscriber: {new_sub}")

# ------------------------------------------------------------------------------
# Update Listener: Log Raw Updates and Auto-Subscribe
# ------------------------------------------------------------------------------

def update_listener(updates):
    """Log raw update data and auto-subscribe users from incoming messages."""
    for update in updates:
        try:
            update_data = update.to_dict()
        except Exception:
            update_data = update.__dict__
        logging.debug(f"Received update: {update_data}")
        # Auto-subscribe if update contains a message.
        if hasattr(update, "message") and update.message is not None:
            ensure_subscriber(update.message)

bot.set_update_listener(update_listener)

# ------------------------------------------------------------------------------
# Retrieve Bot Information
# ------------------------------------------------------------------------------

try:
    bot_info = bot.get_me()
    logging.info(f"Bot info: id={bot_info.id}, username={bot_info.username}")
except Exception as e:
    logging.error(f"Error retrieving bot info: {e}")
    raise

# ------------------------------------------------------------------------------
# Command Handlers (All call ensure_subscriber explicitly)
# ------------------------------------------------------------------------------

@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    """Send a help message with detailed usage instructions for every command."""
    ensure_subscriber(message)
    if message.from_user.id == OWNER_ID:
        help_text = (
            "<b>Welcome to the Alert Bot! 😃</b>\n\n"
            "<b>User Commands:</b>\n"
            "• <b>/subscribe</b> - Confirm your subscription or re‑subscribe (cancels any pending unsubscribe request).\n"
            "• <b>/unsubscribe</b> - Request to unsubscribe (your request will be pending approval).\n"
            "• <b>/status</b> - Check your current subscription status.\n"
            "• <b>/myinfo</b> - View your subscription details.\n\n"
            "<b>Owner‑Only Commands:</b>\n"
            "• <b>/broadcast &lt;message&gt;</b> - <i>Send an alert</i> to all subscribers.\n"
            "    <i>Example:</i> <code>/broadcast Attention: Server maintenance at 10PM.</code>\n"
            "• <b>/stats</b> - View subscription statistics.\n"
            "• <b>/list_subscribers</b> - List all subscribers with detailed info (shows only User ID).\n"
            "• <b>/list_unsubscribes</b> - List all pending unsubscribe requests (shows only User ID).\n"
            "• <b>/process_unsubscribes &lt;approve|deny&gt; &lt;all|numbers&gt;</b> - Process unsubscribe requests.\n"
            "    <i>Examples:</i>\n"
            "       • <code>/process_unsubscribes approve all</code>\n"
            "       • <code>/process_unsubscribes deny 2 4</code>\n"
            "• <b>/clear_chat_logs &lt;chat_id|all&gt;</b> - Clear chat log(s).\n"
            "    <i>Examples:</i>\n"
            "       • <code>/clear_chat_logs all</code>\n"
            "       • <code>/clear_chat_logs 123456789</code>\n"
            "• <b>/ping</b> - Check if the bot is responsive.\n"
        )
    else:
        help_text = (
            "<b>Welcome to the Alert Bot! 😃</b>\n\n"
            "<b>User Commands:</b>\n"
            "• <b>/subscribe</b> - Confirm your subscription or re‑subscribe.\n"
            "• <b>/unsubscribe</b> - Request to unsubscribe (your request is pending approval).\n"
            "• <b>/status</b> - Check your current subscription status.\n"
            "• <b>/myinfo</b> - View your subscription details.\n"
            "• <b>/ping</b> - Check if the bot is responsive.\n"
        )
    try:
        bot.send_message(message.chat.id, help_text, parse_mode="HTML")
        logging.info(f"Sent help message to chat {message.chat.id}.")
    except Exception as e:
        logging.error(f"Error sending help message: {e}")

@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    """(Re)confirm a user's subscription and auto-subscribe if needed."""
    ensure_subscriber(message)
    chat_id = message.chat.id
    subscribers = load_subscribers()
    found = False
    for sub in subscribers:
        if sub.get("chat_id") == chat_id:
            found = True
            if sub.get("unsubscribe_requested"):
                sub["unsubscribe_requested"] = False
                save_subscribers(subscribers)
                reqs = load_unsubscribe_requests()
                new_reqs = [req for req in reqs if req.get("chat_id") != chat_id]
                if len(new_reqs) < len(reqs):
                    save_unsubscribe_requests(new_reqs)
                try:
                    bot.send_message(chat_id, "✅ <b>Your subscription has been re‑confirmed! 🎉</b>", parse_mode="HTML")
                    logging.info(f"Subscription re‑confirmed for chat {chat_id}.")
                except Exception as e:
                    logging.error(f"Error sending re‑confirmation: {e}")
            else:
                try:
                    bot.send_message(chat_id, "😃 <b>You are already subscribed!</b>", parse_mode="HTML")
                    logging.info(f"Chat {chat_id} is already subscribed.")
                except Exception as e:
                    logging.error(f"Error sending subscription message: {e}")
            break
    if not found:
        new_sub = {
            "chat_id": chat_id,
            "user_id": message.from_user.id if message.from_user else None,
            "username": message.from_user.username if message.from_user else "",
            "first_name": message.from_user.first_name if message.from_user else "",
            "last_name": message.from_user.last_name if message.from_user else "",
            "subscription_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "unsubscribe_requested": False
        }
        subscribers.append(new_sub)
        save_subscribers(subscribers)
        try:
            bot.send_message(chat_id, "✅ <b>You have been subscribed to alerts! 🎉</b>", parse_mode="HTML")
            logging.info(f"New subscriber added: {new_sub}")
        except Exception as e:
            logging.error(f"Error sending subscription confirmation: {e}")

@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    """Mark the user as having requested unsubscription and record the request."""
    ensure_subscriber(message)
    chat_id = message.chat.id
    subscribers = load_subscribers()
    found = False
    for sub in subscribers:
        if sub.get("chat_id") == chat_id:
            if sub.get("unsubscribe_requested"):
                try:
                    bot.send_message(chat_id, "⚠️ <b>You have already requested to unsubscribe.</b>", parse_mode="HTML")
                except Exception as e:
                    logging.error(f"Error sending message: {e}")
                return
            else:
                sub["unsubscribe_requested"] = True
                found = True
                break
    if found:
        save_subscribers(subscribers)
        reqs = load_unsubscribe_requests()
        if not any(req.get("chat_id") == chat_id for req in reqs):
            new_req = {
                "chat_id": chat_id,
                "user_id": message.from_user.id if message.from_user else None,
                "username": message.from_user.username if message.from_user else "",
                "first_name": message.from_user.first_name if message.from_user else "",
                "last_name": message.from_user.last_name if message.from_user else "",
                "request_date": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            reqs.append(new_req)
            save_unsubscribe_requests(reqs)
        try:
            bot.send_message(chat_id,
                             "⚠️ <b>Your unsubscribe request has been noted.</b>\nYou will continue to receive alerts until approved.",
                             parse_mode="HTML")
            logging.info(f"Unsubscribe request noted for chat {chat_id}.")
        except Exception as e:
            logging.error(f"Error sending unsubscribe confirmation: {e}")
    else:
        try:
            bot.send_message(chat_id, "ℹ️ <b>You are not in our subscriber list yet!</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending not-subscribed message: {e}")

@bot.message_handler(commands=['status'])
def status(message):
    """Provide the subscription status of the user."""
    ensure_subscriber(message)
    chat_id = message.chat.id
    subscribers = load_subscribers()
    status_msg = "ℹ️ <b>You are not subscribed. Use /subscribe to subscribe.</b>"
    for sub in subscribers:
        if sub.get("chat_id") == chat_id:
            if sub.get("unsubscribe_requested"):
                status_msg = "⚠️ <b>You have requested to unsubscribe. Your request is pending approval.</b>"
            else:
                status_msg = "✅ <b>You are subscribed to alerts.</b>"
            break
    try:
        bot.send_message(chat_id, status_msg, parse_mode="HTML")
        logging.info(f"Sent subscription status to chat {chat_id}.")
    except Exception as e:
        logging.error(f"Error sending status: {e}")

@bot.message_handler(commands=['myinfo'])
def myinfo(message):
    """Send the stored subscriber info for the current user (showing only User ID)."""
    ensure_subscriber(message)
    chat_id = message.chat.id
    subscribers = load_subscribers()
    user_info = next((sub for sub in subscribers if sub.get("chat_id") == chat_id), None)
    if user_info:
        info_text = (
            f"<b>Your Subscription Info:</b>\n"
            f"• <b>User ID:</b> {user_info.get('user_id')}\n"
            f"• <b>Username:</b> @{user_info.get('username')}\n"
            f"• <b>Name:</b> {user_info.get('first_name')} {user_info.get('last_name')}\n"
            f"• <b>Subscribed On:</b> {user_info.get('subscription_date')}\n"
            f"• <b>Unsubscribe Requested:</b> {user_info.get('unsubscribe_requested')}"
        )
    else:
        info_text = "ℹ️ <b>You are not subscribed. Use /subscribe to subscribe.</b>"
    try:
        bot.send_message(chat_id, info_text, parse_mode="HTML")
        logging.info(f"Sent subscription info to chat {chat_id}.")
    except Exception as e:
        logging.error(f"Error sending myinfo: {e}")

@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    """
    Owner‑only command to broadcast an alert message.
    <b>Usage:</b> <code>/broadcast &lt;message&gt;</code>
    <i>Example:</i> <code>/broadcast Attention: Server maintenance at 10PM.</code>
    """
    ensure_subscriber(message)
    if message.from_user.id != OWNER_ID:
        try:
            bot.send_message(message.chat.id, "🚫 <b>You are not authorized to broadcast alerts.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending unauthorized message: {e}")
        return

    broadcast_text = message.text[len('/broadcast'):].strip()
    if not broadcast_text:
        usage = (
            "<b>Usage of /broadcast:</b>\n"
            "• <code>/broadcast &lt;message&gt;</code>\n\n"
            "Example:\n"
            "• <code>/broadcast Attention: Server maintenance at 10PM.</code>"
        )
        try:
            bot.send_message(message.chat.id, usage, parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending broadcast usage guide: {e}")
        return

    subscribers = load_subscribers()
    if not subscribers:
        try:
            bot.send_message(message.chat.id, "ℹ️ <b>No subscribers to send alert.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending no-subscriber message: {e}")
        return

    for sub in subscribers:
        chat_id = sub.get("chat_id")
        try:
            response = bot.send_message(chat_id, broadcast_text, parse_mode="HTML")
            logging.info(f"Broadcast sent to chat {chat_id} (message_id={response.message_id}).")
        except Exception as e:
            logging.error(f"Error sending broadcast to chat {chat_id}: {e}")
    try:
        bot.send_message(message.chat.id, "✅ <b>Broadcast message sent to all subscribers.</b>", parse_mode="HTML")
    except Exception as e:
        logging.error(f"Error sending broadcast confirmation: {e}")

@bot.message_handler(commands=['stats'])
def stats(message):
    """
    Owner‑only command to display subscription statistics.
    """
    ensure_subscriber(message)
    if message.from_user.id != OWNER_ID:
        try:
            bot.send_message(message.chat.id, "🚫 <b>You are not authorized to view stats.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending unauthorized stats message: {e}")
        return
    subscribers = load_subscribers()
    total = len(subscribers)
    active = len(subscribers)
    stats_text = f"<b>Total Subscribers:</b> {total}\n<b>Active Subscribers:</b> {active}"
    try:
        bot.send_message(message.chat.id, stats_text, parse_mode="HTML")
        logging.info(f"Sent stats to owner: {stats_text}")
    except Exception as e:
        logging.error(f"Error sending stats: {e}")

@bot.message_handler(commands=['list_subscribers'])
def list_subscribers(message):
    """
    Owner‑only command to list detailed subscriber info.
    (Only <b>User ID</b> is shown.)
    """
    ensure_subscriber(message)
    if message.from_user.id != OWNER_ID:
        try:
            bot.send_message(message.chat.id, "🚫 <b>You are not authorized to view subscribers.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending unauthorized list_subscribers message: {e}")
        return
    subscribers = load_subscribers()
    if not subscribers:
        reply = "ℹ️ <b>No subscribers found.</b>"
    else:
        reply = "<b>Subscribers:</b>\n"
        for idx, sub in enumerate(subscribers, start=1):
            reply += (
                f"{idx}. <b>User ID:</b> {sub.get('user_id')}, "
                f"<b>Name:</b> {sub.get('first_name')} {sub.get('last_name')}, "
                f"<b>Username:</b> @{sub.get('username')}, "
                f"<b>Subscribed On:</b> {sub.get('subscription_date')}, "
                f"<b>Unsubscribe Requested:</b> {sub.get('unsubscribe_requested')}\n"
            )
    try:
        bot.send_message(message.chat.id, reply, parse_mode="HTML")
        logging.info("Sent detailed subscriber list to owner.")
    except Exception as e:
        logging.error(f"Error sending subscribers list: {e}")

@bot.message_handler(commands=['list_unsubscribes'])
def list_unsubscribes(message):
    """
    Owner‑only command to list all pending unsubscribe requests.
    (Only <b>User ID</b> is shown.)
    """
    ensure_subscriber(message)
    if message.from_user.id != OWNER_ID:
        try:
            bot.send_message(message.chat.id, "🚫 <b>You are not authorized to view unsubscribe requests.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending unauthorized list_unsubscribes message: {e}")
        return
    reqs = load_unsubscribe_requests()
    if not reqs:
        reply = "ℹ️ <b>No unsubscribe requests found.</b>"
    else:
        reply = "<b>Unsubscribe Requests:</b>\n"
        for idx, req in enumerate(reqs, start=1):
            reply += (
                f"{idx}. <b>User ID:</b> {req.get('user_id')}, "
                f"<b>Name:</b> {req.get('first_name')} {req.get('last_name')}, "
                f"<b>Username:</b> @{req.get('username')}, "
                f"<b>Requested On:</b> {req.get('request_date')}\n"
            )
    try:
        bot.send_message(message.chat.id, reply, parse_mode="HTML")
        logging.info("Sent unsubscribe requests list to owner.")
    except Exception as e:
        logging.error(f"Error sending unsubscribe requests list: {e}")

@bot.message_handler(commands=['process_unsubscribes'])
def process_unsubscribes(message):
    """
    Owner‑only command to process unsubscribe requests.
    
    <b>Usage Examples:</b>
      • <code>/process_unsubscribes approve all</code>
      • <code>/process_unsubscribes deny all</code>
      • <code>/process_unsubscribes approve 1 3 5</code>
      • <code>/process_unsubscribes deny 2 4</code>
      
    • If <b>approve</b> is used, the subscriber record is removed (they will no longer receive alerts).
    • If <b>deny</b> is used, the unsubscribe request is canceled (the subscription remains active).
    
    If insufficient parameters are provided, a detailed guide with current pending requests is shown.
    """
    ensure_subscriber(message)
    if message.from_user.id != OWNER_ID:
        try:
            bot.send_message(message.chat.id, "🚫 <b>You are not authorized to process unsubscribe requests.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending unauthorized process_unsubscribes message: {e}")
        return

    args = message.text.split()
    reqs = load_unsubscribe_requests()
    if len(args) < 3:
        guide_text = (
            "<b>Usage of /process_unsubscribes:</b>\n\n"
            "<b>To <u>approve</u> unsubscribe requests (remove subscribers):</b>\n"
            "   • <code>/process_unsubscribes approve all</code> - Approve all requests\n"
            "   • <code>/process_unsubscribes approve 1 3 5</code> - Approve specific requests by their serial numbers\n\n"
            "<b>To <u>deny</u> unsubscribe requests (cancel requests, keep subscription active):</b>\n"
            "   • <code>/process_unsubscribes deny all</code> - Deny all requests\n"
            "   • <code>/process_unsubscribes deny 2 4</code> - Deny specific requests by their serial numbers\n\n"
            "<b>Current Unsubscribe Requests:</b>\n"
        )
        if reqs:
            for idx, req in enumerate(reqs, start=1):
                guide_text += (f"{idx}. <b>User ID:</b> {req.get('user_id')}, "
                               f"<b>Name:</b> {req.get('first_name')} {req.get('last_name')}, "
                               f"<b>Username:</b> @{req.get('username')}, "
                               f"<b>Requested On:</b> {req.get('request_date')}\n")
        else:
            guide_text += "ℹ️ No unsubscribe requests pending."
        try:
            bot.send_message(message.chat.id, guide_text, parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending process_unsubscribes guide: {e}")
        return

    action = args[1].lower()
    if action not in ("approve", "deny"):
        try:
            bot.send_message(message.chat.id, "ℹ️ <b>Action must be either 'approve' or 'deny'.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending action message: {e}")
        return

    targets = args[2:]
    if len(targets) == 1 and targets[0].lower() == "all":
        indices = list(range(len(reqs)))
    else:
        try:
            indices = [int(x) - 1 for x in targets if x.isdigit()]
        except Exception as e:
            try:
                bot.send_message(message.chat.id, "ℹ️ <b>Invalid input. Provide serial numbers or 'all'.</b>", parse_mode="HTML")
            except Exception as ex:
                logging.error(f"Error sending invalid input message: {ex}")
            return

    indices = sorted(set(indices))
    subscribers = load_subscribers()
    processed_details = []
    if action == "approve":
        for i in indices:
            if i < 0 or i >= len(reqs):
                continue
            req = reqs[i]
            chat_id = req.get("chat_id")
            sub_removed = None
            for sub in subscribers:
                if sub.get("chat_id") == chat_id:
                    sub_removed = sub
                    break
            if sub_removed:
                subscribers.remove(sub_removed)
                processed_details.append(f"✅ Approved unsubscribe for <b>{sub_removed.get('first_name')} {sub_removed.get('last_name')}</b> (@{sub_removed.get('username')}) (User ID: {sub_removed.get('user_id')})")
        new_reqs = [req for j, req in enumerate(reqs) if j not in indices]
    elif action == "deny":
        for i in indices:
            if i < 0 or i >= len(reqs):
                continue
            req = reqs[i]
            chat_id = req.get("chat_id")
            for sub in subscribers:
                if sub.get("chat_id") == chat_id:
                    sub["unsubscribe_requested"] = False
                    processed_details.append(f"❌ Denied unsubscribe for <b>{sub.get('first_name')} {sub.get('last_name')}</b> (@{sub.get('username')}) (User ID: {sub.get('user_id')})")
                    break
        new_reqs = [req for j, req in enumerate(reqs) if j not in indices]
    else:
        new_reqs = reqs

    save_subscribers(subscribers)
    save_unsubscribe_requests(new_reqs)
    if processed_details:
        reply = "<b>Processed Unsubscribe Requests:</b>\n" + "\n".join(processed_details)
    else:
        reply = "ℹ️ <b>No valid unsubscribe requests processed.</b>"
    try:
        bot.send_message(message.chat.id, reply, parse_mode="HTML")
        logging.info(f"Processed unsubscribe requests: {reply}")
    except Exception as e:
        logging.error(f"Error sending process_unsubscribes confirmation: {e}")

@bot.message_handler(commands=['clear_chat_logs'])
def clear_chat_logs(message):
    """
    Owner‑only command to clear chat logs.
    
    <b>Usage:</b>
      • <code>/clear_chat_logs all</code> - Clear all chat logs.
      • <code>/clear_chat_logs &lt;chat_id&gt;</code> - Clear the chat log for a specific chat.
      
    If the required parameter is missing, a detailed usage guide is shown.
    """
    ensure_subscriber(message)
    if message.from_user.id != OWNER_ID:
        try:
            bot.send_message(message.chat.id, "🚫 <b>You are not authorized to clear chat logs.</b>", parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending unauthorized clear_chat_logs message: {e}")
        return

    args = message.text.split()
    if len(args) < 2:
        usage = (
            "<b>Usage of /clear_chat_logs:</b>\n\n"
            "• <code>/clear_chat_logs all</code> - Clear all chat logs.\n"
            "• <code>/clear_chat_logs &lt;chat_id&gt;</code> - Clear the chat log for a specific chat.\n\n"
            "Example:\n"
            "• <code>/clear_chat_logs all</code>\n"
            "• <code>/clear_chat_logs 123456789</code>"
        )
        try:
            bot.send_message(message.chat.id, usage, parse_mode="HTML")
        except Exception as e:
            logging.error(f"Error sending clear_chat_logs usage guide: {e}")
        return

    target = args[1].lower()
    if target == "all":
        cleared = 0
        for file in os.listdir(CHAT_LOGS_DIR):
            file_path = os.path.join(CHAT_LOGS_DIR, file)
            try:
                os.remove(file_path)
                cleared += 1
            except Exception as e:
                logging.error(f"Error removing file {file_path}: {e}")
        reply = f"✅ Cleared <b>{cleared}</b> chat log file(s)."
    else:
        file_path = os.path.join(CHAT_LOGS_DIR, f"{target}.log")
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                reply = f"✅ Cleared chat log for chat <b>{target}</b>."
            except Exception as e:
                reply = f"⚠️ Error clearing log for chat <b>{target}</b>: {e}"
                logging.error(reply)
        else:
            reply = f"ℹ️ No log file found for chat <b>{target}</b>."
    try:
        bot.send_message(message.chat.id, reply, parse_mode="HTML")
        logging.info(f"clear_chat_logs: {reply}")
    except Exception as e:
        logging.error(f"Error sending clear_chat_logs confirmation: {e}")

@bot.message_handler(commands=['ping'])
def ping(message):
    """Simple command to check if the bot is responsive."""
    ensure_subscriber(message)
    try:
        bot.send_message(message.chat.id, "🏓 <b>pong</b>", parse_mode="HTML")
        logging.info(f"Ping response sent to chat {message.chat.id}.")
    except Exception as e:
        logging.error(f"Error sending ping response: {e}")

# ------------------------------------------------------------------------------
# Default Handler: Log Incoming Messages and Ensure Subscriber Record
# ------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: True)
def default_message_handler(message):
    """
    For every incoming message:
      1. Auto-subscribe the user (if not already in the list).
      2. Log the message in a per‑chat log file.
    """
    try:
        ensure_subscriber(message)
    except Exception as e:
        logging.error(f"Error ensuring subscriber for chat {message.chat.id}: {e}")
    try:
        log_chat_message(message)
    except Exception as e:
        logging.error(f"Error logging message from chat {message.chat.id}: {e}")
    logging.debug(f"Received message in chat {message.chat.id}: from: {message.from_user.username if message.from_user else 'N/A'} | text: {message.text}")

# ------------------------------------------------------------------------------
# Asynchronous Owner Alert Input (Console)
# ------------------------------------------------------------------------------

def alert_input_listener():
    """
    Continuously prompt the owner (via the console) for an alert message.
    Upon input (unless 'exit' is typed), broadcast the alert to all subscribers.
    """
    while True:
        try:
            alert_message = input("Enter alert message to broadcast (or type 'exit' to stop): ").strip()
            if alert_message.lower() == 'exit':
                logging.info("Exiting console alert input listener.")
                break
            if not alert_message:
                continue  # Skip empty input.
            subscribers = load_subscribers()
            if not subscribers:
                logging.warning("No subscribers found. Alert not sent.")
                continue
            for sub in subscribers:
                chat_id = sub.get("chat_id")
                try:
                    response = bot.send_message(chat_id, alert_message, parse_mode="HTML")
                    logging.info(f"Console alert sent to chat {chat_id} (message_id={response.message_id}).")
                except Exception as e:
                    logging.error(f"Error sending console alert to chat {chat_id}: {e}")
        except Exception as e:
            logging.error(f"Error in alert input listener: {e}")

# Start the asynchronous alert input listener in a daemon thread.
alert_input_thread = threading.Thread(target=alert_input_listener, daemon=True)
alert_input_thread.start()
logging.info("Started asynchronous alert input listener thread.")

# ------------------------------------------------------------------------------
# Start Bot Polling
# ------------------------------------------------------------------------------

try:
    logging.info("Starting bot polling...")
    bot.polling(none_stop=True)
except Exception as e:
    logging.error(f"Bot polling error: {e}")
```

### This code is complete full-fledge robust code for broadcasting system.
- But this lacks the feature to auto detect the last message as above code.
- Need to incorporate the auto detect the last message (if sent by user) to save the user in the list in real-time beforehand.