#!/bin/bash

set -e

usage () {
        echo usage: "$0" \<keydir\> \<serverhost\> \[client1\] \[client2\] ... \[clientn\]
        echo Create CA and server host keys for faucetconfrpc, and optionally client keys.
        echo CA and server host names are required. Existing CA and server/client keys will be preserved - only keys not already existing will be created.
}

KEYDIR=$1
if [[ "$KEYDIR" == "" ]] ; then
	echo must specify key directory
	usage
	exit 1
fi
shift

SERVERHOST=$1
if [[ "$SERVERHOST" == "" ]] ; then
	echo must specify faucetconfrpc server name
	usage
	exit 1
fi
shift

CS="certstrap --depot-path $KEYDIR"
CA=${SERVERHOST}-ca

if [[ ! -d "$KEYDIR" ]] ; then
	echo creating "$KEYDIR"
	mkdir -p "$KEYDIR"
fi
if [[ ! -f "$KEYDIR/$CA.crt" ]] ; then
	if [[ -f "$KEYDIR/*.crl" ]] ; then
		echo CA already exists that does not match "$CA"
		exit 1
	fi
	echo creating CA "$CA" and server host keys
	$CS init --common-name "$CA" --passphrase ""
	$CS request-cert --domain "$SERVERHOST" --common-name "$SERVERHOST" --passphrase ""
	$CS sign "$SERVERHOST" --CA "$CA"
fi
for host in "$@" ; do
	if [[ -f "$KEYDIR/$host.crt" ]] ; then
		echo skip creating existing client key for "$host"
		continue
	fi
	echo creating client key "$host"
	$CS request-cert --common-name "$host" --passphrase ""
	$CS sign "$host" --CA "$CA"
done
