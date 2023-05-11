# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 01:27:01 2021

@author: Mcrye
"""

import turtle

bob = turtle.Turtle()
print(bob)

i = 0
while i < 200:
    bob.fd(5)
    bob.lt(2)
    i += 1


turtle.mainloop()