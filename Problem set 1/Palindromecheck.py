# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:19:35 2020

@author: Bhuvana
"""


import string 

def isPalindrome(a):
    y=len(a)
    m=list(a)
    z=[]
    for i in range(1,len(m)+1):
        x=m[-i]
        z.append(x)
        i+=1
    if z==m:
        print(''.join(z))
        print(''.join(m))
        print(" the string is palindrome")
    else:
        print(''.join(z))
        print(''.join(m))
        print(" the entered string is not palindrome")
            
def main():
    a=input("Enter the string to check palindrome  ")
    isPalindrome(a)

if __name__ == '__main__':
    main()