#!/bin/bash
cmd1=`ifconfig | grep 127`
#cmd2=`sudo service iptables stop`
#cmd3=`sudo service sshd start`
#cmd4=`service httpd start`
cmd5=`wireshark -v | grep 'Wireshark'`
#cmd6=`nmap -V | grep "Nmap"`
cmdn=`hostname`

echo "${cmd1}"
printf "\n\n\n"
#echo "${cmd5}"
#printf "\n\n\n"
#echo "${cmd6}"
#printf "\n\n\n"

if [ "${cmdn}" == "VAIO-SVE14D11L" ] && [ "${cmd1}" == "        inet 127.0.0.1  netmask 255.0.0.0" ]; then
	echo "F.1 NIC is correct"
    echo "${cmd5}"
#else if [ "${cmd1}" == "172.60.100.4 netmask 255.0.0.0" ] && [ ${cmdn} == "F.2" ]; then
#	echo "F.2 NIC is correct"
	#${cmd4}
	#${cmd3}
	#${cmd2}
#else if [ "${cmd1}" == "172.10.30.15 netmask 255.0.0.0" && ${cmdn} == "A.F" ]; then
#	echo "A.F NIC is correct"
	#${cmd4}
	#${cmd3}  
	#${cmd2}
else
	echo "Incorrect NIC configuration"
fi
