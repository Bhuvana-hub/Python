# -*- coding: utf-8 -*-
"""
Two words are anagrams if you can rearrange the letters from one to spell the other. 
Write a function called is_anagram that takes two strings and returns True 
if they are anagrams.
"""


import string 

def is_anagram(s1,s2):
    if len(s1)==len(s2):
        if sorted(s1)==sorted(s2):
            print(" enter two strings are anagram")
        else:
            print("enter two strings are not part of anagram")
    else:
        print("enter string of different length so it will not part of anagram")
    
def main():
    s1=input("enter the string 1 of Anagram check  ")
    s2=input("Enter string2 of Anagram check  ")
    is_anagram(s1, s2)

if __name__ == '__main__':
    main()
