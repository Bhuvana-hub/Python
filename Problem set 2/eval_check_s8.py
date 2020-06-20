# -*- coding: utf-8 -*-
"""
Write a function called eval_loop that iteratively prompts the user, 
takes the resulting input and evaluates it using eval, and prints the result. 
It should continue until the user enters 'done', and 
then return the value of the last expression it evaluated.
"""

import math

def eval_loop():
    while True:
        s1=input("enter the string to evalute eval loop \n enter done to stop from entering string  ")
        if s1=='done':
            break
        else:
            checkstring=eval(s1)
            print(checkstring)
        
def main():
    eval_loop()

if __name__ == '__main__':
    main()