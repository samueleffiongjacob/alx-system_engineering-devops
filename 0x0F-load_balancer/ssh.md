# 1. Generate a New RSA SSH Key Pair

Open your terminal and run the following command:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/id_rsa_webserver
```

- `-t rsa`: Specifies the RSA algorithm.
- `-b 4096`: Specifies a key length of 4096 bits for strong security.
- `-C "your_email@example.com"`: Adds a comment with your email.
- `-f ~/.ssh/id_rsa_webserver`: Specifies the filename for the private key. The public key will be saved as `id_rsa_webserver.pub`.

**Example Output:**

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa_webserver): [Press Enter]
Enter passphrase (empty for no passphrase): [Type passphrase or press Enter]
Enter same passphrase again: [Type passphrase again or press Enter]
Your identification has been saved in /home/username/.ssh/id_rsa_webserver.
Your public key has been saved in /home/username/.ssh/id_rsa_webserver.pub.
The key fingerprint is:
SHA256:exampleFingerprint your_email@example.com
The key's randomart image is:
+---[RSA 4096]----+
| ...             |
| ...             |
| ...             |
+----[SHA256]-----+
```

## 2. Add the SSH Key to the SSH Agent

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Output might look like:

```bash
Agent pid 1234
```

Add your new SSH key to the agent:

```bash
ssh-add ~/.ssh/id_rsa_webserver
```

**Example Output:**

```bash
Identity added: /home/username/.ssh/id_rsa_webserver (your_email@example.com)
```

### 3. Copy the SSH Public Key

Display the public key:

```bash
cat ~/.ssh/id_rsa_webserver.pub
```

**Example Output:**

```bash
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr7E... your_email@example.com
```

Copy this entire output to your clipboard.

### 4. Add the SSH Key to the Web Server

Log in to your web server. If you’re already logged in via another method, open the `authorized_keys` file:

```bash
vi ~/.ssh/authorized_keys
```

Paste the public key into this file. Save and exit the editor (`Ctrl+X`, then `Y`, then `Enter` for `nano`).

### 5. Configure SSH to Use the New Key

Create or modify your SSH configuration file (`~/.ssh/config`) on your local machine:

```bash
vi ~/.ssh/config
```

Add the following:

```plaintext
Host webserver
    HostName your.webserver.address
    User your_username
    IdentityFile ~/.ssh/id_rsa_webserver
```

Replace `your.webserver.address` with your web server’s address and `your_username` with your username on the web server.

**Example Configuration:**

```plaintext
Host mywebserver
    HostName 192.168.1.100
    User ubuntu
    IdentityFile ~/.ssh/id_rsa_webserver
```

### 6. Test the New SSH Key

Connect to your web server using the new configuration:

```bash
ssh mywebserver
```

**Expected Output:**

```bash
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-135-generic x86_64)
...
```

This confirms that the new SSH key is correctly set up and used for connecting to your web server.

Let me know if you need any more details or further help!
