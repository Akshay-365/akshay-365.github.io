---
layout: post
title: GUI Remote Desktop
date: 2025-01-23 00:00:00 +0300
img: remote_desktop2.webp # Add image post (optional)
tags: [GUI, ssh, remote, xfce] # add tag
---

# 🖥️ HOW CAN YOU HAVE A DESKTOP REMOTE ENVIRONMENT
*(focuses on xfce4 / xfce4-session for some xstartup commands.)*

## 🚀 Step 1: Update and Install Required Packages
```bash
apt update && apt upgrade -y
apt install -y xfce4 xfce4-goodies tigervnc-standalone-server wget curl git dbus-x11
```

## 🔑 Step 2: Create a VNC password for the server:
```bash
vncpasswd
```

## 📥 Step 3: Clone the noVNC repository:
```bash
git clone https://github.com/novnc/NoVNC.git /opt/novnc
```

## 📂 Step 4: Navigate to the noVNC directory:
```bash
cd /opt/novnc/utils
ln -s ../novnc_proxy .    # This symbolic link creation may give errors ignore them or you can also skip this command.
```

## ▶️ Step 5: Run noVNC:
```bash
/opt/novnc/utils/novnc_proxy --vnc localhost:5901
```

---

## ⚡ NOW FROM HERE,
there are several ways to run vncserver:
### ✅ What I prefer (xstartup):
1️⃣ First, confirm you have desktop enabled on `:1` or any..
   ```bash
   export DISPLAY=:1
   echo $DISPLAY  # To check
   ```
2️⃣ Navigate to `.vnc` folder:
   ```bash
   ls -la  # To check hidden files
   cd .vnc
   ```
3️⃣ Create a new file:
   ```bash
   nano xstartup  # or nano /root/.vnc/xstartup
   ```
4️⃣ Write in file:
   ```bash
   #!/bin/sh
   # Start up the standard system desktop
   unset SESSION_MANAGER
   unset DBUS_SESSION_BUS_ADDRESS
   /usr/bin/startxfce4
   [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
   #[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
   x-window-manager &
   ```
   *if u want u can also create .Xresources (not necessary.)*

5️⃣ Make it executable:
   ```bash
   chmod +x /root/.vnc/xstartup
   ```
   *for making it as executable (every time you have to run above command.)*
   🔹 Optional:
   ```bash
   chown root:root /root/.vnc/xstartup
   chmod 755 /root/.vnc/xstartup
   ```
6️⃣ Ensure noVNC is running first:
   ```bash
   /opt/novnc/utils/novnc_proxy --vnc localhost:5901
   ```
7️⃣ Then run:
   ```bash
   vncserver :1
   ```
8️⃣ You can kill VNC server if needed:
   ```bash
   vncserver -kill :1
   ```

🚀 Open port 6080 (maybe) in your URL and enjoy! 🎉

---

### 🔄 Another Way (Might Be Useful):
If `vncserver :1` is giving errors, try:
```bash
tigervncserver -xstartup /usr/bin/xterm
```

Then, in the noVNC virtual terminal in browser (website), enter:
```bash
xfce4-session
```
*or*
```bash
xfce4-session --display=:1
```

🔹 You can also run apps without a full desktop environment:
Like x11-apps:
```bash
apt install -y x11-apps
xclock  # Example GUI app
```
or any other app, just search for it(x11-apps).

---

### 🎯 Another Way:
Skip 'xstartup' and just launch `vncserver` normally:
```bash
vncserver :1
```
Then manually launch the XFCE session from your terminal:
```bash
xfce4-session --display=:1
```
And start in the noVNC site.

To stop XFCE:
```bash
xfce4-session-logout --logout
```

---

### 🔥 HOT: Use SSH with X11 Forwarding (For GUI Apps):
Run GUI apps from the container and display them locally!
Once logged in, you can run GUI applications (like xclock, xterm, etc.), and they will be displayed on your local machine.

1️⃣ Install OpenSSH:
   ```bash
   apt install -y openssh-server
   ```
2️⃣ SSH into your server with X11 forwarding:
   ```bash
   ssh -X user@localhost -p 2222  # Modify accordingly (u know it..😎)
   ```

---

### 🛠️ TIPS: Use `-geometry` in VNC server for full resolution:
```bash
vncserver :1 -geometry 1535x824  # Example for my laptop
```

---

## 🌐 Inside GUI Desktop

### 🔍 Install a browser (e.g., Falkon or Firefox via Git):
Let's continue with Falkon.
```bash
apt install falkon
```
⚠️ It might not open directly! Try this:

1️⃣ Navigate to `/usr/bin/`, open terminal, then run:
   ```bash
   sudo env QTWEBENGINE_DISABLE_SANDBOX=1 ./MyApp  # Replace MyApp with falkon or any app having same problem.
   ```
   *(Btw, I like Firefox much, you can install that via binaries.)*

2️⃣ Alternative (not tested yet):
   - Create a new Linux user for a non-root environment:
   ```bash
   sudo adduser newuser_name
   ```
   - and you can also test this command:
   ```bash
   ./MyApp --no-sandbox
   ```

---

🚀 **Enjoy your remote desktop!** 😎
