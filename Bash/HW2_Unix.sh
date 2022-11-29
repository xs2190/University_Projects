#!/bin/bash
#NAME /S: Shelby Jordan
#CS 4350 - Unix System Programming
#Assignment Number: 2

_d=$1

get_UID(){
	local _uid="$(id -u)"
	echo "User ID is $_uid"
	case "$_uid" in
		501)
			printf "Current user is root.\n\n"
			;;
		*)
			printf "Current user is NOT root.\n\n"
			;;
	esac
}

getfile_count(){
	local f_count=0
	local t_count=0
	local d_count=0
	for item in *; do
		if [[ $item == *.txt ]]; then
			t_count=$((t_count+1))
			f_count=$((f_count+1))
		elif [ -f "$item" ]; then
			f_count=$((f_count+1))
		else
			d_count=$((d_count+1))
		fi
	done
	printf "Number of files in $_d: $f_count
Number of directories in $_d: $d_count
Number of .txt files in $_d: $t_count\n"
}

getempty_dir(){
	for dir in */; do
		local num_items=0
		next_dir="${_d}/${dir}"
		cd $next_dir
		for item in *; do
			if ! [[ $item =~ [''*''] ]];then
				num_items=$((num_items+1))
			fi
		done
		if [ "$num_items" -eq "0" ]; then
			echo "$dir" >> $HOME/empty_dir_list.out
		fi
	done
	if [ -f $HOME/empty_dir_list.out ];then
		printf "\nThe contents of empty_dir_list.out is... \n"
		eval cat $HOME/empty_dir_list.out
		printf "\n\n**** FYI: empty_dir_list.out is in the $HOME directory.***\n"
	else printf "\nNo empty directories found in $_d\n"
	fi
}

eval_pswd(){
	if [ ${#_d} -ge 8 ] && [[ "$_d" =~ [0-9] ]] && [[ "$_d" =~ [a-z] ]] && [[ "$_d" =~ [A-Z] ]]; then
	printf "\n<Non-weak Password>\n\n"
	else printf "\n<Weak Password>\n\n"
	fi	
}

reverse(){
	local cpy=${_d}
	local len=${#_d}
	local str_rev=""
	for((i=$len-1;i>=0;i--)); do
		str_rev+="${cpy:$i:1}"
	done
	echo "$_d reversed is $str_rev"
}

if [ -d "$_d" ]; then
	cd $_d
	get_UID
	getfile_count
	getempty_dir
	eval_pswd
	reverse
else
	echo "Error: INVALID DIRECTORY ~~~ try again"
fi
exit 0
