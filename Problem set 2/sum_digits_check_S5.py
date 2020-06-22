# -*- coding: utf-8 -*-
"""
Implement a function that meets the specification below. Use a try-except block.

def sumDigits(s):
	Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5
"""


import math

def sumDigits(num1):
    sumlist=[]
    try:
        for i in num1:
            if i.isdigit():
                sumlist.append(int(i))
        print('the sum of digits',num1,'is',sum(sumlist))
        raise ValueError
    except ValueError as valerr:
        print("entered string doesn't contain number")
    
        
def main():
    num1=input("Enter string with number ")
    sumDigits(num1)


if __name__ == '__main__':
    main()