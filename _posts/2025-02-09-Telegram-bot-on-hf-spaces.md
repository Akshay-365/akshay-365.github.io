---
layout: post
title: "Bot via Webhook"
date: 2025-02-09 00:00:00 +0000
tags: [bot,webhook,fastapi,endpoint]
---

To set up a **Webhook URL** for your Telegram bot running on **Hugging Face Spaces**, follow these steps:

### **1. Get Your Telegram Bot Token**
- Create a bot using [BotFather](https://t.me/BotFather) on Telegram.
- Copy the bot token (it looks like `123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ`).

### **2. Deploy Your Bot on Hugging Face Spaces**
- Use a framework like **Flask** or **FastAPI** to handle webhook requests [I used FAstAPI].
- Make sure your Hugging Face Space provides a **public HTTPS URL**. (Make the space public for convenience.)

### **3. Set the Webhook for Your Bot**
- Use this API request to set the webhook (you can run this anywhere, it just need to run once.):
  ```bash
  curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
       -H "Content-Type: application/json" \
       -d '{"url": "https://your-huggingface-space-url.com/webhook"}'
  ```
- Replace `<YOUR_BOT_TOKEN>` and `your-huggingface-space-url.com` accordingly.

- Now in the setting of HuggingFace and click on te `webhook` option and then create a new webhook by selecting your specific space and then input Webhook url in there.
- Format your webhook URL as:
  ```
  https://your-huggingface-space-url.com/webhook
  ```

### **4. Verify the Webhook**
Check if the webhook is set correctly by visiting:
```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo
```

<hr />
<hr />

## Below is a complete guide on how to containerize your Telegram webhook bot (using FastAPI) with Docker. This setup lets you develop and deploy your bot entirely within a Docker container, which you can then deploy to Hugging Face Spaces (or run locally).

---

## **1. Project Structure**

Organize your project files like so:

```
telegram-bot-docker/
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## **2. Create Your FastAPI Application (`app.py`)**

Below is a sample FastAPI application that listens for Telegram webhook updates and sends a reply:

```python
# app.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]

        # Respond via Telegram's webhook mechanism
        return {
            "method": "sendMessage",
            "chat_id": chat_id,
            "text": "Hello! This message is sent via webhook."
        }

    return {"status": "ok"}

```

*Notes:*
- The webhook endpoint is defined at `/webhook`.
- You can modify the handler logic as needed.

---

## **3. Define Dependencies (`requirements.txt`)**

List the required packages:

```
fastapi
uvicorn[standard]
requests
```

---

## **4. Create a Dockerfile**

Below is a sample Dockerfile that builds your FastAPI app using the official Python image:

```dockerfile
# Dockerfile
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy dependency definitions and install them
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that uvicorn will listen on (Hugging Face Spaces uses port 7860)
EXPOSE 7860

# Start the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
```

*Explanation:*
- We use a slim Python image to keep the container lightweight.
- Dependencies are installed, and the application code is copied.
- The app listens on port **7860**, which is the standard port for Hugging Face Spaces.

---

## **5. Building and Running Your Docker Container Locally**

### **Build the Docker Image**

Open your terminal in the project directory and run:

```bash
docker build -t telegram-bot .
```

### **Run the Docker Container**

Make sure to pass your Telegram bot token as an environment variable:

```bash
docker run -d -p 7860:7860 telegram-bot
```

---

## **6. Deploying to Hugging Face Spaces**

Hugging Face Spaces supports Docker-based deployments. To deploy:

1. **Create a new Space** on Hugging Face.
2. **Select the "Docker" option** when setting up the Space.
3. **Push your repository** (with your Dockerfile, app.py, and requirements.txt) to the Space.

<hr />

### NOTEs:
- We don't need to use the bot Token in the code because it's already confingured with the webhook.
- The code is not based on any wrapper/library of telegram it just made of of pure original telegram, uses mostly json based communication.
- The reason why this can't use any other library like (telebot etc.) because in those libraries thier is the ability to receive the messages from webhook but there's no fuction to send the message via webhook (FastAPI endpoint). At Least It haven't come across yet to me. More to explore!
- app = FastAPI() --> This must be there in the code for FastAPI endpoint and webhook connection.
- ENJOY THE BOT!