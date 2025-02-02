---
layout: post
title: "Remote SSH."
date: 2025-01-20 14:00:00
description: Remote SSH. # Add post description (optional)
img: /video_player.jpg # Add image post (optional)
categories: remote ssh
tags: [ssh, tunnel , socket]
---

for remote ssh:
- first install openssh
sudo apt-get update && sudo apt-get install -y openssh-server
sudo nano /etc/ssh/sshd_config
*Edit the port according to u. lets's say 8081

- then install gsocket.
curl -sSL https://gsocket.io/install.sh | bash
*if needed now go to gsocket folder and then ./gsocket and then make install as guided.
now on server use 'which sshd' for confirming the location
then on SERVER run:
gsocket /usr/sbin/sshd -d
and then enter any {PASS_KEY}

now on CLIENT:
gsocket -s PASS_KEY ssh root@gsocket -p 8081 # your eneter pass_key on server.
# root or any user available on server

##############################################
<hr />
<hr />
##############################################

@ngrok install:
```
# Remove the old version of ngrok if available
rm -f ngrok

# Download the latest ngrok version (Linux)
curl -o ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

# Unzip it
unzip ngrok.zip

# Give execute permissions to ngrok
chmod +x ngrok
```

@code-server install:
```
curl -fsSL https://code-server.dev/install.sh | sh

code-server --bind-addr 0.0.0.0:7860 --auth none

ngrok http 7860
```

one single command:
code-server --bind-addr 0.0.0.0:7860 --auth none & ngrok http 7860

extras:
BONUS:

install socat 'may be apt install socat'
 to transfer the port whithin localhost:

``` socat TCP-LISTEN:2222,fork TCP:localhost:8081 ``` 
from 8081 to 2222.

Using Localtunnel:
1. npm install -g localtunnel
2. lt --port 8081    #or any port 8082..etc
 it will give url like this:
  `https://your-subdomain.loca.lt`

the url can be used for ssh to turn local ip [hostname -I] into public like.
 `` ssh username@your-subdomain.loca.lt -p 8081 ``
(not worked in my test for now. but very useful for further uses)

 SSH tunneling:
 For me, first run localtunnel 'It --port 8081', then u will get a link, then u can replace it with local ip.
 Set up a reverse SSH tunnel on @SERVER:
` ssh -R 8082:localhost:8082 username@remote-server-ip`
- `ssh -R 8082:localhost:8082 root@your-subdomain.loca.lt`
  
Access SSH from @CLIENT:
ssh -p 8082 username@remote-server-ip
# change accordingly.   (play around it..) [❌ but do not waste time.]

Ngrok tcp addressing/forwarding:
 `ngrok tcp 8081`
# may be only one task at a time in ngrok allowed or may be paid fot tcp..


# Very simple, go as you click:
* Cloudflared (Argo Tunnel):
```
apt-get install wget
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
dpkg -i cloudflared-linux-amd64.deb
```
` cloudflared --version `
`` cloudflared tunnel --url http://localhost:8081 ``
Full command to run code-server:
` code-server --bind-addr 0.0.0.0:7860 --auth none & cloudflared tunnel --url http://localhost:7860 `
 also know this more:
*Optional: Run in the Background
If you want to keep cloudflared running in the background, use nohup:
` nohup cloudflared tunnel --url http://localhost:8081 > cloudflared.log 2>&1 & `

# MORE TO EXPLORE:
BORE [https://github.com/ekzhang/bore] similar to gsocket:
exposes local ports to a remote server, bypassing standard NAT connection firewalls.
commands:
`
cargo install bore-cli
bore local 8000 --to bore.pub
`
and 
```
# on the server
bore server --secret my_secret_string

# on the client
bore local <LOCAL_PORT> --to <TO> --secret my_secret_string
```
And other tools like:
- https://github.com/exposesh
- https://telebit.cloud/
- https://github.com/anderspitman/awesome-tunneling?tab=readme-ov-file #awesome-tools

  ######################################################################################################################################
  ######################################################################################################################################
  ######################################################################################################################################

  commands i use often to setup code-server and stuff.
  ```
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

# Run it after above installation
code-server --bind-addr 0.0.0.0:7860 --auth none & cloudflared tunnel --url http://localhost:7860

# for gsocket:
curl -sSL https://gsocket.io/install.sh | bash
# [then just go to gsocket folder and do]
cd gsocket
./install.sh
# (then again a new gsocket folder will be created go inside that)
cd gsocket
# now do
make install
```
