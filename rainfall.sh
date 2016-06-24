#!/bin/sh

export KEY_PATH="$HOME/projects/rainfall/.key"
export VM_PATH="$HOME/projects/rainfall/.rainfall_ip"

updateUser() {
	if [ ! -z "$1" ] && [ ! -z "$2" ]
	then
		printf "user_id: %s\nuser_pass: %s\n" $1 $2 > "$KEY_PATH"
	else
		printf "updating user impossible : missing information!\n" 1>&2
	fi
}

updateVm() {
	if [ ! -z "$1" ] && [ ! -z "$2" ]
	then
		printf "vm_ip: %s\nvm_port: %s\n" $1 $2 > "$VM_PATH"
	else
		printf "updating vm impossible : missing information!\n" 1>&2
	fi
}

if [ $# -ge 3 ]
then
	argsArray=( "$@" )
	for i in `seq ${#argsArray[@]}`
	do
		elem=${argsArray[i - 1]}
		if [ "$elem" == "--update-user" ]
		then
			updateUser ${argsArray[i]} ${argsArray[i + 1]}
		elif [ "$elem" == "--update-vm" ]
		then
			updateVm ${argsArray[i]} ${argsArray[i + 1]}
		fi
	done
fi

vm_ip=`cat ./.rainfall_ip | grep vm_ip | sed 's/vm_ip: //' | tr -d "\n"`
vm_port=`cat ./.rainfall_ip | grep vm_port | sed 's/vm_port: //' | tr -d "\n"`
user_id=`cat ./.key | grep user_id | sed 's/user_id: //' | tr -d "\n"`
user_pass=`cat ./.key | grep user_pass | sed 's/user_pass: //' | tr -d "\n"`

echo "$user_pass" | pbcopy
ssh $user_id@$vm_ip -p $vm_port