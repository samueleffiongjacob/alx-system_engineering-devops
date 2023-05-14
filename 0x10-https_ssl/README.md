# 0x10. HTTPS SSL 

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png"/>
</p>

## Resource

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)

- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)

-[HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/)

- [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)

- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)

- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

- [How to Secure HAProxy with Let's Encrypt on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04)

- [HAProxy SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination/)

man (awk, dig)
## Tasks

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
# directory. To view them do the below
$ ls /etc/letsencrypt/live/domain_name/

# Now concat your certificate .pem files to a single pem file and save them to
# /etc/ssl/private
$ cat cert_key_1 cert_key_2 > /etc/ssl/private/any_desired_name.pem

# Now go to your haproxy config file to add a the path to your certificate
# Then reload haproxy
$ sudo service haproxy reload
```
_If you don't have HAProxy installed just copy and run this on your terminal and save yourself the hassle_

```
$ wget -O haproxy https://github.com/samueleffiongjacob/alx-system_engineering-devops/raw/master/0x0F-load_balancer/install_haproxy_safely && bash haproxy

```


![haproxy configuration](https://www.ssllabs.com/ssltest/)

![haproxy configuraton](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)

![User Guide documentation certbot](https://eff-certbot.readthedocs.io/en/stable/using.html#changing-a-certificate-s-key-type)


![certbot ssl generator official site](https://certbot.eff.org/)
![certbot instructions FOR haproxy in ubuntu --versions](https://certbot.eff.org/instructions?ws=haproxy&os=ubuntufocal)

![DEV GUIDE FOR Setting up SSL Certificates for HAProxy with certbot](https://dev.to/phansch/setting-up-ssl-certificates-for-haproxy-with-certbot-bb0)


![Skarlso's guide for Haproxy](https://skarlso.github.io/2017/02/15/how-to-https-with-hugo-letsencrypt-haproxy/)