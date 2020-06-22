# -*- coding: utf-8 -*-
"""
One way of computing square roots is Newton’s method. 
Suppose that you want to know the square root of a.
 If you start with almost any estimate, x, 
 you can compute a better estimate with the following formula: y = (x + a/x)/2 
 For example, if a is 4 and x is 3:
"""


import math
def Newtonsqrt(num1,num2):
    y=(num2+num1/num2)/2
    return y
        
def main():
    num1=float(input("Enter the number for which square root has to be find  "))
    num2=float(input("Enter the number which could be assume as square root of num1 "))
    square_root_value=Newtonsqrt(num1,num2)
    print("the square roots value is " ,square_root_value)
    

if __name__ == '__main__':
    main()