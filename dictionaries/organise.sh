#!/bin/bash

if [ -z ${1+x} ];
then
	echo "USAGE: organise.sh FILE"
	return
fi

sed -E "s/ 	/\n/g" $1 | # Replace whitespace with newlines
	tr '[:upper:]' '[:lower:]' | # To lower case
	uniq | # Remove duplicates
	grep -e ".\{4,\}" | # Remove small words.  Removes excess newlines too
	sort # Sort results
