# -*- coding: utf-8 -*-
"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and 
returns True if a is a power of b. Note: you will have to think about the base case
"""


import math

def is_power(num1,num2):
        if num2==num2:
            return True
        elif num1%num2==0:
            for i in range(1,num1):
                if num2 ** i==num1:
                    return True
        else:
            return False
    
        
def main():
    num1=int(input("Enter the number1  "))
    num2=int(input("Enter the number2  "))
    checkpower=is_power(num1,num2)
    if checkpower==True:
        print(num1,'is power of',num2)
    else:
       print(num1,'is not power of',num2)
    

if __name__ == '__main__':
    main()