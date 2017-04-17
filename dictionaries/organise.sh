#!/bin/bash

if [ -z ${1+x} ];
then
	echo "USAGE: organise.sh FILE [MIN_LENGTH]"
	exit
fi

if [ -z ${2+x} ];
then
	MIN_LENGTH=4
else
	MIN_LENGTH=$2
fi

sed -E "s/ 	/\n/g" $1 | # Replace whitespace with newlines
	tr '[:upper:]' '[:lower:]' | # To lower case
	uniq | # Remove duplicates
	grep -e ".\{$MIN_LENGTH,\}" | # Remove small words.  Removes excess newlines too
	sort # Sort results
