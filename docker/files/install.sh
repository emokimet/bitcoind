#!/bin/bash
if [[ -z "${VERSION}" ]]; then
    echo "VERSION is not set"
    exit 1
else
    VERSION=${VERSION}
fi
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
    curl -o /tmp/bitcoin/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz https://bitcoincore.org/bin/bitcoin-core-${VERSION}/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz
    tar xzf /tmp/bitcoin/bitcoin-${VERSION}-${ARCH}-linux-gnu.tar.gz -C /tmp/bitcoin
    echo "No file verification, FTW!!"
}

copy_files(){
    cp /tmp/bitcoin/bitcoin-${VERSION}/bin/bitcoind /usr/local/bin/bitcoind
    cp /tmp/bitcoin/bitcoin-${VERSION}/bin/bitcoin-cli /usr/local/bin/bitcoin-cli
    echo "Copy done"
}

setup
get_files
copy_files
