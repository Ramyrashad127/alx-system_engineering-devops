# pip3
package{'flask':
ensure   => '2.1.0',
provider => 'pip3',
path     => ['/usr/bin'],
command  => '/usr/bin/python3 /usr/bin/ run',
}
