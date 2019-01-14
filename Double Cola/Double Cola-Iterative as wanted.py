# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:49:28 2019

@author: Hesam
"""
# The first Iterative solution with While Loop and append list
def whoIsNext(names, r):
    counter = r
    while counter > 1:
            names.append(names[0])
            names.append(names[0])
            counter -= 1
            names.remove(names[0])
    return names[0]

whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"

# The second Iterative solution with For Loop and extend list 
def whoIsNext(names, r):
    for i in range(r):
        names.extend([names[0],names[0]]) 
        names.remove(names[0])
    return names[0]
    