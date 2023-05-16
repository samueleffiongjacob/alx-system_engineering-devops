# 0x10. HTTPS SSL 

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png"/>
</p>

## Prerequisites
- What is `HTTPS`?
- What are the __2 main elements that SSL is providing__
- `HAProxy` __SSL termination on__ `Ubuntu16.04`
- __SSL termination__
- __Bash function__

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck (version 0.3.7)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Installing SSL Termination on Haproxy
- Linux Distro: __Ubuntu 20.04 LTS__
- HAProxy Version: __v2.4.3__

## Resource

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)

- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)

- [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/)

- [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)

- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)

- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

- [How to Secure HAProxy with Let's Encrypt on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04)

- [HAProxy SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination/)

- [haproxy configuration](https://www.ssllabs.com/ssltest/)

- [haproxy configuraton](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)

- [User Guide documentation certbot](https://eff-certbot.readthedocs.io/en/stable/using.html#changing-a-certificate-s-key-type)


- [certbot ssl generator official site](https://certbot.eff.org/)

- [certbot instructions FOR haproxy in ubuntu --versions and installation guide](https://certbot.eff.org/instructions?ws=haproxy&os=ubuntufocal)

- [DEV GUIDE FOR Setting up SSL Certificates for HAProxy with certbot](https://dev.to/phansch/setting-up-ssl-certificates-for-haproxy-with-certbot-bb0)


- [Skarlso's guide for Haproxy](https://skarlso.github.io/2017/02/15/how-to-https-with-hugo-letsencrypt-haproxy/)

- [More on cebort configur](https://markontech.com/linux/install-lets-encrypt-ssl-on-haproxy/)


- [More efficient guide](https://www.linuxtechi.com/how-to-setup-haproxy-ssl-termination-ubuntu/)

- [just a random documentation on haproxy ](https://serversforhackers.com/c/letsencrypt-with-haproxy)

man (awk, dig)
## Tasks :heavy_check_mark:

<details>
<summary><a href="./0-world_wide_web">0. World wide web</a></summary><br>
<a href='https://postimg.cc/w3QxtHzN' target='_blank'><img src='https://i.postimg.cc/Y2Jvsqyd/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-haproxy_ssl_termination">1. HAproxy SSL termination</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/jSy72SG2/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./100-redirect_http_to_https">2. No loophole in your website traffic</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/Njtg78N1/image.png' border='0' alt='image'/></a>
</details>


# HTTPS SSL

![](https://www.x-cart.com/img/8527/http_to_https-1.webp)

> SSL stands for Secure Sockets Layer and, in short, it's the standard technology for keeping an internet connection secure and safeguarding any sensitive data that is being sent between two systems, preventing criminals from reading and modifying any information transferred, including potential personal details. The two systems can be a server and a client (for example, a shopping website and browser) or server to server (for example, an application with personal identifiable information or with payroll information).

> HTTPS (Hyper Text Transfer Protocol Secure) appears in the URL when a website is secured by an SSL certificate. The details of the certificate, including the issuing authority and the corporate name of the website owner, can be viewed by clicking on the lock symbol on the browser bar.

__What happens when you don’t secure your website traffic?__
<img src='https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif'>

```bash
# First update your sofrware: 
$ sudo apt update

# if u are on Ubuntu 18.04 and above Snap is pre-installed  for you. your would not need to install.

# if u are using  a version of ubuntu lower than Ubuntu 18.04 then snap you most intall

$ sudo apt install snapd

# Ensure that your version of snapd is up to date
$ sudo snap install core; sudo snap refresh core

# Remove certbot-auto and any Certbot OS package: The exact command to do this depends on your OS, but common examples are

$ sudo apt-get remove certbot # for linux distribustion

$ sudo dnf remove certbot

$ sudo yum remove certbot

# you are now ready to install cerbort . Note: make sure you have haproxy installed befor doing  this
$ sudo snap install --classic certbot

#Prepare the Certbot command
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot

# check if haproxy is installed
$ sudo service haproxy status

# stop haproxy 
$ sudo service haproxy stop

# Install ssl using certbot
$ sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d exaple.com --non-interactive --agree-tos --email youremail@gmail.com

# if error : Could not bind TCP port 80 because it is already in use by another process on this system (such as a web server). Please stop the program in question and then try again.

# do this below:
$ sudo lsof -i tcp:80
$ sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill

# but if no error proceed below.

# Follow the instrustions accurately, at the end please take note of the
# Location of your SSL Keys. Usually going to default to the /etc/letsencrypt
# directory. To view them do the below
$ sudo ls /etc/letsencrypt/live/example.com

$ sudo mkdir -p /etc/haproxy/certs

$ DOMAIN='example.com' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'

# give permission to the above folder
$ sudo chmod -R go-rwx /etc/haproxy/certs

#     or this
# Now concat your certificate .pem files to a single pem file and save them to
# /etc/ssl/private
$ sudo cat "/etc/letsencrypt/live/example.com/fullchain.pem" "/etc/letsencrypt/live/example.com/privkey.pem" > "/etc/ssl/example.com.pem"

# Now go to your haproxy config file to add a the path to your certificate
$ sudo vi /etc/haproxy/haproxy.cfg

# add your config file in haproxy inside the above open
  
frontend effiongsamuel-tech-backend
    bind *:80
    default_backend effiongsamuel-tech-backend

backend effiongsamuel-tech-backend
    balance roundrobin
    server 139694-web-01 1033.2956.178.1:80 check # your server ip
    server 139694-web-02 34.2302.15457.245:80 check # your server ip
# Then reload haproxy
$ sudo service haproxy reload
```
_If you don't have HAProxy installed just copy and run this on your terminal and save yourself the hassle_

```
$ wget -O haproxy https://github.com/samueleffiongjacob/alx-system_engineering-devops/raw/master/0x0F-load_balancer/install_haproxy_safely && bash haproxy

```


