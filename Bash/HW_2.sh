#!/bin/sh

_d=$1

get_UID(){
	local _uid="$(id -u)"
	echo "User ID is $_uid"
	case "$_uid" in
		501)
			echo "Current user is root."
			echo ""
			;;
		*)
			echo "Current user is NOT root."
			echo ""
			;;
	esac
}

count_f(){
local files=()
while read -r -d ''; do
    files+=("$REPLY")
done < <(find $_d -type f -print0)

local _result=$1
eval $_result=${#files[@]}
}

count_txt(){
local txt=()
while read -r -d ''; do
    txt+=("$REPLY")
done < <(find $_d -type f -name "*.txt" -print0)

local _result=$1
eval $_result=${#txt[@]}
}

count_d(){
local dir=()
while read -r -d ''; do
    dir+=("$REPLY")
done < <(find $_d -type d -print0)

local _result=$1
local size=${#dir[@]}
local total=$((size - 1))
eval $_result=$total
}

get_emptyD(){
echo ""
eval "find $_d -type d -empty > empty_dir.out"
echo "The list of directories that are empty are in empty_dir.out."
echo "The contents of empty_dir.out is:"
echo ""
eval "cat empty_dir.out"
echo ""
}

eval_pswd(){
	if [ ${#_d} -ge 8 ] && [[ "$_d" =~ [0-9] ]] && [[ "$_d" =~ [a-z] ]] && [[ "$_d" =~ [A-Z] ]]; then
	echo ""
	echo "Psuedo password criteria met."
	else echo "Psuedo password criteria NOT met."
	fi	
}

reverse(){
	local cpy=${_d}
	local len=${#_d}
	for((i=$len-1;i>=0;i--)); do str_rev+="$str_rev${cpy:$i:1}"; done
	echo ""
	echo "$_d reversed is $str_rev"
}

if [ -d "$_d" ]; then
	get_UID
	count_f num_files
	count_d num_dir
	count_txt num_txt
	echo "Number of files in $_d: $num_files"
	echo "Number of directories in $_d: $num_dir"
	echo "Number of .txt files in $_d: $num_txt"
	get_emptyD
	eval_pswd
	reverse
else
	echo "$_d does not exist."
fi

exit 0
