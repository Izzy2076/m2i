#!/bin/bash


read -p "Entrer un nombre " number



if [[ number > 0 ]]; then
	echo "Positif"
elif (( number < 0 )); then
	echo " Negatif"
elif (( number == 0 ));then
	echo "Egale a 0"
fi
