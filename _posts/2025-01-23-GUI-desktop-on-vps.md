---
layout: post
title: GUI remote desktop
date: 5025-01-23 00:00:00 +0300
img: hello-world.jpg # Add image post (optional)
tags: [GUI, ssh, remote, xfce] # add tag
---

# HOW CAN U HAVE A DESKTOP REMOTE ENVIROMENT.

Step 1: Update and Install Required Packages
apt update && apt upgrade -y
apt install -y xfce4 xfce4-goodies tigervnc-standalone-server wget curl git dbus-x11


Step 2: Create a VNC password for the server:
vncpasswd

Step 3: Clone the noVNC repository:
git clone https://github.com/novnc/noVNC.git /opt/novnc

Step 4: Navigate to the noVNC directory:
cd /opt/novnc/utils
ln -s ../novnc_proxy .

Step 5: Run noVNC:
/opt/novnc/utils/novnc_proxy --vnc localhost:5901

NOW FROM HERE, there are several ways to run vncserver:
# assuming novnc command is running.
@ What i prefer (xstartup):
* first of all confirm you have desktop enable on :1 or any..
`export DISPLAY=:1` u can check it by `echo $DISPLAY`
* go to `.vnc` folder u can see it by `ls -la`. `cd .vnc`
* now create a new file `nano xstartup`
* write in file:
```
# content of the file ~/.vnc/xstartup for a VNCServer with XFCE Desktop
#!/bin/sh
# Start up the standard system desktop
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
/usr/bin/startxfce4
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
#[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
x-window-manager &
```
if u want u can also create .Xresources (not necessary.)

* ensure novnc is running first `/opt/novnc/utils/novnc_proxy --vnc localhost:5901`
then run `vncserver :1` 
u can kill vncserver by `vncserver -kill :1`

Here we go open port 6080(may be) url and enjoy.

@ other way:
 if `vncserver:1` is giving errors then just try this command
`tigervncserver -xstartup /usr/bin/xterm`
and then go to novnc website.
and in novnc site's virtual terminal.
enter the command `xfce4-session` or `xfce4-session --display=:1`

@ another way:
do not use 'xstartup', simply just launch vncserver normally.
`vncserver :1` and then manually lauch xfce4-session from main terminal where u are currently working.
`xfce4-session --display=:1`
and start in novnc site.
u can stop xfce4 by this command: `xfce4-session-logout --logout`

TIPS: use `-geometry` in vncserver for full-fit resolution.
`vncserver :1 -geometry 1535x824` #for my laptop.


########################
inside gui desktop.

install browser let's say `falkon`. [but best is firefox(install via git)]
`apt install falkon`
but it will not open directly so u can do like:
- go on `/usr/bin/` folder then open terminal there and run
`sudo env QTWEBENGINE_DISABLE_SANDBOX=1 ./MyApp` #replace MyApp with falkon or any. having same problem.

- another way that i did not try yet:
create a sub-user in Linux to get a non-root enviroment.
`sudo adduser newuser_name`
and u can also test `./MyApp --no-sandbox` command.
