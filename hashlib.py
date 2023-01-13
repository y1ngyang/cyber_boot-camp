##!/usr/bin/env python3

#hashlib module implements a list of hash algorithms. 
import hashlib

path = r"/home/kali/hash_this.txt"


md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512() 

list_hash_objects = [md5, sha1, sha256, sha512]

with open(path,"rb") as hash_f:
   print('Result')
   print()
   content = hash_f.read()
   for hashed_string in list_hash_objects:
       hashed_string.update(content)
       print('{}: {}'.format(hashed_string.name, hashed_string.hexdigest()))

