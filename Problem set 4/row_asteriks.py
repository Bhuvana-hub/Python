# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:56:43 2020

Write both a nonrecursive and recursive function that displays the rows of asterisks
@author: Bhuvana
"""



def row_asterisks():
    rows=7
    n=(2*rows)-2
    for i in range(0,rows):
        for j in range(0,n):
            print(end=" ")
        n=n-1
        for j in range(0,i+1):
            print("*",end=' ')
        print(" ")
                
def main():
    row_asterisks()
    
if __name__=='__main__':
    main()
