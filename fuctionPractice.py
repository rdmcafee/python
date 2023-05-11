#spher# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:55:42 2019

@author: Mcrye
"""

#from pylab import *
#Define a function that handles greeting
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, "+ username.title()+"!")
    
greet_user('jesse')
greet_user('ryan')

def display_message():
    """Prints message regarding chapter 8 contents"""
    print("Chapter 8 guides us through defining and calling functions!" +
          " What fun!")
display_message()

def favorite_book(book):
    """Display message regarding favorite book title."""
    print("One of my favorite books is " + book.title() + ". Give it a read!")
    
favorite_book('moby dick')

#Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'noel')
describe_pet('dog', 'bloo')

#Keyword arguments
describe_pet(pet_name = 'lary', animal_type = 'frog')

# More function practice
def make_shirt(shirt_size = 'Large', shirt_phrase = 'I Love Python!!!'):
    """Display shirt size and phrase"""
    print("\nShirt Size: " + shirt_size)
    print("Phrase: " + shirt_phrase)
    
make_shirt('Large', 'Buy me brunch, bitch!')
make_shirt(shirt_phrase = "'Merica!", shirt_size = 'Large')
make_shirt()
make_shirt('Medium')
make_shirt('Small', 'Big Things Come in Small Packages')

def describe_city(city_name, city_country = "'Merica!"):
    """Prints the city and country name"""
    print("\n" + city_name + " is in " + city_country + ".")
    
describe_city('Rome', 'Italy')
describe_city('Fort Wayne')
describe_city('Wabash')

# Return values
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

#The function get_formatted_name returns the formated name, we assign it a value
#musician, which we then print. When we do, we find the name has been formated!
    
musician = get_formatted_name('jimi', 'hendrix')
print('\n'+ musician)
musician = get_formatted_name('john','hoooker', 'lee')
print('\n'+ musician)

#Returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print('\n')
print(musician)

# Automated greeting reference lines 62-69
# Starting loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
# Practice with functions and dictionaries. 
def city_country(city_name, country_name):
    """Display city, country"""
    full_name = city_name +', ' + country_name
    return full_name.title()
print(city_country('santiago','chili'))
print(city_country('london','england'))
print(city_country('fort wayne','united states'))

def make_album(artist_name, album_title, album_tracks =''):
    """Return album dictionary"""
    album = {'Artist':artist_name.title(),'Album':album_title.title()}
    if album_tracks:
        album['Tracks']=album_tracks
    return album
print(make_album('jimi hendrix', 'Experience Hendrix'))
print(make_album('Incubus', 'morning view'))
print(make_album('Chris stapleton', 'Travler',12))

while True:
    print("\nEnter album info:")
    print("(enter 'q' at any time to quit)")
    
    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    a_title = input("Album title: ")
    if a_title == 'q':
        break
    a_track = input("No. of tracks: ")
    if a_track == 'q':
        break
    print(make_album(a_name, a_title, a_track))
