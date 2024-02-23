# last one
exec {'pkill':
command => 'pkill killmenow',
provider => 'shell',
}
