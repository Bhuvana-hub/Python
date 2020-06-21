# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:02:24 2020

Write a program that asks the user to enter an integer and prints two integers, 
root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
 If no such pair of integers exists, it should print a message to that effect.
"""

def power_root_check(n):
    root=0
    power=0

    while root<=n:        
        root+=1   
        while power<6:         
            power+=1 
            if root**power==n:     
                print(root,power)
        power=0
       
      
def main():
    n=int(input("Enter the integer "))
    power_root_check(n)

if __name__ == '__main__':
    main()
