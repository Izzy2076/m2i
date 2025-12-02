#!/bin/bash

greet(){
	echo "Hello to $1 and $2"
	echo "Nombre d'arguments : $#"
	echo "Tout les arguments : $@"
}

sum(){
	total=0
	for arg in "$@"; do
		total=$((total+arg))
	done
	echo "total : $total"
}


#greet "arg1" "arg2" "arg3" "arg4"

sum $@  #{1..10}
