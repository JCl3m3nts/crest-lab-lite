FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    postfix \
    && rm -rf /var/lib/apt/lists/*

RUN echo "smtp.northwind.local" > /etc/mailname

RUN useradd -m -c "Rachel Adams - Sales" sales && \
    echo "sales:Northwind123!" | chpasswd

RUN printf '%s\n' \
    'CREST-SMTP-84216' \
    > /home/sales/smtp_trophy.txt

RUN chown sales:sales /home/sales/smtp_trophy.txt

RUN postconf -e "myhostname = smtp.northwind.local" && \
    postconf -e "mydomain = northwind.local" && \
    postconf -e "myorigin = \$mydomain" && \
    postconf -e "inet_interfaces = all" && \
    postconf -e "mynetworks = 127.0.0.0/8 172.30.0.0/24" && \
    postconf -e "smtpd_banner = \$myhostname ESMTP Northwind Manufacturing" && \
    postconf -e "smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination"

EXPOSE 25

CMD ["postfix", "start-fg"]
