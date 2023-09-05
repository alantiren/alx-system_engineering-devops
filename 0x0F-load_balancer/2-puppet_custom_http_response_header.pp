# Define a custom Nginx configuration for the X-Served-By header
file { '/etc/nginx/sites-available/custom_header':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  content => "# Custom Nginx configuration for X-Served-By header\n\
              server {\n\
                  listen 80 default_server;\n\
                  server_name _;\n\
                  location / {\n\
                      add_header X-Served-By $hostname;\n\
                      # Other configurations...\n\
                  }\n\
              }\n",
}

# Create a symbolic link to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom_header',
}

# Reload Nginx to apply the custom configuration
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-enabled/custom_header'],
}
