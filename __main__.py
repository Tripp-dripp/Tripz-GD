#Ayo fig thanks for trying out and reading my code, it means A LOT!, This took  hours to code(I suck = True)
#Anyways i got that messy, messy code share this, mod and use this as you please!, Its a beta but I polished it a lil' bit .




import random
import math
import gd
import win32gui
import win32api
import win32con
import json
import win32api
import time

mem = gd.memory.get_memory
win = win32gui.FindWindow(None, 'Geometry Dash')

clip = mem().get_size()
safety = mem().set_size

currentBruh = mem().get_speed_value()
bruh = mem().set_speed_value


curGrav = mem().gravity
grav = mem().set_gravity

state_left = win32api.GetKeyState(0x53)
state_right = win32api.GetKeyState(0x56)

while True:
     a = win32api.GetKeyState(0x53)
     if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            safety(-15)
            time.sleep(0.02)
            safety(-14)
            time.sleep(0.02)
            safety(-13)
            time.sleep(0.02)
            safety(-12)
            time.sleep(0.02)
            safety(-11)
            time.sleep(0.02)
            safety(-10)
            time.sleep(0.02)
            safety(-9)
            time.sleep(0.02)
            safety(-8)
            time.sleep(0.02)
            safety(-7)
            time.sleep(0.02)
            safety(-6)
            time.sleep(0.02)
            safety(-5)
            time.sleep(0.02)
            safety(-4)
            time.sleep(0.02)
            safety(-3)
            time.sleep(0.02)
            safety(-2)
            time.sleep(0.02)
            safety(-1)
            time.sleep(0.02)
            safety(0)
            time.sleep(0.02)
            safety(1)
            time.sleep(0.02)
            safety(1.1)
            time.sleep(0.0001)
            safety(1.2)
            time.sleep(0.0001)
            safety(1.3)
            time.sleep(0.0001)
            safety(1.4)
            time.sleep(0.0001)
            safety(1.5)
            time.sleep(0.0001)
            safety(1.6)
            time.sleep(0.0001)
            safety(1.7)
            time.sleep(0.0001)
            safety(1.8)
            time.sleep(0.0001)
            safety(1.9)
            time.sleep(0.0001)
            safety(2)
            time.sleep(0.0001)
            safety(1.9)
            time.sleep(0.0001)
            safety(1.8)
            time.sleep(0.0001)
            safety(1.7)
            time.sleep(0.0001)
            safety(1.6)
            time.sleep(0.0001)
            safety(1.5)
            time.sleep(0.0001)
            safety(1.4)
            time.sleep(0.0001)
            safety(1.3)
            time.sleep(0.0001)
            safety(1.2)
            time.sleep(0.0001)
            safety(1.1)
            time.sleep(0.0001)
            safety(1)
            print('Button Pressed')
            time.sleep(0.2)

     b = win32api.GetKeyState(0x56) #Press v to dodge
     if b != state_right:  # Button state changed
             state_right = b
             print(b)
             if b < 0:
               bruh(0.9)
               time.sleep(0.025)
               bruh(0.8)
               time.sleep(0.025)
               bruh(0.7)
               time.sleep(0.025)
               bruh(0.6)
               time.sleep(0.025)
               bruh(0.5)
               time.sleep(0.025)
               bruh(0.4)
               time.sleep(0.025)
               bruh(0.3)
               time.sleep(0.025)
               bruh(0.2)
               time.sleep(0.025)
               bruh(0.1)
               time.sleep(0.025)
               print('Button Pressed')
             else: #ease oback into motion
               bruh(0.2)
               time.sleep(0.025)
               bruh(0.3)
               time.sleep(0.025)
               bruh(0.4)
               time.sleep(0.025)
               bruh(0.5)
               time.sleep(0.025)
               bruh(0.6)
               time.sleep(0.025)
               bruh(0.7)
               time.sleep(0.025)
               bruh(0.8)
               time.sleep(0.025)
               bruh(0.9)
               time.sleep(0.025)
               bruh(1)
               time.sleep(0.025)
               bruh(1)
               time.sleep(0.025)
               grav(1)
               safety(1)
               print('Button Released')




