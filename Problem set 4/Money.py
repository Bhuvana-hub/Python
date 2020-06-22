# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:52:59 2020

Design and implement a Money class that stores monetary values in dollars and cents.
 Special method init should have the following function header, def init(self, dollars, cents) 
 Include special method repr (str) for displaying values in dollars 
 and cents: $ 0.45, $ 1.00, $ 1.25. Also include special method add, 
 and three getter methods that each provide the monetary value in another currency. 
 Choose any three currencies to convert to
"""

class Money:
    def __init__(self,dollars,cents):
        self.dollar_1=dollars
        self.cents_1=cents
        
    def __repr__(self):
        return '$'+str(self.add())
    
    def add(self):
        #self.sum1=self.dollar_1+self.cents_1
        return(self.dollar_1+self.cents_1)
        
    def GRB(self,foreignexchange=80):
        print((self.dollar_1+self.cents_1)*foreignexchange)
    
    def CHN(self,foreignexchange=20):
        print((self.dollar_1+self.cents_1)*foreignexchange)
    
    def IND(self,foreignexchange=1):
        print((self.dollar_1+self.cents_1)*foreignexchange)

t=Money(1,0.75)
print(t)
t.GRB()
t.CHN()
t.IND()

