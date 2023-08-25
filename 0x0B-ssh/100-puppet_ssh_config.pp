# Puppet manifest to configure SSH client for passwordless authentication
# Configure SSH client to use the private key ~/.ssh/school

include stdlib

file_line { 'SSH Private Key Configuration':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# Regex match explanation for IdentityFile:
# ^       beginning of the line
# [#]*    at least one hash character
# [\s]*   zero or more white space characters
# (?i)    case insensitive "IdentityFile"
# [\s]+   at least one whitespace character
# ~/.ssh/id_rsa The ssh private key file path we want to replace
# $       end of the line

# Configure SSH client to deny password authentication

file_line { 'Deny Password Authentication':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

# Regex match explanation for PasswordAuthentication:
# ^       beginning of the line
# [#]*    at least one hash character
# [\s]*   zero or more white space characters
# (?i)    case insensitive "PasswordAuthentication"
# [\s]+   at least one whitespace character
# (yes|no) with the value "yes" or the value "no"
# $       end of the line
