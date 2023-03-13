FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y curl \
    gnupg

EXPOSE 8332 8333

COPY files/install.sh /tmp
RUN bash /tmp/install.sh

COPY files/bitcoind.conf /data/conf/

USER bitcoin
CMD bitcoind -conf=/data/conf/bitcoind.conf -datadir=/data/bitcoin
