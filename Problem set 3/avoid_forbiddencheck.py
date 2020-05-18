# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:39:53 2020

@author: Bhuvana
"""

import string 

def avoids(x,k):
    k2=k.split(' ') #aerh
    ##print(k2)
    z=list(x) #comt
    ym=[]
    for i in range(0,len(z)):
            if z[i] in k2:
                ym.append(z[i])
            else:
                    i+=1
    if ym==[]:
        print("Forbidden character are not present TRUE ")
    else:
        print("Forbidden character is present FALSE")
    
    print("the original string",''.join(z))
    print("the forbidden letter in original string",' '.join(ym))
    
    
def main():
    print("Program returns true if given word doesn't have any forbidden string letters /n  ")
    x=input("enter a word that needs to be checked   ")
    k=input("enter the forbidden letters by providing space between 2 letters")
    avoids(x,k)

if __name__ == '__main__':
    main()