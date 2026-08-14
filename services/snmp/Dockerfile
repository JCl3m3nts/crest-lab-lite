FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        snmpd snmp && \
    rm -rf /var/lib/apt/lists/*

COPY snmpd.conf /etc/snmp/snmpd.conf
COPY extend.sh /opt/extend.sh
COPY trophy.txt /opt/trophy.txt

RUN chmod +x /opt/extend.sh

EXPOSE 161/udp

CMD ["/usr/sbin/snmpd","-f","-Lo"]
