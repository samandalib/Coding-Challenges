# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:30:41 2018

@author: Hesam
"""
'''
My Code for finding Harshad Numbers 
it gets a number and if it is devisable to the sum of its digits says it is a harshad number
else, it says it is not a harshad number

The URL on geeksforgeeks.org:
https://ide.geeksforgeeks.org/ERrMT9P9Nt

'''
number = input("")
number = int(number)
sn = str(number)
digits = []
for m in sn:
    digits.append(int(m))
for digit in digits:
    S = sum(digits)
    n = ""
    for mem in digits:
        n += str(mem)
        N = int(n)
if S != 0 and N % S == 0:    
    print(N, "is a harshad Number")
else:
    print(N, " is NOT a harshad Number")