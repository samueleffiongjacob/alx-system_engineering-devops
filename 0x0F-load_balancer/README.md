# Load balancer

![load_balancer](https://miro.medium.com/max/720/0*CCK15OF3DizmOITk)

> Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Concepts

- HTTP Header
- Debian/UbuntuHAProxy Packages
- Introduction to Load Balancing.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A __README.md__ file, at the root of the folder of the project, is mandatory
- All your Bash script files __must be executable__
- Your Bash script must pass `Shellcheck (version 0.3.7)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing.

## Installing HAProxy and configuring HAProxy

```bash

$ sudo apt-get install -y haproxy=1.6.\*

$ sudo vi /etc/haproxy/haproxy.cfg
# Add the below code to the file opened using vi editor
frontend effiongsamuel.tech
        bind 0:80
 mode http
        default_backend web_servers

backend web_servers
        balance roundrobin
        server 139694-web-01 3.85.141.200:80 check
        server 139694-web-02 54.236.190.52:80 check
~
~
:wq(to save and exit)
--------------- or ----------------------- 
$ echo '
frontend effiongsamuel.tech
        bind 0:80
 mode http
        default_backend web_servers

backend web_servers
        balance roundrobin
        server 139694-web-01 3.85.141.200:80 check
        server 139694-web-02 54.236.190.52:80 check
' >> /etc/haproxy/haproxy.cfg

$ service haproxy restart

# git clone this repo on your terminal and run the file
# install_haproxy_safely or 1-install_load_balancer to 
# configure yours on a fly.
```

## resource

[haproxy](https://www.techtarget.com/searchnetworking/definition/HAProxy)
[haproxy docs](https://www.haproxy.com/documentation/haproxy-configuration-manual/latest/)
[digital ocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
