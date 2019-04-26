#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = "hashes.txt"
    passwords = "passwords.txt"
    characters = string.ascii_lowercase
    
    charlettered = []

    with open(passwords) as p:
    	for line in p:
    		for c in characters:
    			ch = c + line
    			ch = ch.rstrip()
    			charlettered.append(ch)

   	

    for ch in charlettered:
    	a = ch.rstrip().encode().rstrip()
    	hashed = hashlib.sha256(a)
    	hashed = hashed.hexdigest().rstrip()

    	with open(hashes, "r") as h:
    		for line in h:
    			if line.rstrip() == hashed:
    				print(ch + ":" + hashed)

if __name__ == "__main__":
    crack()
