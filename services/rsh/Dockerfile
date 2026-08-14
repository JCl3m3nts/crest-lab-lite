FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openbsd-inetd \
    rsh-redone-server \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -g operator -c "David Wilson - Operations" operator && \
    echo "operator:Northwind123!" | chpasswd

RUN printf '%s\n' \
    'shell stream tcp nowait root /usr/sbin/in.rshd in.rshd' \
    > /etc/inetd.conf

RUN printf '%s\n' \
    '172.30.0.1 operator' \
    > /etc/hosts.equiv

RUN printf '%s\n' \
    '172.30.0.1 operator' \
    > /home/operator/.rhosts && \
    chown operator:operator /home/operator/.rhosts && \
    chmod 600 /home/operator/.rhosts




RUN printf '%s\n' \
    'CREST-RSH-66318' \
    > /home/operator/rsh_trophy.txt

RUN chown operator:operator /home/operator/rsh_trophy.txt

EXPOSE 514

CMD ["/usr/sbin/inetd", "-d"]
