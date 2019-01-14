# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 23:36:04 2019

@author: Hesam
"""

def is_merge(s, part1, part2):
    while len(s)>0:
        if len(part1)>1 and len(part2)>1 and s[0] == part1[0] and s[0] == part2[0]:
            if s[1] == part1[1]:
                print(11)
                s = s[2:]
                print(111)
                part1 = part1[2:]
                print(1111)
                
            elif s[1] == part2[1]:
                print(22)
                s = s[2:]
                print(222)
                part2 = part2[2:]
                print(2222)
            else:
                return False
        elif len(part1)>0 and s[0] == part1[0]:
            print('s1=',s)
            s = s[1:]
            print('s11=',s)
            print('part1= ', part1)
            part1 = part1[1:]
            print('part11= ', part1)
    
        elif len(part2)>0 and s[0] == part2[0]:
            print('s2=',s)
            s = s[1:]
            print('s22=',s)
            print('part2= ',part2)
            part2 = part2[1:]
            print('part22= ',part2)
        else:
            return False
    else:
        return s == part1 and s == part2
#    if s == part1 or s == part2:
#        return True
#    else:
#        is_merge(s, part1, part2)
        
