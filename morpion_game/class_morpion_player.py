# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:59:05 2020

@author: imran
"""
from Dé import Dice


# class which model our tic_tac_toe players 
class MorpionPlayer():
    """Model a ""tic tac toe" player, and sets the action he/she can do"""
    
    def __init__(self,name='',number_player='',symbol=''):
        self.name = name
        self.number_player = number_player 
        self.symbol = symbol
        self.dice_score = 0
        
    def roll_the_dice(self):
        """
        Ask the player to roll the dice to see who goes first,
        it will aslo help to set each players number
        """
        response = input(self.name.title() +
                         " Are you ready to roll the dice? (yes/no)")
        my_dice = Dice()
        if response.strip() == 'yes':
            self.dice_score = my_dice.roll_dice()
            print(self.name.title() + ' you rolled a : ' + str(self.dice_score))
        elif response.strip == 'q':
            self.dice_score = 'q'
        else:
            print("Too bad you're starting second ")
            self.dice_score = 0
        return self.dice_score    

    def choose_case(self):
        """Enables the player to choose a case on the board to fill"""
        case = input(self.name.title() + 
                     " which case do you want to choose? (from 1 to 9): ")
        try:
            case = int(case) -1
        except ValueError:
            print('Enter a number please !')
        
        return case 
    
    def play_another_round(self):
        """The player can choose if we wants to play another round""" 
        another_round = input(self.name.title() + 
                              ' do you want to play another round ? (yes/no) :')
        return another_round
