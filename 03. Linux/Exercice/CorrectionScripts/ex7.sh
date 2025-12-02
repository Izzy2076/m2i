#!/bin/bash

read -p "Entrer le chemin vers le fichier : " filepath

if [ -e "$filepath" ] && [ -r "$filepath" ]; then
	echo "fileok"
	exit 0
else
	echo "Error : le fichier n'existe pas ou n'est pas lisible"
	exit 2
fi


