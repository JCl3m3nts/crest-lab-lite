FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    bind9 \
    bind9utils \
    dnsutils && \
    rm -rf /var/lib/apt/lists/*

COPY named.conf.local /etc/bind/named.conf.local
COPY db.northwind.local /etc/bind/db.northwind.local

EXPOSE 53/tcp
EXPOSE 53/udp

CMD ["named", "-g"]
