#!/bin/bash
VERSION=22.0
ARCH="x86_64"

echo "Installing Bitcoind $VERSION"

setup(){
    mkdir /tmp/bitcoin
    mkdir -p /data/{bitcoin,conf}
    useradd bitcoin
    chown -R bitcoin: /data
    echo "Setup done"
}

get_files(){
    curl -o /tmp/bitcoin/SHA256SUMS.asc https://bitcoin.org/bin/bitcoin-core-${VERSION}/SHA256SUMS.asc
    curl -o /tmp/bitcoin/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz https://bitcoin.org/bin/bitcoin-core-${VERSION}/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz
    tar xzf /tmp/bitcoin/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz -C /tmp/bitcoin
    #sha256=$(sha256sum /tmp/bitcoin/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz | awk '{print $1}')
    #grep -w $sha256 /tmp/bitcoin/SHA256SUMS.asc

    #if [ $? -eq 0 ]; then
    #    tar xzf /tmp/bitcoin/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz -C /tmp/bitcoin
    #else
    #    echo "SHA256SUMS is invalid!"
    #    exit 1
    #fi
    echo "Files done"
}

copy_files(){
    cp /tmp/bitcoin/bitcoin-${VERSION}/bin/bitcoind /usr/local/bin/bitcoind
    cp /tmp/bitcoin/bitcoin-${VERSION}/bin/bitcoin-cli /usr/local/bin/bitcoin-cli
    echo "Copy done"
}

setup
get_files
copy_files
