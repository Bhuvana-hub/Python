# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:09:11 2020

@author: Bhuvana
Add an eq method that returns True if coordinates refer to same point in the plane
 (i.e., have the same x and y coordinate)
 
 Define repr, a special method that returns a string that looks like a 
 valid Python expression that could be used to recreate an object with the same value. 
 In other words, eval(repr(c)) == c given the definition of eq from part 1.
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def eq(self,x,y):
        return self.x==self.y
    
    def __repr__(self):
        return str(self.getX()==self.getY())
    
x1=int(input("enter coordinate x" ))
y1=int(input("enter coordinate y" ))
t=Coordinate(x1, y1)
print(t)
print(t.__str__())
print(t.eq(x1,y1))
print(eval(repr(t)))
