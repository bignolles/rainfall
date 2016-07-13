# RAINFALL

## Introduction
You will find in this repository the complete solution to the project Rainfall.
Once the VM provided with this project installed, you should be able to log in through ssh as user `level0`

```bash
$ ssh level0@localhost -p 4242
	  _____       _       ______    _ _
	 |  __ \     (_)     |  ____|  | | |
	 | |__) |__ _ _ _ __ | |__ __ _| | |
	 |  _  /  _` | | '_ \|  __/ _` | | |
	 | | \ \ (_| | | | | | | | (_| | | |
	 |_|  \_\__,_|_|_| |_|_|  \__,_|_|_|

                 Good luck & Have fun

  To start, ssh with level0/level0 on 10.0.2.15:4242
level0@localhost's password:
```
<br />

Once logged in, your goal is to obtain the password of user `levelX`, *X* being the number of the next level.
You'll find this password stored in the file `.pass` in the next user's home directory.

```bash
level0@RainFall:~$ ./level0 $(exploit)
$ cat /home/user/level1/.pass
?????????????????????
$ exit
level0@RainFall:~$ su level1
Password:
level1@RainFall:~$ _
```
<br />

## Repository organization

In evey *levelX* directory, you will find a `flag` file, containing the flag you have to obtain while being logged as *levelX*.
You will also find a `source` file, containing **metacode** that I have reverse-engineered from the executable
```bash
$ ls -l ./level1
total 10
-rw-r--r--  1 marene  2013_paris    65 Jul  6 17:03 flag
drwxr-xr-x  2 marene  2013_paris  4096 Jul  6 17:01 ressource
-rw-r--r--  1 marene  2013_paris    80 Jul  6 13:40 source.c
```

<br />

In some of the directories, you might also find a `ressource` sub-directory.
It will contain all the scripts and files needed to realize the exploit.

```bash
$ ls -l ./level1/ressource
total 3
-rwxr-xr-x  1 marene  2013_paris  391 Jul  6 17:01 run.py
-rwxr-xr-x  1 marene  2013_paris  201 Jul  6 17:01 shellcode.s
-rwxr-xr-x  1 marene  2013_paris  384 Jul  6 17:01 shellforge.sh
```

## rainfall.sh
rainfall.sh is a basic utility script that helps you keep track of your current level and password to access this level.
All passwords are stored into their appropriate user directory in the file `.pass`
The VM informations (IP and port) are stored in `./.rainfall\_ip`
The current user informations are stored in ./.key
just launch `./rainfall.sh` to log through ssh as the current registered user. The password will be copied into your clipboard

```bash
$ ls -l ./level01/.pass
-rw-r--r--  1 marene  2013_paris  26 Jul 13 11:32 ./level01/.pass

$ ls -la ./.rainfall_ip
-rw-r--r--  1 marene  2013_paris  31 Jul 13 11:29 ./.rainfall_ip

$ ls -la ./.key
-rw-r--r--  1 marene  2013_paris  33 Jul 13 13:37 ./.key
```
### Options
 - `--update-user levelXX` : If `levelYY` exists (*ie* if the directory `levelXX` exists and contains a `.pass` file), change the current user to `levelYY` and logs you as it
 - `--update-vm ip port` : Changes the registered ip and port for the rainfall vm
 - `--add-user levelXX password` : If `levelXX` doesn't already exists, create a `levelXX` directory and write the provided password in `levelXX/.pass`
 - `--whoami` : Shows which user is currently registered
 - `--whatvm` : Shows current VM's port and IP
 - `--no-connect` : Prompts the ssh command line used to connect, but does not actually try to log in


### Notice
[ ] add a link for VM download 
