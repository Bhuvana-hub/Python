# -*- coding: utf-8 -*-
"""
Write a program that examines three variables—x, y, and z— and 
prints the largest odd number among them. If none of them are odd, 
it should print a message to that effect.
"""
import math

def oddfind(x,y,z):
    s1=x,y,z
    ym=[]
    for i in range(0,len(s1)):
        if s1[i]%2!=0:
            ym.append(s1[i])
        else:
            i+=1
    print(ym)
    if ym==[]:
        return 0
    else:
        return max(ym)

def main():
    print("To get Three Largest Odd Number")
    x = int(input("Enter the number1 \n"))
    y = int(input("Enter the number2 \n"))
    z = int(input("Enter the number3 \n"))
    m=oddfind(x,y,z)
    if m==0:
        print("All 3 Numbers are not odd number")
    else:
        print("The Largest Number", m)

if __name__ == '__main__':
    main()