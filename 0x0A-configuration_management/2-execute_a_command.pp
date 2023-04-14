# A manifest to kill a running process killmenow from the process table
# check the read me file under resource to see what command, path,onlyif,provider  means in puppet
# on every puppet run

exec { 'killing a process using pkill':
  command  => 'pkill -9 killmenow',
  path     => '/usr/bin:/bin',
  onlyif   => 'pgrep killmenow',
  provider => shell,

}
