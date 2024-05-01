# Attack is the best defense

## Concepts: Network basics

- [What is a protocol](https://www.techtarget.com/searchnetworking/definition/protocol)

- [What is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)

- [What is TCP/IP](https://www.avast.com/c-what-is-tcp-ip#)

- [What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)

## Concepts:Docker

[What is Docker and why is it popular?](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)

## Resource

- [Network sniffing](https://www.lifewire.com/definition-of-sniffer-817996)
- [ARP spoofing](https://www.veracode.com/security/arp-spoofing)
- [Connect to SendGrid’s SMTP relay using telnet](https://docs.sendgrid.com/ui/account-and-settings/troubleshooting-delays-and-latency)
- [What is Docker and why is it popular?](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
- [Dictionary attack](https://en.wikipedia.org/wiki/Dictionary_attack)

man or help:

    tcpdump
    hydra
    telnet
    docker

## Tasks

- ARP spoofing and sniffing unencrypted traffic [spoofing](https://postlmg.cc/dZFTgZM5)

```sh
sylvain@ubuntu$ telnet smtp.sendgrid.net 587
Trying 167.89.121.145...
Connected to smtp.sendgrid.net.
Escape character is '^]'.
220 SG ESMTP service ready at ismtpd0013p1las1.sendgrid.net
EHLO ismtpd0013p1las1.sendgrid.net
250-smtp.sendgrid.net
250-8BITMIME
250-PIPELINING
250-SIZE 31457280
250-STARTTLS
250-AUTH PLAIN LOGIN
250 AUTH=PLAIN LOGIN
auth login           
334 VXNlcm5hbWU6
VGhpcyBpcyBteSBsb2dpbg==
334 UGFzc3dvcmQ6
WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA==
235 Authentication successful
mail from: sylvain@kalache.fr
250 Sender address accepted
rcpt to: julien@google.com
250 Recipient address accepted
data
354 Continue
To: Julien
From: Sylvain
Subject: Hello from the insecure world

I am sending you this email from a Terminal.
.
250 Ok: queued as Aq1zhMM3QYeEprixUiFYNg
quit
221 See you later
Connection closed by foreign host.
sylvain@ubuntu$ 
```

```sh
# Run this when there is no other process running,
# ...tried to find a way to specifically filter the specif process but
# ...the best option was to run it in a virtual enviroment
# ...also base64 should be your best friend
sudo tcpdump -A -l
```

- [user\_authenticating\_into\_server](./user_authenticating_into_server) binary script file.

</details>

## summary

[Dictionary attack](./1-dictionary_attack)
[attack docker](https://ibb.co/Ltr6sZh)

- [Wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) **Rockyou.txt**

```sh
# command
hydra -V -s 2222 -l sylvain -P rockyou.txt 127.0.0.1 ssh -t 64
```

</details>
