# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:35:36 2020

Write a function isIn() that accepts two strings as arguments and 
returns True if either string occurs anywhere in the other, and False otherwise.
 Hint: you might want to use the built-in str operation in.
"""

import string

def IsIn(str1,str2):
    print(str1,str2)
    if str1 in str2:
        return True
    elif str2 in str1:
        return True
    else:
        return False
       
      
def main():
    str1=input("enter string 1 ")
    str2=input("enter string2 ")
    check_in_func=IsIn(str1,str2)
    if check_in_func==True:
        print("The string1 is present in String 2 or vice versa")
    else:
        print("the string doesn't present between each other")

if __name__ == '__main__':
    main()


