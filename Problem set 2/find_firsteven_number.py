# -*- coding: utf-8 -*-
"""
Implement a function that satisfies the specification. Use a try-except block.
def findAnEven(l):
	Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number
"""

import string 

def findAnEven(k):
    try:
        for i in k:
                if i%2==0:
                    print('the first even number of list',i)
                    exit()
                raise ValueError
    except ValueError as valer:
        print("All number are odd and enter atleast one even number")
     
def main():
    print("Program returns first even number from list /n  ")
    k=[]
    n=int(input("Number of entries to the list "))
    i=0
    while i < n:
        y=int(input("enter the numbers to the list " ))
        k.append(y)
        i+=1
    print("the final list - ",k)
    findAnEven(k)

if __name__ == '__main__':
    main()