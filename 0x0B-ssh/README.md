# 0X0B-SSH

![ssh_connection](https://www.ipxo.com/app/uploads/2022/02/What-is-SSH-820x460.jpg)

A __Secure Shell__, or __Secure Socket Shell__, is a network protocol that allows devices to achieve two important things: communicate and share data. Additionally, the SSH protocol also encrypts data, making it ideal for unsecured networks.

## Learning Objectives

- What is a __server__
- Where servers usually live
- What is `SSH`
- How to create an `SSH RSA` key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## REsource

[what is a server](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)

[server](https://www.youtube.com/watch?v=B1ANfsDyjeA)

[ssh](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)

[ssh config](https://www.ssh.com/academy/ssh/config)

[ssh pub keys](https://www.ssh.com/academy/ssh/public-key-authentication)

[ssh video](https://www.youtube.com/watch?v=ORcvSkgdA58)

[ssh server](https://www.youtube.com/watch?v=hQWRp-FdTpc)

[ssh encyption](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)

[sh](https://en.wikipedia.org/wiki/Secure_Shell)

[ietf](https://www.ietf.org/rfc/rfc4251.txt)

[internet engineering task force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)

[ssh comments](https://en.wikipedia.org/wiki/Request_for_Comments)

Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password

## adding a user to a server

```bash
# run the below command
$ echo "ssh pub key here" >> ~/.ssh/authorized_keys
```
