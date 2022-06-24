FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt upgrade -y && \
    apt install -y --no-install-recommends \
    build-essential python3 python3-distutils python3-dev curl \
    git libpcre3 libpcre3-dev \
    pkg-config swig libcairo2-dev libnetpbm10-dev netpbm libpng-dev libjpeg-dev \
    zlib1g-dev libbz2-dev libcfitsio-dev wcslib-dev python3-pip file && \
    apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install numpy scipy Django fitsio uwsgi tzdata

RUN git clone https://github.com/dstndstn/astrometry.net.git astrometry \
  && cd astrometry && git checkout 0.84
RUN cd astrometry && make && make py && make extra && make install

RUN git clone https://github.com/dstndstn/unwise.me.git

COPY entry.sh /app

ENTRYPOINT ["/app/entry.sh"]
