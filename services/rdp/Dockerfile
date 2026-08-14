FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    xrdp \
    xfce4 \
    xfce4-goodies \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -c "Michael Turner - Finance" rdpuser && \
    echo "rdpuser:Northwind123!" | chpasswd

RUN echo "NW-RDP-001" > /etc/hostname

RUN printf '%s\n' \
    'CREST-RDP-51842' \
    > /home/rdpuser/rdp_trophy.txt

RUN chown rdpuser:rdpuser /home/rdpuser/rdp_trophy.txt

RUN echo "startxfce4" > /home/rdpuser/.xsession && \
    chown rdpuser:rdpuser /home/rdpuser/.xsession

EXPOSE 3389

CMD ["/usr/sbin/xrdp", "--nodaemon"]
