from pyautogui import *
import pyautogui
import time
import keyboard
import random
from win32 import win32api
from win32.lib import win32con

#Tile 1 Position: X:  763 Y:  934 RGB: (158, 163, 231)
#Tile 2 Position: X:  875 Y:  994 RGB: (253,  18,   1)
#Tile 3 Position: X: 1032 Y:  952 RGB: (152, 157, 230)
#Tile 4 Position: X: 1200 Y:  952 RGB: (169, 173, 232)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(700, 750)[0] == 0:
        click(x=700, y=750)
    if pyautogui.pixel(875, 750)[0] == 0:
        click(x=875, y=750)
    if pyautogui.pixel(1075, 750)[0] == 0:
        click(x=1075, y=750)
    if pyautogui.pixel(1200, 750)[0] == 0:
        click(x=1200, y=750)
        
