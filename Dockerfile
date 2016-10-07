# Get UCS Firmware from CCO

FROM alpine:latest

MAINTAINER Jason Makar <jmakar@mac.com>

RUN apk add --update \
    python \
    py-pip \
&& pip install ucsmsdk \
&& rm -rf /var/cache/apk/*

RUN mkdir /ucspy

COPY get_ucs_firmware_cco.py /ucspy/get_ucs_firmware_cco.py

# ENTRYPOINT python /ucspy/get_ucs_firmware_cco.py -u