#!/bin/bash

#-- check whether correct arguments are passed to the script. 
#-- #1 - Path to folder containing images.
#-- #2 - Timeout for wallpaper change.
#-- #3 - Desktop Envioronment e.g. gnome, mate etc.

if [ $# != 3 ]
then
echo "'readlink -f $0':No arguments supplied."
echo "Please give directory containing wallpapers or images."
exit -1
fi

envio=$3
if [ $envio == 'gnome' ]
then
	setbackground="gsettings set org.gnome.desktop.background picture-uri file://"
else
	setbackground="gsettings set org.mate.background picture-filename "
fi

wallpapertimeout=$2

pathname=$1
if [ ! -d $pathname ]
then 
echo "$pathname is not a directory"
exit -1
fi

if [ $pathname == "." ]
then
pathname='pwd'
fi

if [ $pathname == ".." ]
then
pathname='dirname $PWD'
fi

echo "Got the directory and its path is $pathname"

filecount=$(ls -l $pathname/*.JPG | wc -l)
#filecount=$(find $pathname -type f | wc -l)

if [ $filecount == 0 ]
then
echo "No wallpapers or images found in directory"
exit -1
fi

echo "Number of wallpapers in directory are $filecount"

filelst='ls $pathname/*.JPG'
while [ 1 ]
do
	j=1
	rndnum=$(($RANDOM % $filecount + 1 | bc))
	for i in $(ls $pathname/*.JPG)
	do
		if [ $j == $rndnum ]
		then
		echo "Got the match for $i"
			$setbackground$i
		fi
		j=$(($j+1))
	done
	sleep $wallpapertimeout
done
