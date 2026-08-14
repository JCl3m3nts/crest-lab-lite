FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    dovecot-pop3d \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -c "Emma Carter - HR" hr && \
    echo "hr:Northwind123!" | chpasswd

RUN printf '%s\n' \
    'CREST-POP3-39527' \
    > /home/hr/pop3_trophy.txt

RUN chown hr:hr /home/hr/pop3_trophy.txt

RUN sed -i 's/^#disable_plaintext_auth = yes/disable_plaintext_auth = no/' /etc/dovecot/conf.d/10-auth.conf && \
    sed -i 's/^auth_mechanisms = plain/auth_mechanisms = plain login/' /etc/dovecot/conf.d/10-auth.conf

RUN printf '%s\n' \
    'listen = *' \
    'protocols = pop3' \
    'mail_location = maildir:~/Maildir' \
    > /etc/dovecot/conf.d/99-crest.conf

EXPOSE 110

CMD ["/usr/sbin/dovecot", "-F"]
