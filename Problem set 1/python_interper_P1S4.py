# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:29:23 2020

Practice using the Python interpreter as a calculator:

a) The volume of a sphere with radius r is 4/3pr3. What is the volume of a sphere
 with radius 5?
Hint: 392.7 is wrong!
b) Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. 
    Shipping costs
Rs.3 for the first copy and 0.75p for each additional copy.
 What is the total wholesale cost for 60 copies?
c) If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
    then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""


import math 

def sphere_check():
    r=5
    p=math.pi
    radius=4/3*p*r**3
    print("radius" , radius)
    
def wholesale_cost():
    cover_price=24.95
    discount=0.4
    discount_book_price=cover_price*discount
    actual_book_price=cover_price-discount_book_price
    print(actual_book_price)
    shipping_cost=3
    additional_copy=0.75
    first1=actual_book_price+shipping_cost
    remaining_copy=actual_book_price*59+additional_copy*59
    total=first1+remaining_copy
    print("final total wholesale cost",total)

 
def main():
    sphere_check()
    wholesale_cost()

if __name__ == '__main__':
    main()