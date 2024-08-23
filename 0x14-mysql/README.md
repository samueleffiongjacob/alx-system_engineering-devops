# 0x14-mysql

![mysql](https://www.simplilearn.com/ice9/free_resources_article_thumb/difference_between_sql_and_mysql.jpg)

The MySQL server provides a database management system with querying and connectivity capabilities, as well as the ability to have excellent data structure and integration with many different platforms.

## Needed Knowledge

- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)

- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)

- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

- `mysqldump`

## Learning Objectives

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Project Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck __(version 0.3.7-5~ubuntu16.04.1 via apt-get)__ without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Installation Guide for mysql 5.7.*

- First go to site [dev.mysql.com](https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html) and copy the PGP PUBLIC KEY just immediately under the _Notice_ section to your clipboard.

- Create a new file in your terminal with a .key extension and paste the PGP PUB KEY copied to clipboard.
- Then do the following

```bash
$ sudo apt-key add name_of_file.key
OK

# adding it to the apt repo
$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.18-1_all.deb
$ sudo dpkg -i mysql-apt-config_0.8.18-1_all.deb


# updating the apt repo to add the url i added earlier
$ sudo apt-get update
$ sudo apt-get install mysql-client=5.7.* mysql-community-server=5.7.* mysql-server=5.7.*

# or 
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository 'deb http://repo.mysql.com/apt/ubuntu/ focal mysql-5.7'
$ sudo apt-get update
$ sudo apt-cache policy mysql-server
$ sudo apt-get install mysql-server=5.7.*

# now check your available versions
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.31-0ubuntu0.20.04.2
  Version table:
     8.0.31-0ubuntu0.20.04.2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
     8.0.31-0ubuntu0.20.04.1 500
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.40-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

# Now am installing mysql 5.7.*
$ sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y
```

## Project Task

### Creating a user and Granting Priviledges in mysql

```mysql
$ mysql -u root -p

Password: /* Type root password

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

mysql>  GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

mysql> FLUSH PRIVILEGES;
```

### now see if grant works

```bash
# command
$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
```

### Creating Database, Tables and adding Data to the Tables

```mysql

mysql> CREATE DATABASE db_name_;

-- To verify if db is created
mysql> SHOW DATABASES;

mysql> USE db_name;

mysql> CREATE TABLE table_name (
    -> col_1 data_type,
    -> col_2 data_type);
-- continue adding more coloums to your taste for me i just added two coloumns

mysql> INSERT INTO table_name VALUES (val_1, val_2); # INSERT INTO nexus6 (name, hire_date) VALUES ('John Doe', '2024-08-23');


-- Verify if data was added succesfully do
mysql> SELECT col_1, col_2 FROM tb_name;
```

``` GRant table privilage
GRANT ALL PRIVILEGES ON tyrell_corp.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```

### Setting Up MySQL Replication

- First create replication user and grant replication priviledge ( best practice).

```mysql

mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd'; # 

mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

mysql> FLUSH PRIVILEGES;

-- to verify
mysql> SELECT user, Repl_slave_priv FROM mysql.user;

mysql> exit
```

- Next up you go to the /etc/mysql/mysql.conf.d/mysqld.cnf and comment the bind address and then add this lines to it

```bash
# By default we only accept connections from localhost
# bind-address = 127.0.0.1
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name #tyrell_corp
```

- Then you enable incoming connection to port 3306 and restart mysql-server

```bash

sudo ufw allow from 'replica_server_ip' to any port 3306 # sudo ufw allow from 54.236.190.52 to any port 3306 So if your replica server's IP address is 192.168.1.100, the command would be:
 

sudo service mysql restart
```

- Now log back in to mysql-server to lock db and prepare binary file for replication.

```bash
$ mysql -uroot -p
password:
```

```mysql
mysql> 
mysql> SELECT USER();
+----------------+
| USER()         |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)

mysql> FLUSH TABLES WITH READ LOCK;

mysql> SHOW MASTER STATUS;

+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      149 | db           |                  |                   |
+------------------+----------+--------------+------------------+-------------------+

mysql> SHOW MASTER STATUS;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000004 |      154 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

```

_Take note of the binary log and the position, jot it down or you leave this window open and you open another window to continue_ .

- you then export the db from myql-server to local machine and then copy this db to replica machine

```bash
mysqldump -uroot -p tyrell_corp > export_db_name.sql

scp -i _idenetity_file_ export_db_name.sql user@machine_ip:location 
# or remote machine directly: 
scp ~/export_db_name.sql ubuntu@54.236.190.52:~/ #

 # moving made local:
 scp mywebserver2:~/export_db_name.sql /home/samueleffiong/Desktop/export_db_name.sql
```

- Then ssh to replica machine ip_adress to import this tables to replica mysql-server

```bash

$ mysql -uroot -p 
password:


mysql> CREATE DATABASE db_name; #tyrell_corp 

mysql>exit
bye

$ mysql -uroot -p db_name < export_db_name.sql # tyrell_corp

password:

# Now edit the config file in /etc/mysql/mysql.conf.d/mysqld.cnf and then reload mysql-server

```bash

server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name_from_master_mysql-server #tyrell_corp 
relay_log = /var/log/mysql/mysql-relay-bin.log

$ sudo service mysql restart
```

- Login to mysql server in replica to configure replication

```bash

$ mysql -uroot -p
password:


mysql>
```

```mysql

mysql> CHANGE MASTER TO
    -> MASTER_HOST='source_host_name',
    -> MASTER_USER='replication_user_name',
    -> MASTER_PASSWORD='replication_password',
    -> MASTER_LOG_FILE='recorded_log_file_name',
    -> MASTER_LOG_POS=recorded_log_position;

# eg
CHANGE MASTER TO
    MASTER_HOST='192.168.1.100',
    MASTER_USER='repl_user',
    MASTER_PASSWORD='securepassword',
    MASTER_LOG_FILE='mysql-bin.000001',
    MASTER_LOG_POS=154;


-- Then you start slave
mysql> START SLAVE;

-- check the status
mysql> show slave status\G
```

_That's it you've configured replication on mysql, do reach out for any further assistance_ .
