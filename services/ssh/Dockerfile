FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        openssh-server && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN useradd -m analyst

RUN echo "analyst:Password123!" | chpasswd

COPY trophies /opt/trophies

RUN chmod -R 755 /opt/trophies

EXPOSE 22

CMD ["/usr/sbin/sshd","-D","-e"]
