FROM ubuntu:24.04

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    samba \
    samba-common-bin \
    && rm -rf /var/lib/apt/lists/*

COPY smb.conf /etc/samba/smb.conf

COPY shares /shares

RUN chmod -R 755 /shares

EXPOSE 139 445

CMD ["smbd", "--foreground", "--no-process-group"]
