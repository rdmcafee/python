# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:19:27 2022

@author: Mcrye
"""
from sympy import *
from tkinter import *
from tkinter import ttk
from sympy.interactive import printing
printing.init_printing(use_latex=True)
#from sympy import init_printing
#from sympy import Eq
import numpy as np
import scipy as sc

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
x, y, z = symbols('x y z')
init_printing()

eq1 = latex(Integral(sqrt(1/x), x))

ttk.Label(frm, text = '$V_{0}$').grid(column=0, row=0)
root.mainloop()
input("Press Enter to Continue...")
