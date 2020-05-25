# -*- coding: utf-8 -*-
"""
Write a function called has_no_e that returns True if the
given word doesn’t have the letter "e" in it.
"""



def has_no_e(s1):
    if 'e' in s1:
        print(" letter e is present in the word" , s1)
    else:
        print(" letter e is not present in the word", s1)



def main():
    s1=input("enter the string to check e condition  ")
    has_no_e(s1)
    


if __name__=='__main__':
    main()

    