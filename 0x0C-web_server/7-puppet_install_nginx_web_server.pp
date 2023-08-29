# Puppet manifest to install and configure Nginx with 301 redirection

class nginx_web_server {
  package { 'nginx':
    ensure => installed,
  }

  file_line { 'redirect_config':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    after  => 'listen 80 default_server;',
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

class { 'nginx_web_server': }
