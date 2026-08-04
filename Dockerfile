FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    supervisor \
    curl \
    nano \
    net-tools \
    iproute2 \
    nmap \
    && apt clean

WORKDIR /crest

COPY portal/requirements.txt .

RUN pip3 install -r requirements.txt

COPY portal/app /crest/app
COPY data /crest/data

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord","-n"]
