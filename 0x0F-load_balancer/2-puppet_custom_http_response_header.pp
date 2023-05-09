# Setup New Ubuntu server with nginx
# and add a custom HTTP header

# update ubuntu server
exec { 'update system':
        command => '/usr/bin/apt-get update',
        user    => 'root',
        provider=>  'shell'
}
# install nginx web server on server
-> package { 'nginx':
  ensure => 'installed',
  require => Exec['update system']
}
# or use 
# package { 'nginx':
#   ensure   => present,
#   provider => 'apt'
# }

# custom Nginx response header (X-Served-By: hostname)
-> file_line { 'http_header':
  ensure => 'present',
  path  => '/etc/nginx/nginx.conf',
  after  => 'listen 80 default_server;',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# or

# file_line { 'add HTTP header':
#   ensure => 'present',
#   path   => '/etc/nginx/sites-available/default',
#   after  => 'listen 80 default_server;',
#   line   => 'add_header X-Served-By $hostname;'
# }

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# start service
# service {'nginx':
# 	ensure => running,
# 	require => Package['nginx']
# }
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}

# service { 'nginx':
#   ensure  => 'running',
#   enable  => true,
#   require => Package['nginx']
# }
