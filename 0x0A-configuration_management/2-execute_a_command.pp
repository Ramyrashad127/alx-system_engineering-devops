# last one
exec {'kill_killmenow':
command     => '/usr/bin/pkill killmenow',
refreshonly => true,
provider => 'shell',
}
