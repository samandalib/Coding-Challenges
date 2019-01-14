# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:39:39 2018

@author: Hesam
"""
'''
This code is written after a first try with the use of list properties; I found this one as another alternative\
which is really more efficient because it is O(n) order.
'''

N = input()
length = len(N)
Number = int(N)
l = []
c = 1
while c <= length:
    R = Number % 10**c
    R = str(R)
    l.append(int(R[0]))
    c += 1
l.reverse()
S = sum(l)
if S != 0 and Number % S == 0:
    print(Number, 'is a Harsahd Number')
else:
    print(Number, 'is NOT a Harsahd Number')