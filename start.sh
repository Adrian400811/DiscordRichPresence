#!/bin/bash
echo 1. Main
echo 2. YT

read -p "1/2/3" var

if [ "${var}" == "1" ]; then
	printf "Selected Custom\n"
	python3 ./custom.py
elif [ "${var}" == "2" ]; then
	printf "Selected YT\n"
	node ./YT/index.js
else
	echo WTF u saying
fi
