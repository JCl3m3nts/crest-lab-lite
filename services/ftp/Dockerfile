FROM ubuntu:24.04

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y vsftpd && \
    rm -rf /var/lib/apt/lists/*


COPY vsftpd.conf /etc/vsftpd.conf

COPY share /srv/ftp

RUN chmod -R 755 /srv/ftp


RUN useradd -m ftpuser


EXPOSE 21


CMD ["/usr/sbin/vsftpd","/etc/vsftpd.conf"]
