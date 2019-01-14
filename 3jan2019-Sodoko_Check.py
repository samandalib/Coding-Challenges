# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 00:43:31 2019

@author: Hesam
"""

def done_or_not(board):
    import numpy as np
    b = np.array(board)
    bx= b.transpose()
    chunks = np.array([b[0:3,0:3],b[0:3,3:6],b[0:3,6:9],b[3:6,0:3],b[3:6,3:6],b[3:6,6:9],b[6:9,0:3],b[6:9,3:6],b[6:9,6:9]])
    test = set()
    for i in b:
        for j in i:
            test.add(j)
        if len(test) < 9:
            return 'Try again!'
        else:
            test = set()
            continue
    for k in bx:
        for m in k:
            test.add(m)
        if len(test) < 9:
            return 'Try again!'
        else:
            test = set()
            continue  
    for p1 in chunks:
        for p2 in p1:
            for p3 in p2:
                test.add(p3)
        if len(test)<9:
            return 'Try again!'
        else:
            test = set()
            continue
    return 'Finished!'
        
    
    
    
    
    
    
#    b[0:3,0:3]
#    b[0:3,3:6]
#    b[0:3,6:9]
#    
#    b[3:6,0:3]
#    b[3:6,3:6]
#    b[3:6,6:9]
#    
#    b[6:9,0:3]
#    b[6:9,3:6]
#    b[6:9,6:9]
    