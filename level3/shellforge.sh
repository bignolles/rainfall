#!/bin/sh

if [ ! -z "$1" ]
then
	objName=`echo "$1" | sed 's/\.s/.o/'`
	binName=`echo "$1" | sed 's/\.s/.bin/'`
	execName=`echo "$1" | sed 's/\.s//'`
	as -o $objName $1 && ld --oformat binary -o $binName $objName
	as -o $objName $1 && ld -o $execName $objName
	hexdump $binName\
	| sed 's/[0-9a-f]\{7,8\} \?//'\
	| xargs\
	| sed 's/\([0-9a-f]\{2\}\)\([0-9a-f]\{2\}\)/\\x\2\\x\1/g'\
	| tr -d " "
fi
