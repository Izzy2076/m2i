#!/bin/bash

read -p "entrer le chemin vers le repertoire : " dirpath

if [ -d "$dirpath" ];then
	for file in "$dirpath"/*.txt; do
		if [ -f "$file" ]; then
			size=$(stat -c%s "$file")
			echo "$size bytes"
		fi
	done
else
	echo "Error : not valid directory"
	exit 1
fi
