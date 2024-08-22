# HTTPS SSL

![http termination image](https://www.x-cart.com/img/8527/http_to_https-1.webp)

> SSL stands for Secure Sockets Layer and, in short, it's the standard technology for keeping an internet connection secure and safeguarding any sensitive data that is being sent between two systems, preventing criminals from reading and modifying any information transferred, including potential personal details. The two systems can be a server and a client (for example, a shopping website and browser) or server to server (for example, an application with personal identifiable information or with payroll information).

> HTTPS (Hyper Text Transfer Protocol Secure) appears in the URL when a website is secured by an SSL certificate. The details of the certificate, including the issuing authority and the corporate name of the website owner, can be viewed by clicking on the lock symbol on the browser bar.

__What happens when you don’t secure your website traffic?__

![http termination gif](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif)

## Prerequisites

- What is `HTTPS`?
- What are the __2 main elements that SSL is providing__
- `HAProxy` __SSL termination on__ `Ubuntu16.04`
- __SSL termination__
- __Bash function__

## Tasks :heavy_check_mark:

- [0-world_wide_web](./0-world_wide_web)
- [1-haproxy_ssl_termination](./1-haproxy_ssl_termination)
- [100-redirect_http_to_https](./100-redirect_http_to_https)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck (version 0.3.7)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Resource

[wiki](https://en.wikipedia.org/wiki/TLS_termination_proxy)
[haproxy](https://www.haproxy.com/blog/haproxy-ssl-termination)
[digital](https://www.digitalocean.com/community/tutorials/how-to-implement-ssl-termination-with-haproxy-on-ubuntu-14-04)
[media](https://antmedia.io/docs/guides/clustering-and-scaling/load-balancing/load-balancer-with-haproxy-ssl-termination/?utm_source=github&utm_medium=wiki)

## CONFIGURE DNS to add sub domain

CONFIGURE :DNS Settings: Ensure that the DNS record for `www.samueleffiong.tech` is correctly and do for all servers.
configured in your domain's DNS settings. You should have an A record pointing www to the correct IP address.

Propagation Time: DNS changes can take some time to propagate. If you recently updated or added the record, wait a few hours and try again.

Verify with Other Tools: Use an external DNS checker tool like `dnschecker.org` to see if the DNS record is visible globally.

It looks like you have successfully set up the A records for your subdomains on the domain effiongsamuel.tech. Here's a summary of your DNS configuration:

```www.effiongsamuel.tech: Points to IP 34.202.234.6
lb-01.effiongsamuel.tech: Points to IP 34.202.234.6
web-01.effiongsamuel.tech: Points to IP 3.85.141.200
web-02.effiongsamuel.tech: Points to IP 54.236.190.52
```

```bash
$ ubuntu@139694-lb-01:~$ sudo systemctl restart systemd-resolved
$ ubuntu@139694-lb-01:~$ dig lb-01.effiongsamuel.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.effiongsamuel.tech. 300   IN      A       34.202.234.6
$ ubuntu@139694-lb-01:~$ dig web-01.effiongsamuel.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.effiongsamuel.tech. 300  IN      A       3.85.141.200
$ ubuntu@139694-lb-01:~$ dig web-02.effiongsamuel.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
$ web-02.effiongsamuel.tech. 300  IN      A       54.236.190.52
$ ubuntu@139694-lb-01:~$ ./sub effiongsamuel.tech
The subdomain www is a A record and points to 34.202.234.6
The subdomain lb-01 is a A record and points to 34.202.234.6
The subdomain web-01 is a A record and points to 3.85.141.200
The subdomain web-02 is a A record and points to 54.236.190.52
$ ubuntu@139694-lb-01:~$ ./sub effiongsamuel.tech web-02
The subdomain web-02 is a A record and points to 54.236.190.52
$ ubuntu@139694-lb-01:~$ ./sub effiongsamuel.tech web-01
The subdomain web-01 is a A record and points to 3.85.141.200
$ ubuntu@139694-lb-01:~$ ./sub effiongsamuel.tech lb-1
The subdomain lb-1 is a  record and points to
$ buntu@139694-lb-01:~$ ./sub effiongsamuel.tech lb-01
The subdomain lb-01 is a A record and points to 34.202.234.6
$ ubuntu@139694-lb-01:~
```

## Installing SSL Termination on Haproxy

- Linux Distro: __Ubuntu 20.04 LTS__
- HAProxy Version: __v2.4.3__

```bash

#if you already have haproxy installed do this
$ sudo snap install --classic certbot

# check if haproxy is installed, if yes stop haproxy
$ sudo service haproxy stop

# Install ssl using certbot
$ sudo certbot certonly --standalone

# Follow the instrustions accurately, at the end please take note of the
# Location of your SSL Keys. Usually going to default to the /etc/letsencrypt
# when below shows: 
# Successfully received certificate.
# Certificate is saved at: /etc/letsencrypt/live/www.effiongsamuel.tech/fullchain.pem
# Key is saved at:         /etc/letsencrypt/live/www.effiongsamuel.tech/privkey.pem
# This certificate expires on 2024-11-20.
# These files will be updated when the certificate renews.
# Certbot has set up a scheduled task to automatically renew this certificate in the background.
# directory. To view them do the below
$ ls /etc/letsencrypt/live/domain_name/

# Combine the PEM files by writting script and and place blow command
    #!/bin/bash

    DOMAIN='www.effiongsamuel.tech'

    # Create the directory if it does not exist
    sudo mkdir -p /etc/haproxy/certs

    # Combine the certificates into a single file
    sudo -E bash -c "cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem"

    # Set permissions for the certificate directory
    sudo chmod -R go-rwx /etc/haproxy/certs

# or 

# Now concat your certificate .pem files to a single pem file and save them to
# /etc/ssl/private
$ cat cert_key_1 cert_key_2 > /etc/ssl/private/any_desired_name.pem

# Configuring HAProxy
    #Backup the default configuration file
    $ mv /etc/haproxy/haproxy.cfg{,_backup}

    # Create a new configuration file
    sudo vi /etc/haproxy/haproxy.cfg

    # confirm file is properly written
    sudo haproxy -c -f /etc/haproxy/haproxy.cfg


# Now go to your haproxy config file to add a the path to your certificate
# Then restart haproxy
$ sudo service haproxy restart

# Check the Status
$ sudo service haproxy status
```

__If you don't have HAProxy installed just copy and run this on your terminal and save yourself the hassle_

```bash
wget -O haproxy https://github.com/samueleffiongjacob/alx-system_engineering-devops/raw/master/0x0F-load_balancer/install_haproxy_safely && bash haproxy

```
