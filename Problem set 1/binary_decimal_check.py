# -*- coding: utf-8 -*-
"""
binary to decimal check
"""


import math

def bin_decimal(num):
    num2=list(num)
    num3=num2[::-1]
    print(num3)
    sum=0
    for i in range(0,len(num3)):
            y=int(num3[i])
            x=y*2**i
            sum=sum+x
            i+=1
    return sum
    
        
def main():
    num=input("Enter the binary number  ")
    numcheck=bin_decimal(num)
    print("the Binary to decimal output ",numcheck)
    

if __name__ == '__main__':
    main()
