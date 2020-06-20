# -*- coding: utf-8 -*-
"""
The greatest common divisor (GCD) of a and b is the largest number 
that divides both of them with no remainder. 
One way to find the GCD of two numbers is based on the observation that
 if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). 
 As a base case, we can use gcd(a, 0) = a.
 Write a function called gcd that takes parameters a and b and 
 returns their greatest common divisor
"""


import math

def gcd(num1,num2):
    while(num1!=num2):
        if num1>num2:
            num1=num1-num2
            print(num1)
        else:
            num2=num2-num1
            print(num2)
    return num1
    
        
def main():
    num1=int(input("Enter the number1  "))
    num2=int(input("Enter the number2  "))
    if num2==0:
        print ('gcd of ' , num1, 'and',num2, 'is',num1)
    elif num1==0:
        print ('gcd of ' , num1, 'and',num2, 'is',num2)
    elif num1==num2:
        print ('gcd of ' , num1, 'and',num2, 'is',num1)
    else:
        numcheck=gcd(num1,num2)
        print ('gcd of ' , num1, 'and',num2, 'is',numcheck)
    

if __name__ == '__main__':
    main()