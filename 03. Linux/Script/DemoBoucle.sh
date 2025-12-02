#!/bin/bash


couleurs=( "rouge" "vert" "bleu" )

echo "${couleurs[@]}"


for i in "${couleurs[@]}"; do
	echo $i
done

compteur=1

while [[ $compteur < 6 ]]; do
	echo $compteur
	compteur=$((compteur+1))
done


