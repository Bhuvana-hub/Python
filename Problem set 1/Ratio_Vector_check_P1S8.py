# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:50:49 2020

Implement a function that satisfies the specification. Use a try-except block.

def getRatios(vect1, vect2):
	Assumes: vect1 and vect2 are lists of equal length of numbers
	Returns: a list containing the meaningful values of
	vect1[i]/vect2[i]
"""
 

def getRatios(vect1,vect2):
    list_empty=[]
    for i in range(0,len(vect1)):
        try:
            y=vect1[i]/vect2[i]
            list_empty.append(y)
        except:
            list_empty.append("NAAA")
                
    print(list_empty)
     
def main():
    vect1=[2,3,5,6,9]
    vect2=[1,4,8,12,13]
    vect3=[1,4,8,12,13]
    vect4=[2,0,5,6,45]
    getRatios(vect1, vect2)
    getRatios(vect3, vect4)

if __name__ == '__main__':
    main()