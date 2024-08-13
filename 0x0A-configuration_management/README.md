# Configuration management

![configuration_management](https://wac-cdn.atlassian.com/dam/jcr:f4635478-48a1-45d1-9b2f-43d14b2666ba/Configuration-management-tools-2x.png?cdnVersion=690)

> Configuration management is a systems engineering process for establishing consistency of a product’s attributes throughout its life.

Puppet is a tool that helps you manage and automate the configuration of servers. When you use Puppet, you define the desired state of the systems in your infrastructure that you want to manage.

![puppet](https://miro.medium.com/max/720/1*j0RHN3oXzOfXWl7XeLzxZw.webp)

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

## Project Requirements

- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A __README.md__ file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint version 2.1.1` without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line __must be a comment__ explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension __.pp__

## Installing puppet and puppet-lint on ubuntu

### Commands on Terminal

```bash

$ apt-get update && upgrade -y

$ sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades

$ sudo apt-get install -y ruby-augeas

$ sudo apt-get install -y ruby-shadow

$ sudo apt-get install -y puppet

#installs puppet linter
$ gem install puppet-lint
```

Follow the above instructions to install puppet and puppet-linter then watch the video to enable you understand how to get started with the task

## my RESOURCE for easy acesss

[configations intro](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)

[puppet docs](https://www.puppet.com/docs/puppet/5.5/types/file.html)

[puppet blog](https://www.puppet.com/blog)

[puppet lint](http://puppet-lint.com/)

[emac puupet](https://github.com/voxpupuli/puppet-mode)

[puppet old](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)

[puppet new](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)

### Excuting task

```bash
# first thing check version
$ puppet-lint --version

# create a file 
$  puppet-lint 0-create_a_file.pp

# appy my change
$  puppet apply 0-create_a_file.pp

# confirm file path
$ ls -l /tmp/school

# view what in the path
$ cat /tmp/school

# apply file second config
$ puppet apply 1-install_a_package.pp

# verify installation
$ flask --version

# if error Check Installed Versions: First, verify the versions of Flask and Werkzeug that are installed:

$ pip3 show flask werkzeug


# Reinstall Flask and Werkzeug: To make sure there are no leftover issues, you can force reinstall both packages. eg :

$ pip3 install --force-reinstall Flask==2.1.0 Werkzeug==2.0.3

# re apply build
# check version

# kill running terminal
# with a bash command and puppet .this process require 2 terminall.. 
# first terminal your bash command and second terminal your puppet command

$ ./killmenow
$ puppet apply 2-execute_a_command.pp
```
