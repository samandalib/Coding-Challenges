# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def harshad_num_list(seq_of_numbers):
    l = []
    l2= []
    for i in seq_of_numbers:
        l.append(str(i))
    for m in l:
        digits = []
#        print(m)
        for j in m:
            digits.append(int(j))
#            print(digits)
        l2.append(digits)
    for sublist in l2:
#        print(sum(sublist))
        S = sum(sublist)
#        print(S)
        n = ""
        for mem in sublist:
            n += str(mem)
            N = int(n)
        if S != 0 and N % S == 0:    
            print(N, "is a harshad Number")
#        

#harshad_num_list(range(1000))


def harshad_num(number):
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
#        

harshad_num(90)