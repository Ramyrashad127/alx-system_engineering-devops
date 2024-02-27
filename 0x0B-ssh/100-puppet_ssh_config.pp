#work with keys
file_line{'turn off pass':
line => '    PasswordAuthentication no',
path => '/etc/ssh/ssh_config',
ensure => 'present',
}

file_line {'turn on keys':
line   => '    IdentityFile ~/.ssh/school',
path   => '/etc/ssh/ssh_config',
ensure => 'present',
}
