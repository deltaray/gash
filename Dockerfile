from debian:stable

RUN apt update && apt install -y \
    psmisc \
    nano \
    tree \
    x11-apps \
    python3 \
    gcc \
    wget \
 && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/phyver/GameShell/raw/master/GameShell.tgz -O - | tar -xz

ENTRYPOINT ./GameShell/start.sh
