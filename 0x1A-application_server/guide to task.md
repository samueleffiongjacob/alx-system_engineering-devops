# RESOURCE

[NGINX docs :  Nginx Reverse Proxy.](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#)
[Understanding nginx location blocks and rewrite rules](https://blog.pixelastic.com/2013/09/27/understanding-nginx-location-blocks-rewrite-rules/)
[digital ocean](https://blog.pixelastic.com/2013/09/27/understanding-nginx-location-blocks-rewrite-rules/)

## task 2

Step 1: Create a New Nginx Configuration File
Create a new configuration file specifically for the /airbnb-onepage/ route under /etc/nginx/sites-available/. Let's call it airbnb-onepage.

```bash
# command
$ sudo vi /etc/nginx/sites-available/airbnb-onepage
```

Step 2: Add the Configuration
Add the following configuration to the airbnb-onepage file:

```bash
#  Default Site Configuration 
$ sudo vi /etc/nginx/sites-available/default

server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    server_name localhost;  # This server will handle requests to 'localhost' or the server's IP
    add_header X-Served-By $HOSTNAME;

    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}

# save above

# Custom Configuration for /airbnb-onepage/

$ sudo vi /etc/nginx/sites-available/airbnb-onepage

# Nginx configuration for serving /airbnb-onepage/ and proxying to port 5000
server {
    listen 80;
    listen [::]:80;

    server_name 127.0.0.1 3.85.141.200;  # Replace with your actual domain or IP

    add_header X-Served-By $HOSTNAME;

    location /airbnb-onepage/ {
        proxy_pass http://localhost:5000/airbnb-onepage/;
        include proxy_params;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}

#  Nginx Main Configuration 
$ sudo vi /etc/nginx/nginx.conf

user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 768;
}

http {
    # Basic Settings
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    default_type application/octet-stream;

    # Adjust proxy headers hash size
    proxy_headers_hash_max_size 512; # feature 1024
    proxy_headers_hash_bucket_size 128; # before default value 64
    # server_name_in_redirect off;

    # SSL Settings (optional, if needed)
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    # Logging Settings
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    # Gzip Settings
    gzip on;
    gzip_disable "msie6";

    # Virtual Host Configurations
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-available/*;

    # Add header to identify the web server instance
    add_header X-Served-By "139694-web-01";
}



```

Step 3: Enable the Configuration
Create a symbolic link to enable the configuration:

```bash
# command
$ sudo ln -s /etc/nginx/sites-available/airbnb-onepage /etc/nginx/sites-enabled/
```

Step 4: Test the Configuration
Test the Nginx configuration for syntax errors:

```bash
# comand
$ sudo nginx -t

# You will probably need to reboot your server (by using the command $ sudo reboot) to have Nginx publicly accessible
$ sudo reboot
```

Step 5: Restart Nginx
If the test is successful, restart Nginx to apply the changes:

```bash
# command
$ sudo systemctl restart nginx
```

Check Logs: If there are any issues or if you want to confirm everything is working properly, check the Nginx logs:

```bash
# comand

$ sudo tail -f /var/log/nginx/access.log
$ sudo tail -f /var/log/nginx/error.log

```

kill instance runnin

```bash
# view what is there command
$  sudo lsof -i :<pid>

# kill command
$ sudo kill -9 <pid>
```

## test the above

```bash

# terminal 1 
$  gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

# terminal 2  curl 127.0.0.1/airbnb-onepage/

# On my local terminal:
$ curl -sI 3.85.141.200 /airbnb-onepage/

erver {
    listen 80;
    listen [::]:80;

    server_name 127.0.0.1 3.85.141.200;  # Replace with your actual domain or IP

    add_header X-Served-By $HOSTNAME;

    location /airbnb-onepage/ {
        proxy_pass http://localhost:5000/airbnb-onepage/;
        include proxy_params;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /airbnb-dynamic/number_odd_or_even/ {
        rewrite /airbnb-dynamic/(.*) $1 break;
        include proxy_params;
    proxy_pass http://localhost:5001/number_odd_or_even;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}

# TEST ABOVE
# TERMINAL 1
$ ubuntu@139694-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
$ ubuntu@139694-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
$ ubuntu@139694-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
$ ubuntu@139694-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
$ ubuntu@139694-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@139694-web-01:~/AirBnB_clone_v2$
$ 
$ ubuntu@139694-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
# 
$ samueleffiong@SAMUELEFFIONG:~/Desktop$ curl 3.85.141.200/airbnb-dynamic/number_odd_or_even/899
```

## task 4

```bash
# run query
$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -
$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db  # password: 
$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p # password: hbnb_test_pwd
$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
# command 
$ pip install flask
$ pip install Flask-CORS
$ pip install SQLAlchemy
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
$ sudo apt-get update
$ sudo apt-get install pkg-config

$ pip3 install mysqlclient
$ python3 -c "import MySQLdb" # if no output or error installation succeful



# task 1 : Never fail!
$ python3 -m unittest discover tests 2>&1 | tail -1
$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1

# task 2 :  Improve storage
# let add dummy state 
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./add_states.py

# now Let's do this for your API task 4
$  tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
$  curl 127.0.0.1:5002/api/v1/states
#Local Terminal:
$  curl 3.85.141.200/api/v1/states
# on browser
$ http://3.85.141.200/api/v1/states
```
