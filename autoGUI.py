'''
Created on Feb 18, 2022

@author: Mcrye
'''
import pyautogui

fw = pyautogui.getActiveWindow()

fw.width = 1200

pyautogui.move(500, 550, duration = 3.0)

pyautogui.click(500, 550)

#pyautogui.write('Hello World!')

#Write something here: 