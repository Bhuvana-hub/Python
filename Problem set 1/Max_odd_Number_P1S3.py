# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:52:50 2020

@author: Bhuvana
"""


import string 

def Large_odd(k):
    ym_list=[]
    for i in range(0,len(k)):
            if k[i]%2!=0:
                ym_list.append(k[i])
            else:
                    i+=1
    if ym_list==[]:
        print("entered number doesn't have odd number ")
    else:
        max_num=max(ym_list)
        print("The maximum odd number is ",max_num)
    
    
    
def main():
    print("Program returns true if entered number has max odd number /n  ")
    k=[]
    n=int(input("Number of integer to be entered "))
    i=0
    while i < n:
        y=int(input("enter the integers " ))
        k.append(y)
        i+=1
    print("the Final input integer lst - ",k)
    Large_odd(k)

if __name__ == '__main__':
    main()