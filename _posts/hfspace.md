@Can you make it like installing a proot distro with root user and then when through ssh giving bash terminal to client just give the bash terminal of that proot distro directly. insure that proot terminal is directly accessible through user ssh connection [not root].

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
