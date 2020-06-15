# -*- coding: utf-8 -*-
"""
Write a function called is_abecedarian that returns True
 if the letters in a word appear in alphabetical order 
 (double letters are ok). How many abecedarian words are there? (i.e)
 "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"
"""

import string 

def is_abecedarian(s):
    y=list(s)
    print(y)
    z=sorted(y)
    print(z)
    if y==z:
        return True
    else:
        return False
    
    
def main():
    s=input("Enter the string to check whether given string is abecedarian or not  ")
    checkabe=is_abecedarian(s)
    if checkabe==True:
        print("the given word is abecedarian")
    else:
        print("the given word is not abecedarian")

if __name__ == '__main__':
    main()

