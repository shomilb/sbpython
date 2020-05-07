# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:43:31 2020

@author: bansal
"""

d_marriage = input ("Is driver married: M/U: ")
d_gender = input ("Enter driver's gender: M/F: ")                    
d_age = input ("Enter driver's age: ")
d_age = int(d_age)
if (d_marriage == 'M'):
    print ("Insured")
elif (d_gender == 'M'):
    if (d_age >= 30):
        print ("Insured")
    else:  
        print ("Not insured")
elif (d_gender == 'F'):
    if (d_age >= 25):
        print ("Insured")
    else:
        print ("Not insured")


