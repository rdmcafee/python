# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:38:18 2019

@author: Mcrye
"""

# 8-11
print('\n')
magician_names = ['joe', 'Bob', 'gob', 'john', 'Gary']

def make_great(magicians):
    """Modifies names in a list by inserting 'Great ' """
    great_magicians = []
    
    while magicians: 
        magician = magicians.pop()
        great_magician = magician + " the Great!"
        great_magicians.append(great_magician) 
        
    for great_magician in great_magicians:
        magicians.append(great_magician)
        
    return magicians
           
def show_magicians(names):
    """Takes a list of names and prints them"""
    for name in names:
        print(name.title())

great_names = make_great(magician_names[:])
show_magicians(great_names)
show_magicians(magician_names)