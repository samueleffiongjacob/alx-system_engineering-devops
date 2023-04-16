# 0x0D Web stack debugging #0 :wrench:

> Debugging is the process of finding and fixing errors in software that prevents it from running correctly. As you become a more advanced programmer and an industry engineer, you will learn how to use debugging tools such as gdb or built-in tools that IDEs have. However, it’s important to understand the concepts and processes of debugging manually. This project covers the optimal framework and blueprint for debugging web stack (remote containers this scenario) bugs

Challenge:

Get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it. After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains Hello Holberton. Paste the command(s) you used to fix the issue in your answer file.
Here we can see that after starting my Docker container, I curl the port 8080 mapped to the Docker container port 80, it does not return a page but an error message. Note that you might also get the error message curl: (52) Empty reply from server.


## Tasks :heavy_check_mark:

0. Bash script that once executed, will bring the webstack to a working state.


## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [0-give_me_a_page](./0-give_me_a_page)|

## Additional info :construction: and resource for reading

network basics -> [Read me](https://intranet.alxswe.com/concepts/33)
i) what is a protocol -> [read me](https://www.techtarget.com/searchnetworking/definition/protocol)

ii) what is an ip address -> (https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)

iii) what is TCP/ip -> [read me](https://www.avast.com/c-what-is-tcp-ip#)

iv)what is internet protocol ip [read me](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
Docker -> [Read me](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)

what is docker and why it is popular -> [read me ](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
notting here -> [Read me](https://intranet.alxswe.com/concepts/65)
notting here -> [Read me](https://intranet.alxswe.com/concepts/68)


web debugging -> [Read me](https://intranet.alxswe.com/concepts/68)

Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

Is the web server started? - You can check using the service manager, also double check by checking process list.
On what port should it listen? - Check your web server configuration
Is it actually listening on this port? - *netstat -lpdn*- *run* as *root or sudo* so that you can see the process for each listening port
It is listening on the correct server IP? - *netstat* is also your friend here
Is there a firewall enabled?
Have you looked at logs? - usually in */var/log and tail -f* is your friend
Can I connect to the HTTP port from the location I am browsing from? - *curl* is your friend
There is a good chance that at this point you will already have found part of the issue.

##Get a quick overview of the machine state
*w*:
shows server uptime which is the time during which the server has been continuously running
shows which users are connected to the server
load average will give you a good sense of the server health - (read more about load here and here)
*history* :
shows which commands were previously run by the user you are currently connected to
you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
where you might want to start your debugging work
*top*:
shows what is currently running on this server
order results by CPU, memory utilization and catch the ones that are resource intensive
*df* :
shows disk utilization
*netstat*:
what port and IP your server is listening on
what processes are using sockets
try *netstat -lpn* on a Ubuntu machine

## Machine
Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:

Does the server have free disk space? - *df*
Is the server able to keep up with CPU load? - *w, top, ps*
Does the server have available memory? *free*
Are the server disk(s) able to keep up with read/write IO? - *htop*


## Network issue
For the machine level, you want to ask yourself these questions:

Does the server have the expected network interfaces and IPs up and running? *ifconfig*
Does the server listen on the sockets that it is supposed to? *netstat (netstat -lpd or netstat -lpn)*

Can you connect from the location you want to connect from, to the socket you want to connect to? *telnet* to the IP + PORT (*telnet 8.8.8.8 80*)

Does the server have the correct firewall rules? *iptables, ufw*:
*iptables -L
sudo ufw status*

## Process issue
If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).

Is the software started? *init, init.d*:
8service NAME_OF_THE_SERVICE status*

*/etc/init.d/NAME_OF_THE_SERVICE status*
Is the software process running? *pgrep, ps*:
*pgrep -lf NAME_OF_THE_PROCESS*
*ps auxf*

Is there anything interesting in the logs? look for log files in */var/log/ and tail -f* is your friend

## how to install Docker
mac Os [read me](https://docs.docker.com/desktop/install/mac-install/)

windows [read me ](https://docs.docker.com/desktop/install/windows-install/)

How to Install Docker on Ubuntu 14.04 LTS[read me](https://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/)

How To Install and Use Docker on Ubuntu 16.04[read me](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

## man or help
curl

Apache Http server [read me](https://en.wikipedia.org/wiki/Apache_HTTP_Server)
### Resources

- emacs
- BASH
- Debian 9 stable / Ubuntu 16.04 / Ubuntu 18.04 
- Shellcheck
- Puppet 3.8
- Puppet-lint 2.1.1
- Docker

<!
### Try It On Your Machine :computer:
```bash
git clone https://github.com/samueleffiongjacob/alx-system_engineering-devops.git
cd 0x0D-web_stack_debugging_0
cat FILENAME
docker run -p 8080:80 -d -it CONTAINER_ID
curl 0:8080
MUST SHOW REPLY FROM SERVER

```
-->

```bash
# i realized that installing apache2 on my machine doesn't automatically starts
# apache as in the case of nginx. as such i neede to start the apache web server
# which actually gave me the expected results as apache is configured to listen
# to port 80 by default.


$ service apache2 start

$ curl localhost

```
