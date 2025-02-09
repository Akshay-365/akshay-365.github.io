---
layout: post
title: "Remote SSH."
date: 2025-01-20 14:00:00
description: Remote SSH. # Add post description (optional)
img: remote_ssh.jpg # Add image post (optional)
categories: remote ssh
tags: [ssh, tunnel, socket]
---

# 🚀 Remote SSH Guide

## 🛠️ Install OpenSSH

```bash
sudo apt-get update && sudo apt-get install -y openssh-server
sudo nano /etc/ssh/sshd_config
```

*Edit the port according to you. Let's say `8081`.*

## 🔗 Install Gsocket

```bash
curl -sSL https://gsocket.io/install.sh | bash
```

*If needed, now go to the gsocket folder, then `./gsocket` and then `make install` as guided.*

📌 **For Gsocket:**
```bash
curl -sSL https://gsocket.io/install.sh | bash
cd gsocket
./install.sh
cd gsocket
make install
```

### 🖥️ On Server:

```bash
gsocket /usr/sbin/sshd -d
```

Then enter any `{PASS_KEY}`.

### 💻 On Client:

```bash
gsocket -s PASS_KEY ssh root@gsocket -p 8081
```

*(You can use `root` or any available user on the server.)*

---

## 🌍 Ngrok Installation

```bash
# Remove the old version of ngrok if available
rm -f ngrok

# Download the latest ngrok version (Linux)
curl -o ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

# Unzip it
unzip ngrok.zip

# Give execute permissions to ngrok
chmod +x ngrok
```

## 🖥️ Install Code-Server

```bash
curl -fsSL https://code-server.dev/install.sh | sh

code-server --bind-addr 0.0.0.0:7860 --auth none

ngrok http 7860
```

🎯 **One single command:**
```bash
code-server --bind-addr 0.0.0.0:7860 --auth none & ngrok http 7860
```

---

## 🎁 BONUS: Using Socat

Install `socat`:
```bash
apt install socat -y
```

Transfer port within localhost:
```bash
socat TCP-LISTEN:2222,fork TCP:localhost:8081
```
*(port transferred from 8081 to 2222.)*

---

## 🌐 Using Localtunnel

```bash
npm install -g localtunnel
lt --port 8081
```
*(or any port 8082..etc)*

It will give a URL like:
```bash
https://your-subdomain.loca.lt
```

To SSH using the URL (I think the url can be used for ssh to turn local ip [hostname -I] into public like.):
```bash
ssh username@your-subdomain.loca.lt -p 8081
```

*(Not working in my test for now, but very useful for future use.)*

---

### 🔄 SSH Tunneling:
-  For me, first run localtunnel 'It --port 8081', then u will get a link, then u can replace it with local ip.

**Set up a reverse SSH tunnel on SERVER**:
First, run Localtunnel:
```bash
lt --port 8081
```

Then use the generated link:
```bash
ssh -R 8081:localhost:8081 username@remote-server-ip
```
*or*
```
ssh -R 8081:localhost:8081 root@your-subdomain.loca.lt
```

**Access from Client:**
```bash
ssh -p 8081 username@remote-server-ip
```

*(Change accordingly. Play around with it.. but do not waste time ❌.)*

---

## 🛜 Ngrok TCP Forwarding

```bash
ngrok tcp 8081
```

*(May allow only one task at a time in Ngrok, or may require a paid plan for TCP forwarding.)*

---

## 🌩️ Cloudflared (Argo Tunnel)
**Very simple, go as you click:**

```bash
apt-get install wget
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
dpkg -i cloudflared-linux-amd64.deb
```

Check version:
```bash
cloudflared --version
```

Run tunnel:
```bash
cloudflared tunnel --url http://localhost:8081
```

📌 **Full command to run Code-Server with Cloudflared:**
```bash
code-server --bind-addr 0.0.0.0:7860 --auth none & cloudflared tunnel --url http://localhost:7860
```

🔹 **Optional: Run in the Background**
- If you want to keep cloudflared running in the background, use nohup:

```bash
nohup cloudflared tunnel --url http://localhost:8081 > cloudflared.log 2>&1 &
```

---

## 🔎 MORE TO EXPLORE:

### 🛠️ BORE ([GitHub](https://github.com/ekzhang/bore))

Exposes local ports to a remote server, bypassing standard NAT connection firewalls.

```bash
cargo install bore-cli
bore local 8000 --to bore.pub
```

Or:

```bash
# On the server
bore server --secret my_secret_string

# On the client
bore local <LOCAL_PORT> --to <TO> --secret my_secret_string
```

🔗 **Other tools:**
- [Expose.sh](https://github.com/exposesh)
- [Telebit](https://telebit.cloud/)
- [Awesome Tunneling](https://github.com/anderspitman/awesome-tunneling?tab=readme-ov-file)

---

## 🔄 Frequently Used Commands

```bash
apt-get update && apt-get install -y openssh-server
apt install curl -y
apt-get install build-essential -y
apt install libssl-dev -y
apt-get install git -y
apt install automake -y
apt install autoconf -y
apt install nano -y
apt install npm -y
apt install systemctl -y
apt install net-tools -y
curl -fsSL https://code-server.dev/install.sh | sh
apt install wget -y
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb 
dpkg -i cloudflared-linux-amd64.deb
```

💡 **Run after installation:**
```bash
code-server --bind-addr 0.0.0.0:7860 --auth none & cloudflared tunnel --url http://localhost:7860
```

🚀 **Enjoy Secure Remote Access!**
