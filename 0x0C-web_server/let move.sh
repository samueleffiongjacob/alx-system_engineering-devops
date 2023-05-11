#!/usr/bin/env bash

sudo add-apt-repository ppa:certbot/certbot
sudo apt update
sudo apt install snapd
sudo apt-get remove certbot
sudo apt-get install certbot
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d effiongsamuel.tech -d www.effiongsamuel.tech
sudo ls /etc/letsencrypt/live/effiongsamuel.tech
sudo mkdir -p /etc/haproxy/certs
DOMAIN='effiongsamuel.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs

 https://act.eff.org.