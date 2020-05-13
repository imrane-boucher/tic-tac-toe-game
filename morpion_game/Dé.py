# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:05:42 2020

@author: imran
"""

from random import randint

class Dice():
    """Simulates the features of a Dice"""
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_dice(self):
        """Display the result of a dice-roll"""
        return randint(1,self.sides)

