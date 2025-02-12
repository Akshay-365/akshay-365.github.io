@Can you make it like installing a proot distro with root user and then when through ssh giving bash terminal to client just give the bash terminal of that proot distro directly. insure that proot terminal is directly accessible through user ssh connection [not root].
```
# Use Python 3.9 base image
FROM python:3.9

# Avoid interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies with -y to auto-confirm prompts
RUN apt-get update && apt-get install -y \
    openssh-server \
    curl \
    build-essential \
    libssl-dev \
    git \
    automake \
    autoconf \
    nano \
    npm \
    systemctl \
    net-tools \
    wget && \
    rm -rf /var/lib/apt/lists/*

# Ensure the SSH runtime directory exists
RUN mkdir -p /var/run/sshd

# Generate SSH host keys automatically (as root)
RUN ssh-keygen -A

# Set SSH host private key permissions to 644 (as requested)
RUN chmod 644 /etc/ssh/ssh_host_*_key

# Update SSH configuration:
#   - Change listening port from 22 to 7860.
#   - Disable password authentication.
#   - Disable PAM.
RUN sed -i -E 's/#?Port 22/Port 7860/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config


# Create a user with UID 1000 (for key-based authentication)
RUN useradd -m -u 1000 user

# (Optional) Switch to the user so you can configure key-based authentication.
# Make sure to copy your public key into /home/user/.ssh/authorized_keys.
USER user
RUN mkdir -p /home/user/.ssh && chmod 700 /home/user/.ssh
# For example, to add a public key, you could COPY it from your build context:
# COPY authorized_keys /home/user/.ssh/authorized_keys
# RUN chmod 600 /home/user/.ssh/authorized_keys
# If you already have a key setup process, adjust accordingly.
# Create the .ssh directory, paste your public key, and set proper permissions
RUN mkdir -p /home/user/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABA..........4P3U43D1lmLCn0kN64lsK6oxXWXzw== your_email@example.com" > /home/user/.ssh/authorized_keys && \ 
    chmod 700 /home/user/.ssh && \
    chmod 600 /home/user/.ssh/authorized_keys && \
    chown -R user:user /home/user/.ssh

# Switch back to root for the remainder of the setup
USER root

# Install Code Server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Cloudflare Tunnel
RUN wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && \
    dpkg -i cloudflared-linux-amd64.deb

# Install Gsocket
RUN curl -sSL https://gsocket.io/install.sh | bash && \
    cd gsocket && ./install.sh && make install

# (Optional) Switch back to user if desired
USER user

# Set working directory
WORKDIR /app

# Copy application files (if any)
COPY . /app

# Start the SSH server (wrapped with gsocket) in the foreground
CMD ["/bin/sh", "-c", "gsocket -s nopass /usr/sbin/sshd -D"]
```





