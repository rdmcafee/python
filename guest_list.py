# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:39:38 2018

@author: Mcrye
"""

#create a guest list of three people
#create an invitation to each member of the lsit. 
guest_list = ["George Washington", "Abraham Lincoln", "John Adams"]
introductory_phrase = "Greetings, "
invitation_phrase = "You are cordially invited to a dinner party 1/1/2019. \
I look forward to seeing you there. \n\t Sincerely, JWB\n"

print ("\n")
print ( guest_list)

#practice replacing items in a list. 
print ("\nSorry folks, Georgio cannot make it to the dinner party; please"
       "review the new list for details\n")
guest_list[0] = "My mom"

print ("\n") 
print(guest_list)

#practice appending and inserting into lists. 
print ("\nOk, folks...it looks like the accomodations have improved; review" 
       " list for changes\n")
guest_list.insert(1, "Cinamon")
guest_list.insert(0, "Brotato-Chip")
guest_list.append("Mrs. JWB")

print ("\n") 
print (guest_list)

#practice removing people from lists
print("\n Ooooo, sorry. It looks like we'll have to cut a few people from the" 
      " list...our new table wont be available in time! Review list for changes.")
popped_guest = guest_list.pop(0)
print ("\n Sorry, " + popped_guest + " you didn't make the cut, asshole!")
popped_guest = guest_list.pop(0)
print ("\n Sorry, " + popped_guest + " you didn't make the cut, asshole!")
popped_guest = guest_list.pop(0)
print ("\n Sorry, " + popped_guest + " you didn't make the cut, asshole!")
popped_guest = guest_list.pop(1)
print ("\n Sorry, " + popped_guest + " you didn't make the cut, asshole!")
popped_guest = guest_list.pop(1)
print ("\n Sorry, " + popped_guest + " you didn't make the cut, asshole!")

print("\n")
print(guest_list)

#loop through list and print an invitation message.
send_it = input("Send list?")


if send_it == "yes":
    i = 0
    
    while i < len(guest_list): 
            print ("\n\t" + introductory_phrase + guest_list[i] + "! " + 
                   invitation_phrase)
            i += 1
            if i == 6:
                break
else:
    print ("Ok, I'll save this for later...")