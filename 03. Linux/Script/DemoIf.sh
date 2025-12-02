

echo "rentrer la valeur a : "
read a
echo "entrer la valeur b :"
read b


if (( "$a" ==  "$b" )); then
	echo "$a egale a $b"
elif (( "$a" <  "$b" )); then
	echo "$a superieur a $b"
else
	echo "$b superieur a $a"
fi



