FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    telnetd \
    openbsd-inetd \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -N operator && \
    echo "operator:Northwind123!" | chpasswd

COPY trophy.txt /opt/trophy.txt

RUN chmod 644 /opt/trophy.txt

RUN echo "telnet stream tcp nowait root /usr/sbin/telnetd telnetd" \
    > /etc/inetd.conf

EXPOSE 23

CMD ["/usr/sbin/inetd","-d"]
