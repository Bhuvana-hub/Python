# -*- coding: utf-8 -*-
"""
Write a function called is_sorted that takes a list as a parameter and
 returns True if the list is sorted in ascending order and False otherwise.
 You can assume (as a precondition) that the elements of the
 list can be compared with the relational operators <, >, etc. 
 For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) 
 should return False
"""


import string 

def is_sorted(s):
    if s==sorted(s):
        return True
    else:
        return False
    
    
def main():
    s=[]
    n=int(input("Number of parameter to be entered "))
    i=0
    while i< n:
        y=int(input("Enter the parameter " ))
        s.append(y)
        i+=1
    print(s)
    checksort=is_sorted(s)
    if checksort==True:
        print("the parameter list is in sorted order")
    else:
        print("the parameter list is not in sorted order")

if __name__ == '__main__':
    main()