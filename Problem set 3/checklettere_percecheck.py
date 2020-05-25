# -*- coding: utf-8 -*-
"""
Modify the above program to print only the 
words that have no “e” and compute the percentage of the words in the list have no “e.
"""
import math

def check_elist(Slist):
    ymelist=[]
    ym_not_e_list=[]
    for i in range(0,len(Slist)):
        if 'e' in Slist[i]:
            ymelist.append(Slist[i])
            i+=1
        else:
            ym_not_e_list.append(Slist[i])
            i+=1
    return ym_not_e_list
    
def main():
    Slist=[]
    n=int(input("enter the no of words "))
    i=0
    while i < n:
        y=input("enter the words ")
        Slist.append(y)
        i+=1
    print("entered words - ",Slist)
    ym_not_e_list=check_elist(Slist)
    if ym_not_e_list==[]:
        print("Entered words all has letter e in it ")
    else:
        print("words which has no e in the list - ",ym_not_e_list)
        checlen1=len(Slist)
        checlen2=len(ym_not_e_list)
        Percheck=(checlen2/checlen1)*100
        print("Percentage of the words in the list that as no e ", Percheck)   

if __name__=='__main__':
    main()