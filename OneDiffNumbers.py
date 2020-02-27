# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:24:26 2020

@author: Hesam
"""

"""
Given a number N, write a code to print all positive numbers less than N in which
all adjacent digits differ by 1
example N = 105
Output:
1
2
3
4
5
6
7
8
9
10
12
21
23
32
34
43
45
54
56
65
67
76
78
87
89
98
101
"""

def challenge(number):
    #first make a list of all the numbers less than the given number
    p_list = [i for i in range(1,number)]
    print(p_list)
    
    #define a result list 
    result =[]
    
    #second, define a function for evaluating compliance of each number with the provided condition
    def evaluator(p_list):
        print(f"p_list {p_list}")
        # step 1, turn each member of the list into a string
        for k in p_list:
            print(f"k is: {k}")
            k_string = str(k)
            #step 2, separate digits of the number an put them in a list
            # now each number is a list of its digits in the string format
            k_list = [digit for digit in k_string]
            print(f"k_list is {k_list}")
            
            #step3, if the number only has 1 digit (0-9) add it to the results list
            digit_n = len(k_list)
            if digit_n == 1:
                result.append(k)
                
            #step 4, if the number has more than 1 digit (>9), we have to iterate through the digits
            # and calculate the difference between every two digits
            else:
                index = 0#have to define the index to add it up for not doing repetitive calculation
                diffs =[]#list of differences between digits is defined to add differences and evaluate if the number complies with the condition
                for n in range (digit_n):
                    try:#there might be some errors due to index increase
                        diff = abs(int(k_list[index])-int(k_list[index+1]))
                        print(f"diff is {diff}")
                        if diff>1 or diff<1:#if difference between 2 digits is more than 1 or 0 it is not good so will append a 0 to diffs list
                            diffs.append(0)
                            index+=1
                        else:
                            diffs.append(diff)# if difference is 1, will add it to diffs list
                            index += 1
                    except:
                        print("diff error")
                        index+=1   
                            

                li_checker = 1 # Define a variable to multiply all numbers in the list.
                #if there is a single 0 in diffs list, the input number doesn't meet the condition
                for m in diffs:
                    li_checker = li_checker *m 
                    print(f"li_checker is {li_checker}")
                if li_checker == 1:# if the result of multiplying diffs members is 1, the condition is met
                    result.append(k)
                                
                            
                            

        return result #evaluator function will return a list of acceptable numbers
    for x in evaluator(p_list):# an iterator will print all the numbers
        print(x)
            
            
        
        