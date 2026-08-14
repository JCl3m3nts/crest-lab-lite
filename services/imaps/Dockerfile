FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    dovecot-imapd \
    openssl \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -c "Laura Bennett - Finance" imapuser && \
    echo "imapuser:Northwind123!" | chpasswd

RUN echo "IMAPS-SERVER01" > /etc/hostname

RUN printf '%s\n' \
    'CREST-IMAPS-61527' \
    > /home/imapuser/imaps_trophy.txt && \
    chown imapuser:imapuser /home/imapuser/imaps_trophy.txt

RUN mkdir -p /home/imapuser/Maildir/{cur,new,tmp} && \
    chown -R imapuser:imapuser /home/imapuser/Maildir

RUN openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 \
    -keyout /etc/dovecot/private/dovecot.key \
    -out /etc/dovecot/dovecot.crt \
    -subj "/CN=imap.northwind.local" && \
    chmod 600 /etc/dovecot/private/dovecot.key

RUN printf '%s\n' \
    'ssl = yes' \
    'ssl_cert = </etc/dovecot/dovecot.crt' \
    'ssl_key = </etc/dovecot/private/dovecot.key' \
    'disable_plaintext_auth = no' \
    'auth_mechanisms = plain login' \
    'mail_location = maildir:~/Maildir' \
    > /etc/dovecot/conf.d/99-crest-imaps.conf

RUN printf '%s\n' \
    'service imap-login {' \
    '  inet_listener imap {' \
    '    port = 0' \
    '  }' \
    '  inet_listener imaps {' \
    '    port = 993' \
    '    ssl = yes' \
    '  }' \
    '}' \
    > /etc/dovecot/conf.d/99-crest-listener.conf

EXPOSE 993

CMD ["/usr/sbin/dovecot", "-F"]
