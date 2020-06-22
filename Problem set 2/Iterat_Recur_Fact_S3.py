# -*- coding: utf-8 -*-
"""
Observe the following function definitions. They Calculate the Factorial as 
per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n! Implement factI(n) 
as an Iterative Implementation & factR(n) as a Recursive Implementation
"""


def factI(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
        
def factR(n):
    if n==1:
        return 1
    else:
        return n*factR(n-1)
        
def main():
    n=int(input("enter the number to find factorial  "))
    if n==1:
        print(" the factorial of" ,n, "is", n)
    else:
        iterative_impl=factI(n)
        Recursive_impl=factR(n)
        print("The iterative implemetation of factorial",n,"is", iterative_impl)
        print("The iterative implemetation of factorial",n,"is", Recursive_impl)

if __name__ == '__main__':
    main()