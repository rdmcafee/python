# -*- coding: utf-8 -*-
"""
Created on Sun May 26 01:55:40 2019

@author: Mcrye
"""

# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names: 
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print('\n')

# Making changes to a list.
# Start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design until none are left
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
print('\n')
    
# Updated design of above program
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 'Try it yourself' 
# 8-9 Magicians
print('\n')
magician_names = ['joe', 'Bob', 'gob', 'john', 'Gary']

def show_magicians(names):
    """Takes a list of names and prints them"""
    for name in names:
        print(name.title())
        
show_magicians(magician_names)
print(magician_names)

# 8-10 Great Magicians
print('\n')
magician_names = ['joe', 'Bob', 'gob', 'john', 'Gary']

def make_great(magicians):
    """Modifies names in a list by inserting 'Great ' """
    great_magicians = []
    while magicians: 
        magician = magicians.pop()
        great_magicians.append(magician + " the Great! ")        
    for great_magician in great_magicians:
        magicians.append(great_magician)
           
def show_magicians(names):
    """Takes a list of names and prints them"""
    for name in names:
        print(name.title())

make_great(magician_names)
show_magicians(magician_names)

# 8-11
print('\n')
magician_names = ['joe', 'Bob', 'gob', 'john', 'Gary']

def make_great(magicians):
    """Modifies names in a list by inserting 'Great ' """
    great_magicians = []
    
    while magicians: 
        magician = magicians.pop()
        great_magicians.append(magician + " the Great! ") 
        
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