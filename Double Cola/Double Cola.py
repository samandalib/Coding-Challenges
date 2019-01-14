# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 00:43:40 2019

@author: Hesam
"""

def whoIsNext(names, r):
    if r == 0 or r == 1:
        Next = names[0]
    else:
        if r % 2 == 1:
            Next = whoIsNext(names, r-1)
        else:
            ind = names.index(whoIsNext(names, r-1))+1
            if ind >= len(names):
                Next = names[ind - len(names)]
            else:
                Next = names[ind]
    return Next