@ well i am near now to root:
```
# Use Python 3.9 base image (Debian‑based)
FROM python:3.9

# Avoid interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies, including proot, debootstrap, fakeroot, and automake
RUN apt-get update && apt-get install -y \
    openssh-server \
    curl \
    build-essential \
    libssl-dev \
    git \
    automake \
    autoconf \
    nano \
    npm \
    systemctl \
    net-tools \
    wget \
    proot \
    debootstrap \
    fakeroot && \
    rm -rf /var/lib/apt/lists/*

# Ensure the SSH runtime directory exists
RUN mkdir -p /var/run/sshd

# Generate SSH host keys automatically
RUN ssh-keygen -A

# Set SSH host private key permissions
RUN chmod 644 /etc/ssh/ssh_host_*_key

# Update SSH configuration:
#   - Change listening port from 22 to 7860.
#   - Disable password authentication.
#   - Disable PAM.
#   - Disallow root login (forcing SSH access via the non‑root user).
RUN sed -i -E 's/#?Port 22/Port 7860/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config

# Create a non‑root user with UID 1000
RUN useradd -m -u 1000 user

# Switch to the non‑root user to set up key‑based authentication.
USER user
RUN mkdir -p /home/user/.ssh && chmod 700 /home/user/.ssh
# Replace the key below with your own public key.
RUN echo "ssh-rsa AAAAB3NzaC1yc2EA.........Uic6MA0F+yYHgBubqT5WAtitzeLYEaWK7gfK4qvz0AI0wLdTvFfvlIEKJCP0dKplGXE92JCkNEsK8b4P3U43D1lmLCn0kN64lsK6oxXWXzw== your_email@example.com" \
    > /home/user/.ssh/authorized_keys && \
    chmod 600 /home/user/.ssh/authorized_keys && \
    chown -R user:user /home/user/.ssh

# Switch back to root for remaining setup
USER root

# (Optional) Install additional tools: Code Server, Cloudflare Tunnel, and Gsocket
RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && \
    dpkg -i cloudflared-linux-amd64.deb
RUN curl -sSL https://gsocket.io/install.sh | bash && \
    cd gsocket && ./install.sh && make install

# --- Set up the proot distro ---
# Use fakeroot to bypass device node creation issues.
RUN fakeroot debootstrap --variant=minbase --no-check-gpg bullseye /proot-distro http://deb.debian.org/debian/

# Create a wrapper script that launches a bash shell within the proot distro.
# Options:
#   - "-0": emulate root privileges in proot.
#   - "-r /proot-distro": use our new root filesystem.
#   - "-b /dev -b /proc": bind host /dev and /proc.
#   - "-w /root": set the working directory.
RUN echo '#!/bin/bash' > /usr/local/bin/proot-bash.sh && \
    echo 'exec proot -0 -r /proot-distro -b /dev -b /proc -w /root /bin/bash' >> /usr/local/bin/proot-bash.sh && \
    chmod +x /usr/local/bin/proot-bash.sh

# Change the non‑root user's login shell to the proot wrapper script.
RUN usermod -s /usr/local/bin/proot-bash.sh user

# Final step: switch to non‑root user so that SSH sessions use the proper environment.
USER user

# Set working directory and copy application files, if any.
WORKDIR /app
COPY . /app

# Start the SSH server (wrapped with gsocket) in the foreground.
CMD ["/bin/sh", "-c", "gsocket -s fvfdxr45evvf /usr/sbin/sshd -D"]
```

@ just another simplified, nice , but not root priviledge.

```
# Use Python 3.9 base image
FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y \
    systemctl \
    openssh-server \
    curl \
    build-essential \
    libssl-dev \
    git \
    automake \
    autoconf \
    nano \
    npm \
    systemctl \
    net-tools \
    wget \
    sudo \
    gnupg \
    ca-certificates \
    libcap2-bin && \
    rm -rf /var/lib/apt/lists/*
    
# Create a user
RUN useradd -m -u 1000 -s /bin/bash user

# Generate SSH host keys properly
# Ensure the SSH runtime directory exists
RUN mkdir -p /var/run/sshd

# Generate SSH host keys automatically (as root)
RUN ssh-keygen -A

# Set SSH host private key permissions to 644 (as requested)
RUN chmod 644 /etc/ssh/ssh_host_*_key


# Configure SSH
RUN sed -i -E 's/#?Port 22/Port 7860/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PermitEmptyPasswords .*/PermitEmptyPasswords yes/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?ChallengeResponseAuthentication .*/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PermitRootLogin .*/PermitRootLogin forced-commands-only/' /etc/ssh/sshd_config

# Force user to always get a root shell
RUN echo 'Match User user\n\tForceCommand /bin/bash' >> /etc/ssh/sshd_config

# Install Gsocket
RUN curl -sSL https://gsocket.io/install.sh | bash && \
    cd gsocket && ./install.sh && make install

# Set up SSH authorized keys
RUN mkdir -p /home/user/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8MNnoeALNRO.....WXzw== your_email@example.com" > /home/user/.ssh/authorized_keys && \
    chmod 700 /home/user/.ssh && chmod 600 /home/user/.ssh/authorized_keys && \
    chown -R user:user /home/user/.ssh

# Expose SSH port
EXPOSE 7860

# Start SSH server wrapped with gsocket
CMD ["gsocket", "-s", "killpass", "/usr/sbin/sshd", "-D"]
```


