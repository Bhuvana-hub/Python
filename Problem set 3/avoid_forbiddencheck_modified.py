# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:39:53 2020

@author: Bhuvana
"""

import string 

def avoids(x,k):
    z=list(x) #comt
    ym=[]
    for i in range(0,len(z)):
            if z[i] in k:
                ym.append(z[i])
            else:
                    i+=1
    if ym==[]:
        print("Forbidden character are not present TRUE ")
    else:
        print("Forbidden character is present FALSE")
    
    print("the original string - ",''.join(z))
    
    
def main():
    print("Program returns true if given word doesn't have any forbidden string letters /n  ")
    x=input("enter a word that needs to be checked   ")
    k=[]
    n=int(input("Number of forbidden letters to checked  "))
    i=0
    while i < n:
        y=input("enter the forbidden letters " )
        k.append(y)
        i+=1
    print("the forbidden list - ",k)
    avoids(x,k)

if __name__ == '__main__':
    main()