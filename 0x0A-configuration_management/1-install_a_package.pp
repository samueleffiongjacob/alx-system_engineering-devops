# A puppet manifest installing flask v2.1.0 which is a package from pip3.
# Am also specifying the version of flask to install using the ensure attribute
# flask -- version to check version of python and flask install
# check the read me file under resource to see what ensure, provider means in puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