@ i was working on it, but it cannot establish ssh connection.

```
# Use Python 3.9 base image
FROM python:3.9

# Avoid interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    openssh-server \
    curl \
    build-essential \
    libssl-dev \
    git \
    automake \
    autoconf \
    nano \
    npm \
    systemctl \
    net-tools \
    wget \
    sudo \
    gnupg \
    ca-certificates \
    libcap2-bin && \
    rm -rf /var/lib/apt/lists/*

# Ensure the SSH runtime directory exists
RUN mkdir -p /var/run/sshd

# Generate SSH host keys (as root)
RUN ssh-keygen -A

# Set SSH host private key permissions to 644
RUN chmod 644 /etc/ssh/ssh_host_*_key

# Update SSH configuration:
#   - Change port 22 to 7860.
#   - Disable password authentication.
#   - Disable PAM.
#   - And (optionally) disallow SSH login as root.
RUN sed -i -E 's/#?Port 22/Port 7860/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PermitEmptyPasswords .*/PermitEmptyPasswords yes/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?ChallengeResponseAuthentication .*/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && \
    sed -i -E 's/#?PermitRootLogin .*/PermitRootLogin without-password/' /etc/ssh/sshd_config 

# Update SSH client configuration to set PermitRootLogin to forced-commands-only
# RUN echo "PermitRootLogin forced-commands-only" >> /etc/ssh/ssh_config

# Restart both ssh and sshd services to apply the changes
# RUN service ssh restart && service sshd restart

# ----------------------------
# Create a non‑root user and grant sudo privileges
# (We initially give it UID 1000.)
# ----------------------------
RUN useradd -m -u 1000 -s /bin/bash user && \
    usermod -aG sudo user && \
    echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user

# Create the .ssh directory for the user, add an authorized_keys file, and set permissions
RUN mkdir -p /home/user/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8MNnoeALNR....+YZU4VE8xu/f9cZuS0+x4Qv35fHrYr7dqwsLGuibLPt4lfXtLHbBUKjzmv1nSXc3YDwbqD3Uic6MA0F+yYHgBubqT5WAtitzeLYEaWK7gfK4qvz0AI0wLdTvFfvlIEKJCP0dKplGXE92JCkNEsK8b4P3U43D1lmLCn0kN64lsK6oxXWXzw== your_email@example.com" \
         > /home/user/.ssh/authorized_keys && \
    chmod 700 /home/user/.ssh && \
    chmod 600 /home/user/.ssh/authorized_keys && \
    chown -R user:user /home/user/.ssh

# ----------------------------
# Give the "user" account full root privileges
# by changing its UID from 1000 to 0.
# (This way no sudo/privilege‑escalation is necessary at runtime.)
# ----------------------------
RUN sed -i 's/^user:x:1000:/user:x:0:/' /etc/passwd && \
    chown -R user:user /home/user

# or
# RUN useradd -m -u 0 -o -s /bin/bash user && \
#     echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user


# ----------------------------
# (Continue with installations that require root.)
# Switch back to root to install Code Server, Cloudflare Tunnel, Gsocket, etc.
# ----------------------------
USER root

# Install Code Server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Cloudflare Tunnel
RUN wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && \
    dpkg -i cloudflared-linux-amd64.deb

# Install Gsocket
RUN curl -sSL https://gsocket.io/install.sh | bash && \
    cd gsocket && ./install.sh && make install

# (We no longer install or use gosu since our "user" is now effectively root.)

# ----------------------------
# Set working directory and copy application files
# ----------------------------
WORKDIR /app
COPY . /app

# ----------------------------
# Switch to the "user" account (which now has UID 0)
# ----------------------------
USER user

# Expose the SSH port (optional)
EXPOSE 7860

# Start the SSH server (with gsocket as desired) in the foreground
CMD ["gsocket", "-s", "hipass", "/usr/sbin/sshd", "-D"]

```
