#!/usr/bin/env python

from __future__ import print_function

import sys

def main():
    if len(sys.argv) < 2:
        print("USAGE: organise.py FILE_NAME [MIN_LENGTH]")
        return

    min_length = 4
    try:
        min_length = int(sys.argv[2])
    except (IndexError, ValueError) as ex:
        pass

    with open(sys.argv[1], 'r') as f:
        read = f.readlines()
        read = [x.strip() for x in read]
        read = filter(lambda x: ' ' not in x, read) # Filter out two word elements
        read = filter(lambda x: len(x) >= min_length, read) # Filter out small words
        read = filter(lambda x: '-' not in x, read)
        read = map(lambda x: x[0].upper() + x[1:].lower(), read)
        read = list(set(read)) # Remove duplicates
        read = sorted(read) # Sort
        for r in read:
            print(r)

if __name__ == '__main__':
    main()
