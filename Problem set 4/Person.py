# -*- coding: utf-8 -*-
"""
Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and 
"Female" for Female class.

@author: Bhuvana
"""


class Person:
    def __init__(self):
        pass
        
    def getGender(self):
        pass
    
class Male(Person):
    def __init__(self):
        Person.__init__(self)
        
    def getGender(self):
        print("Male")
        
class Female(Person):
    def __init__(self):
        Person.__init__(self)
        
    def getGender(self):
        print("Female")
        
t1=Male()
t1.getGender()
t2=Female()
t2.getGender()

        