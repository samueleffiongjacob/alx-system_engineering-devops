# Shell Process and signals

## Learning objectives

- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Concepts

- ps
- pgrep
- pkill
- kill
- exit
- trap

### Resource for the project that would help


[PID definition](https://www.linfo.org/pid.html)


[Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)

[Linux signal](https://www.educative.io/answers/what-are-linux-signals)

[Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)

[shell check](https://github.com/koalaman/shellcheck/wiki/Ignore)

[Linux signals](https://www.computerhope.com/unix/signals.htm)

[man sudo ](https://linux.die.net/man/8/sudo)

[&: BashItOut](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)

[init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)

[Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)

[Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

[What is a zombie Process](https://zombieprocess.wordpress.com/what-is-a-zombie-process/)

#### running zombie process in c
- gcc 102-zombie.c -0 zombie
- ps aux | grep -e 'Z+.*<defunct>' ===> teminal 2