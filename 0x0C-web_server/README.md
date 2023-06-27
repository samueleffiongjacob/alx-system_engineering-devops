# 0X0C - Web Server

![](https://www.keil.com/pack/doc/mw/Network/html/http_server_block_diagram.png)

Web servers consist of hardware and software that use Hypertext Transfer Protocol (HTTP) to respond to web users’ requests made via the World Wide Web.

__NOTE__: In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention).

## Learning Objectives

A good software engineer is a lazy software engineer, crazy right.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

__General Objectives__
	- what is the main role of a web server
	- What is a child process
	- Why web servers usually have a parent process and child processes
	- What are the main HTTP requests

__DNS__
	- What DNS stands for
	- What is DNS main role

__DNS Record Types__
	- `A Records`
	- `CNAME`
	- `TXT Records`
	- `MX Records`

- How the web works
- `Nginx`
- How to __Configure Nginx__
- Child process concept page
- __Root and sub domain__
- `HTTP` __requests__
- `HTTP` __redirection__
- Not found `HTTP` response code
- Logs files on Linux
- `HTTP/1.1` and `HTTP/2`
- `scp` and `curl`

## RESOURCE
what is child process on server -> [Read me](https://intranet.alxswe.com/concepts/110)

SRE -> [Read me](https://intranet.alxswe.com/rltoken/9I0WufjKdW3TZA2EVrGnlQ)


lazy software engineer -> [Read me](https://intranet.alxswe.com/rltoken/sRY__axKNHhNW0SVmsUC_A)

how the web works -> [Read me](https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw)

Ngnix but pronouce engine x -> [Read me](https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA)

how to configure Nginx -> [Read me](https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw)

child process concept  -> [Read me](https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg)

Root and sub domain -> [Read me](https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ)

HTTP requests -> [Read me](https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw)

Http redirection -> [Read me](https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ)

Not found HTTP response code -> [Read me](https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw)

logs files on linux -> [Read me](https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg)

RFC 7231(http/1.1) -> [Read me](https://intranet.alxswe.com/rltoken/BGa6RrS0dnM6EdBGS_ZDUw)

RFC 7540(http/2)-> [Read me](https://intranet.alxswe.com/rltoken/IZ2fyYn1qNZ9RXXsg5vG1g)

man or help on linux terminal
scp or curl


##Geting .TECH DONAINS.
.TECH Domains -> [first read more here](https://intranet.alxswe.com/rltoken/Hcb-pfK8UiDBfwsDJPyZZw) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your tools space [see here](https://intranet.alxswe.com/rltoken/CprZO4m1rUm5C6ZgvROpgg). Feel free to drop a thank you tweet for .TECH Domains -> [see here](https://intranet.alxswe.com/rltoken/y3_YCbJ5bGKgPYqP0LyVBA)

My Tools
GitHub Student Developer Pack
Learn to ship software like a pro

There's no substitute for hands-on experience. But for most students, real world tools can be cost-prohibitive.

That's why we created the GitHub Student Developer Pack with some of our partners and friends: to give students free access to the best developer tools in one place so they can learn by doing.

More information -> [More information](https://education.github.com/pack)

don't use this dam link is for porn alx[porn alx](https://education.github.com/student/verify?school_id=7806&student_id=ALX-139694&signature=f691fa09d618d4eee2a20c7eb28509f7a766bf98c4b944f1989e49fe5226c643)
## Requirements

__General__

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A `README.md file`, at the root of the folder of the project, is mandatory
- All your Bash script __files must be executable__
- Your Bash script must pass `Shellcheck (version 0.3.7)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use `systemctl` for restarting a process
- A prior knowledge to bash scripting

## Video Tutorial

For stsep by step guide on how to go about the installation and configuration, you can click the __"watch video"__ link to get started

- Proceed to video -> [Watch Video](#)

## useful resource

[ngix](https://docs.nginx.com/nginx/admin-guide/web-server/web-server/)
## Installing Needed Packages

```bash

$ sudo apt-get install shellcheck -y

# Check shellcheck version

$ shellcheck -V

# Installing nginx

$ sudo apt-get install nginx -y

```
## Configuring nginx
```bash

# Configuring the default file

$ sudo vi /etc/nginx/sites-available/default

# Once the vi editior opens

server {
  listen 80 default_Server;
  listen [::]:80 default_Server
  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;

# add a server headed to the the config
$ add_header X-Server-By 153318-web-01

# if you have a domain name replace '_' with it
  server_name _;

# configuring error_page
  error_page 404 404.html;

  location / {
	try_files $uri $uri/ =404;
  }

  location = /404.html {
	internal;
  }
}

# Alway confirm that your nginx configuration is valid, suceesful and tested.
$ sudo nginx -t

# To archieve a folder for backup
$ sudo tar -czf /tmp/web01.tar.gz /alx/home/ubuntu/etc/var/www/root

# backup server to avoid wonderful stories
$ scp ubuntu@<server_ip>: <path_to_file> <path_to_save_tranferred_file> -i <path_to_key>

# Usuage 

$ scp ubuntu@web01:/temp/webo1.tar.gz

# To view content of an archive file:

$ tar -tf webo1.tar.gz  # not web01.tar.gz is folder archive for backup

# To extract the content of afile for tar

$ tar -xf web01.tar.gz <path_to_file>
```
coupon for .tech domain once(Holb2023nmz07n)

how to creat ssh :ssh-keygen -t rsa