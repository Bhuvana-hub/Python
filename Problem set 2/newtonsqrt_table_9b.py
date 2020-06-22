# -*- coding: utf-8 -*-
"""
Write a function named test_square_root that prints a table like this:
The first column is a number, a; the second column is the square root of a computed 
with the function NewtonSqrt(); 
the third column is the square root computed by math.sqrt; 
the fourth column is the absolute value of the difference between the two estimates
"""
import math
from prettytable import PrettyTable 

def test_square_root():
    dictvalue={}
    y=[]
    for i in range(1,10):
        y1=(i+i/i)/2
        y2=math.sqrt(i)
        y3=y1-y2
        dictvalue[i]={'Number':i,'Netwonsqrt':y1,'sqrt_root':y2,'difference':y3}
        y.append(dictvalue[i])
        i+=1
        t=PrettyTable(['Number','Netwonsqrt','sqrt_root','difference'])
    for i in range(0,len(y)):
        t.add_row([y[i]['Number'],y[i]['Netwonsqrt'],y[i]['sqrt_root'],y[i]['difference']])
        i+=1
    print(t)
               
def main():
    test_square_root()
    

if __name__ == '__main__':
    main()