#!/bin/bash

if ls myFile; then
	exit 0
else
	exit 2
fi


echo "end"
