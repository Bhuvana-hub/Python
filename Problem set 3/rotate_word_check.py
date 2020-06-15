# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:22:33 2020

@author: Bhuvana
"""

import string 

def rotate_word(x,k):
    z=list(x)
    ym=[]
    zm=string.ascii_lowercase
    xm=list(zm)
    for i in range(0,len(z)):
        m=z[i] # c
        n=xm.index(m) #2
        p1=n+k #7
        p2=xm[p1]
        ym.append(p2)
        i+=1
        
    print(ym)
    lm=''.join(ym)
    print(lm)
        
    
def main():
    print("To rotate the string no of times")
    x=input("enter the string that needs to be rotated")
    k=int(input("no of times the string has to be rotated"))
    rotate_word(x,k)

if __name__ == '__main__':
    main()
