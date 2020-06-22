# -*- coding: utf-8 -*-
"""
Let s be a string that contains a sequence of decimal numbers 
separated by commas, e.g., s = '1.23,2.4,3.123'. 
Write a program that prints the sum of the numbers in s 
"""

import operator 

def addtu(s):
    
    sum=0
    for i in range(0,len(s)):
        sum=sum+s[i]
        i+=1
    return sum
    
    
def main():
    s=1.23,2.4,3.123
    print(" the data type of s is ", type(s))
    consol_value=addtu(s)
    print(" the sum of the type is ",consol_value)

if __name__ == '__main__':
    main()