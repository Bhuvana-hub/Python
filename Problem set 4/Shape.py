# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:54:54 2020

1.Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function
 which can print the area of the shape where Shape's area is 0 by default
"""


class Shape:
    def __init__(self):
        pass
        
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length1):
        Shape.__init__(self)
        self.length=length1
        
    def area(self):
        return self.length*self.length

n=int(input("enter the length of an area to find square "))
t1=Square(n)
print("Area of subclass",t1.area())
#print(a2)
t2=Shape()
print("Area of mainclass",t2.area())
        
    
    
    