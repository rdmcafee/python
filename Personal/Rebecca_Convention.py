'''
Created on May 7, 2023

@author: Mcrye
'''

import pandas as pd
import numpy as np

data = pd.read_excel(r'C:\Users\Mcrye\workspace\Python\Personal\convention_01.xlsx', 
                     engine = 'openpyxl', sheet_name = 'MINE', 
                     usecols = [0, 4])

session = data.iloc[:, [0]]
tara = data.iloc[:, [1]]
session.sort_values(by = ['Session Tickets '], ascending = True, inplace = True )
session.dropna(axis = 'rows', how = 'any', inplace = True)
session.reset_index(inplace = True, drop = True)
tara.sort_values(by = ['Tara\'s List '], ascending = True, inplace = True)
tara.dropna(axis = 'rows', how = 'any', inplace = True)
tara.reset_index(inplace = True, drop = True)
print(session)
print(tara)

new_data = pd.concat([session, tara], axis = 1)
print(new_data)

print(new_data.keys())

new_data.to_excel(r'C:\Users\Mcrye\workspace\Python\Personal\cleanData_Alphabetized.xlsx', 
                  sheet_name = "CleanData")
