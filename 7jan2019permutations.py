# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:17:55 2019

@author: Hesam
"""

def permutations(string):
    from itertools import permutations
    l = [''.join(i) for i in list(permutations(string))]
    result = set()
    for member in l:
        result.add(member)
    return list(result)
            