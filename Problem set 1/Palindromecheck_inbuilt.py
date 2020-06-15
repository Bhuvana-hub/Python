# -*- coding: utf-8 -*-
"""
Palindrome modified
"""


import string 

def isPalindrome(a):
    m=list(a)
    z=m[::-1]
    print(z)
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