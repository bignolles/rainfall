#!/bin/sh

pass=`cat ./.key | grep user_pass | sed 's/user_pass: //' | tr -d "\n"`
echo "$pass" | pbcopy
