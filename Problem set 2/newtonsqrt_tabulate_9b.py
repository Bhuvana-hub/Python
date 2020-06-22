# -*- coding: utf-8 -*-
"""
Write a function named test_square_root that prints a table like this:
The first column is a number, a; the second column is the square root of a computed 
with the function NewtonSqrt(); 
the third column is the square root computed by math.sqrt; 
the fourth column is the absolute value of the difference between the two estimates
"""
import math
from tabulate import tabulate 

def test_square_root():
    num2=3
    dictvalue={}
    finalvalue={}
    y=[]
    for i in range(1,10):
        y1=(num2+i/num2)/2
        y2=math.sqrt(i)
        y3=y1-y2
        dictvalue[i]={'Number':i,'Netwonsqrt':y1,'sqrt_root':y2,'difference':y3}
        y.append(dictvalue[i])
        i+=1
    print(tabulate(y,tablefmt="github"))
        
               
def main():
    test_square_root()
    

if __name__ == '__main__':
    main()