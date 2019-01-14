# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 23:02:57 2019

@author: Hesam
"""
def whoIsNext(names, r):
    Next = r+1
    ind_name = 0
    name = ''
    counter = 0
    while counter < Next:
        if ind_name+1 >= len(names):
            ind_name = 0
            name=names[ind_name]
            counter += 1
            if counter < Next:
                name = names[ind_name]
                counter += 1
                ind_name += 1
            else:
                return name
            
#            print(ind_name, 1111)
        else:
            name=names[ind_name]
            counter += 1
            if counter < Next:
                name=names[ind_name]
                counter += 1
                ind_name += 1
            else:
                return name
    return name
            
            
        
        
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"