---
layout: post
title: My Telegram Bot That Keeps Lightning AI Awake 🤖
date: 2025-08-05 09:00:00 +0300
description: A step-by-step tutorial on how I built a "ping-pong" bot using Python, Gradio, and Telegram to prevent my Lightning AI studio from auto-shutting down during long-running tasks.
img: keep_alive/keep_alive_banner.png # Optional: A banner image for your post
tags: [Python, Automation, Telegram, Gradio, DevOps, CloudIDE]
---

# My Journey: Building a Bot to Keep My Lightning AI Studio Alive 🚀

This story begins with a familiar frustration for anyone who runs long tasks in cloud development environments. I was deep into a project scraping the Classplus API, a job that needed to run for hours in the background. My platform of choice was **[Lightning AI Studio](https://lightning.ai/)**, which is fantastic, but has one major feature designed to save resources: it automatically shuts down inactive instances.

### The Frustration 😟

I'd leave my scraper running, only to return later to find the studio had shut down, killing my progress. I needed a way to signal to the platform, "Hey, I'm still here! Don't turn off the lights!"

### The 'Aha!' Moment 💡

The shutdown is triggered by inactivity—no key presses, no mouse movements, and critically, no network traffic. I realized that if I could generate consistent, small-scale network activity from within the studio, I could trick the system into thinking it was still in use.

My solution? A fully automated "ping-pong" (핑퐁) bot system operated via Telegram.

### The Game Plan 🛠️

I decided to build a system with three core components, all running inside my Lightning AI instance:

1.  **The Ping Bot:** A script that sends a "ping" message to a public Telegram channel every few minutes. This generates outgoing network traffic.
2.  **The Pong Bot:** A second script that listens to the same channel. When it sees a "ping," it immediately replies with "pong," generating incoming network traffic.
3.  **The Control Panel:** A simple web UI built with [Gradio](https://www.gradio.app/) to monitor the bots, check their status, and manually trigger a ping if needed.

This constant, tiny chatter between the bots would be enough to keep the studio from falling asleep. And it worked perfectly.

---

### Peek Under the Hood: Explore the Code 🔍

I've packaged the entire project for you. You can download the files below to see exactly how it works and set it up yourself.

*   **🤖 Main Application (`main.py`):** Launches the bots and the Gradio web interface.
    *   [**⬇️ Download `main.py`**][main-py]
*   **📤 Ping Scheduler (`ping_scheduler.py`):** Sends "ping" messages and includes the watchdog.
    *   [**⬇️ Download `ping_scheduler.py`**][ping-scheduler-py]
*   **📥 Pong Responder (`pong_bot.py`):** Listens for pings and replies with "pong."
    *   [**⬇️ Download `pong_bot.py`**][pong-bot-py]
*   **✅ Project Dependencies (`requirements.txt`):** All the necessary packages.
    *   [**⬇️ Download `requirements.txt`**][requirements-txt]

[main-py]: /assets/code/keep_alive/main.py
[ping-scheduler-py]: /assets/code/keep_alive/ping_scheduler.py
[pong-bot-py]: /assets/code/keep_alive/pong_bot.py
[requirements-txt]: /assets/code/keep_alive/requirements.txt

---

### Technical Deep Dive: How the Code Works 🔬

Here’s a breakdown of the key logic in each file.

#### 1. `pong_bot.py` (The Listener)
This is the simplest component. Its only job is to listen and respond.
*   **Technology:** It uses the `py-telegram-bot-api` library to connect to Telegram's API.
*   **Core Logic:** The `@bot.channel_post_handler` is a decorator that tells the bot to execute a function only when a new message appears in the channel. The `func` filter ensures it only triggers if the message text is exactly "ping".
*   **Action:** When triggered, it sends "pong" back to the same channel and logs the timestamp.

#### 2. `ping_scheduler.py` (The Initiator & Watchdog)
This is the heart of the keep-alive mechanism.
*   **Scheduling:** The `start_ping_loop` function runs an infinite `while` loop. Inside, it calls `send_ping()` and then `time.sleep(300)` to pause for 5 minutes before repeating.
*   **Sending Pings:** The `send_ping()` function makes a direct HTTP GET request to the Telegram Bot API endpoint (`/sendMessage`) to post "ping" in the channel.
*   **The Watchdog:** After a ping is sent, a `threading.Timer` starts a 12-second countdown. The `check_pong_watchdog` function then compares the timestamp of the last ping with the last pong. If the last pong is older than the last ping, it means a pong was missed, and it's logged.

#### 3. `main.py` (The Conductor & UI)
This script brings everything together and provides a user interface.
*   **Multithreading:** To run the ping loop, the pong bot, and the web UI simultaneously, we use Python's `threading` module. Each major component is started in its own `daemon` thread.
*   **Gradio UI:** It uses `gradio` to create a simple web dashboard with buttons to refresh logs or send a ping.
*   **External Keep-Alive Hooks:** The Gradio app provides two powerful ways to be triggered externally:
    1.  **GET Request:** By visiting `YOUR_GRADIO_URL/?ping=true`.
    2.  **POST Request (API):** By calling the function's direct API endpoint. We'll explore this in the next section.

### Deployment Guide 🚀

1.  **Get Telegram Bots:** Talk to the [BotFather](https://t.me/botfather) on Telegram to create two bots and get their API tokens.
2.  **Create a Public Channel:** Create a new public Telegram channel. Give it a username (e.g., `@my_keepalive_pings`). Add both of your bots to the channel as administrators.
3.  **Configure the Code:**
    *   In `ping_scheduler.py`, add your **Ping Bot Token** and **Channel Username**.
    *   In `pong_bot.py`, add your **Pong Bot Token**.
4.  **Set up in Lightning AI:**
    *   Upload the four project files to your studio instance.
    *   Open a terminal and install the dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Run the main application:
        ```bash
        python main.py
        ```
5.  **Monitor:** The terminal will output a public Gradio URL. Open it in your browser to see your control panel in action!

---

### Bonus: Setting Up an External Cron Job with `cron-job.org`

While a simple uptime monitor is good, a more robust method is to call our Gradio function's API endpoint directly. This is exactly what I did using **`cron-job.org`**. This method uses a POST request, giving us more control.

Here's how to set it up:



1.  **Get Your API URL:** First, you need the direct API endpoint for your Gradio function. It usually follows this pattern: `YOUR_GRADIO_URL/gradio_api/call/YOUR_FUNCTION_NAME`. For our project, the function is `manual_ping`.
2.  **Configure the Cron Job:** In `cron-job.org`, create a new cron job with the following settings, as shown in the screenshot:
    *   **URL:** Your Gradio API URL (e.g., `https://....litng.ai/gradio_api/call/manual_ping`).
    *   **Request Method:** Set this to `POST`.
    *   **Headers:** Add a header with `Key: Content-Type` and `Value: application/json`.
    *   **Request Body:** Add the following JSON to the body. This is required by the Gradio API to call a function that takes no arguments.
        ```json
        {
          "data": []
        }
        ```
3.  **Set the Schedule:** Choose how often you want the job to run (e.g., every 5 or 10 minutes).
4.  **Save and Activate:** Save your cron job. Now, `cron-job.org` will send a POST request to your application on schedule, generating the network traffic needed to keep it active!

### Conclusion 🎉

This project was a fantastic exercise in solving a practical problem with a bit of creative automation. It demonstrates how simple scripts and freely available services like Telegram and Gradio can be combined to create a robust and useful tool. What started as a small annoyance became a fun project that has saved me countless hours of lost work.

May your long-running tasks always complete without interruption!

---

### References

*   **Cloud IDE:** [**Lightning AI**](https://lightning.ai/)
*   **UI Framework:** [**Gradio**](https://www.gradio.app/)
*   **Bot Creation:** [**Telegram's BotFather**](https://t.me/botfather)
*   **External Cron Service:** [**cron-job.org**](https://cron-job.org/)
