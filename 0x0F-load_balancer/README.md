# 0x0F. Load balancer

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png"/>
</p>

## Resource

<details>
<summary>Load balancer</summary><br>
<ul>
  <li>Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic? They don’t have just one server, but tens of thousands of them. In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

  <p align="center">
   <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/6cefdd14b2f8c36789cba132bd5a10d42d88a177.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220111T181845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=792a403303cb0d1faf98b4886f11e22013fa58b709f00d84029ac5877beb6aab" />
  </p>
  <ul>
      <li><a href="https://www.thegeekstuff.com/2016/01/load-balancer-intro/">Load-balancing</a></li>
      <li><a href="https://devcentral.f5.com/s/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms">Load-balancing algorithms</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary>Web stack debugging</summary><br>
<ul>
  <li>Intro
  <ul>Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.</ul>

  <p align="center">
   <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/45dffb0b1da8dc2ce47e340d7f88b05652c0f486.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220105T050302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d499fde872931932fc76dedd39b4298797482fd9b7ca1fc09f0a885ea8aa1cae" />
  </p>
  </li>
</ul>

<details>
<summary>Test and verify your assumptions</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/rFMtkCt8/image.png' border='0' alt='image'/></a>
</details>

<ul>
  <li>Debugging is fun
  <ul>Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck 😃</ul>

  <p align="center">
   <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bae58c9f066a9668001ef4b4c39778407439d2f9.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220105T050302Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67d4c1d736b92bef534ab94427ff3bef2c8ad4b498cafb512fbe6f6ddefec9ba" />
  </p>
  </li>
</ul>

</details>

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HAProxy Configuration Basics: Load Balance Your Servers](https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [HTTP Header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Tasks

<details>
<summary><a href="./0-custom_http_response_header">0. Double the number of webservers</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/prMGd5GF/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-install_load_balancer">1. Install your load balancer</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/4dBWZ476/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-puppet_custom_http_response_header.pp">2. Add a custom HTTP header with Puppet</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/sD2G5kZY/image.png' border='0' alt='image'/></a>
</details>

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
        server 139694-web-01 100.26.178.1:80
        server 139694-web-02 34.202.157.245:80
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
        server 139694-web-01 100.26.178.1:80
        server 139694-web-02 34.202.157.245:80
' >> /etc/haproxy/haproxy.cfg

$ service haproxy restart

# git clone this repo on your terminal and run the file
# install_haproxy_safely or 1-install_load_balancer to 
# configure yours on a fly.
```

