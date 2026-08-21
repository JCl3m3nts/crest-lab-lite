FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openbsd-inetd \
    fingerd \
    finger \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -c "Sarah Mitchell - IT Support - NW-FINGER-001" analyst && \
    echo "analyst:Northwind123!" | chpasswd


COPY trophy.txt /opt/trophy.txt
RUN printf '%s\n' \
    'finger stream tcp nowait nobody /usr/sbin/in.fingerd in.fingerd' \
    > /etc/inetd.conf

RUN printf '%s\n' \
    'Sarah Mitchell - IT Support' \
    'IT Support - Northwind Manufacturing' \
    'Contact: sarah.mitchell@northwind.local' \
    'CREST-FINGER-77421' \
    > /home/analyst/.plan && \
    chown analyst:analyst /home/analyst/.plan

EXPOSE 79

CMD ["/usr/sbin/inetd", "-d"]
