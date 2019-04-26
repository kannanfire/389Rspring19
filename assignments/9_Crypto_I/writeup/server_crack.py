#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = "hashes.txt"
    passwords = "passwords.txt"
    characters = string.ascii_lowercase
    server_ip = "134.209.128.58"
    server_port = 1337 

    charlettered = []
    hashlist = {}

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
        hashlist[hashed] = ch
    

    count = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while count < 4:
        data = s.recv(1024)
        data = data.decode()
        datalen = len(data)
        temp = hashlist[data.rstrip()[datalen-69:datalen-4].rstrip()]
        temp = temp + "\n"
        temp = temp.encode()
        s.send(temp)

        count = count + 1

        if count == 3:
            print(s.recv(1024).decode().rstrip())
            break





    
        
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
