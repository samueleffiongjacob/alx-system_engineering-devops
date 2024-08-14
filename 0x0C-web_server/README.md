# 0X0C - Web Server

![](https://www.keil.com/pack/doc/mw/Network/html/http_server_block_diagram.png)

Web servers consist of hardware and software that use Hypertext Transfer Protocol (HTTP) to respond to web users’ requests made via the World Wide Web.

__NOTE__: In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention).

## what is a Child Process?

 Although it may sound like something out of a parenting handbook or a psychological journal, the term child process actually has nothing to do with human development. If you run a Unix or Linux dedicated server, you have likely encountered child processes without even knowing it. Therefore, it is good to know what child processes are and how they work.

 A child process is a process created by another process. The creator process is properly called the “parent process”. The benefit of a child process is that it can start or stop at will without affecting the parent process. The child process is, however, is typically dependent on the parent process. If the parent process dies, the child process becomes an orphan process.

 In normal server operations, the kernel may initiate child processes, and other programs, such as Apache, may have them as well. Apache creates child processes (or children, if you prefer) whenever the number of requests (web page accesses from users) exceeds the maximum allowed number of requests. When the maximum number of child process requests is exceeded, another child process spawns.

 To view all running processes along with their child processes in a “tree” format, use the following command:

```bash
# chaild process
$ ps axf
```

## Learning Objectives

[A good software engineer is a lazy software engineer, crazy right](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb)

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

## My resource

[what is web serve](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb)

[Nginx](https://en.wikipedia.org/wiki/Nginx)

[how to configure ngix](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)

[http request](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)

[http redirect](https://moz.com/learn/seo/redirection)

[not found http response](https://en.wikipedia.org/wiki/HTTP_404)

[log file](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

[ref](https://datatracker.ietf.org/doc/html/rfc7231)

[ref1](https://datatracker.ietf.org/doc/html/rfc7540)

[intall ngix](https://askubuntu.com/questions/672892/what-does-y-mean-in-apt-get-y-install-command)

[replace varable with seed](effiongsamuel.tech)

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
  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;

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

```

ssh mywebserver
/home/ubuntu
ubuntu@139694-web-01:~$