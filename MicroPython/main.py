"""
Created by: Pablo
Created on: Sep 2024
This module is a Micro:bit MicroPython program show are and perimeter formulas
"""

from microbit import *
from time import sleep


display.clear()
sleep(1)


""" perimeter """
display.scroll("5 * 2 + 3 * 2 =" +str(5 * 2 + 3 * 2))
sleep(0.5)
display.clear()



"""area"""
display.scroll("5 * 3 =" +str(5 * 3))
sleep(0.5)
display.clear()
