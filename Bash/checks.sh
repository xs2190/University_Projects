#!/bin/bash
cmd1=`ifconfig | grep 172`
cmd2=`sudo service iptables stop`
cmd3=`sudo service sshd start`
cmd4=`sudo service httpd start`
cmd5=`wireshark -v`
cmd6=`nmap -V`
cmdn=`hostname`

echo "${cmd1}"
echo "${cmd5}"
echo "${cmd6}"
echo "${cmd2}"

if [ "${cmd1}" == "        172.60.50.3 netmask 255.0.0.0" ] && [ "${cmdn}" == "F.1" ]; then
	echo "F.1 NIC is correct"
else if [ "${cmd1}" == "        172.60.100.4 netmask 255.0.0.0" ] && [ "${cmdn}" == "F.2" ]; then
	echo "F.2 NIC is correct"
	echo "${cmd4}"
	echo "${cmd3}"
else if [ "${cmd1}" == "        172.10.30.15 netmask 255.0.0.0" ] && [ "${cmdn}" == "A.F" ]; then
	echo "A.F NIC is correct"
	echo "${cmd4}"
	echo "${cmd3}"
else
	echo "${cmd1}"
	echo "Incorrect NIC configuration"

fi #end of file
