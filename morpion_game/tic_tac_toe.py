# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:34:42 2020

@author: imran
"""


#============imports ================================

from Dé import Dice
from class_morpion_player import MorpionPlayer
#============== GLOBAL VARIABLE =====================

board = ['-','-','-',
        '-','-','-',
        '-','-','-',]
#get the game continue running until it stops
game_still_going = True
power_button = True
# These are my two players for the game, they can have a name, a number(1,2),
# and a symbol(X or O)
player_x = MorpionPlayer()
player_y = MorpionPlayer()
players = [player_x,player_y]



# function which gets the game running
def run_morpion():
    global game_still_going
    global power_button
    while power_button:
        set_game()
        game_still_going = True
        while game_still_going:
            first_player_plays()
            check_game_end()
            if game_still_going == False:
                break
            next_player_plays()
            check_game_end()
        play_another_round()
       
        
        
#function which sets the game on         
def set_game():
    """Sets the whole game on"""
    setting_game = True
    while setting_game == True:
        message = "===Hello everyone the game is starting !====\n"
        message += " Remember that you can quit any time just enter 'q'"
        print(message)
        clean_board()
        get_player_names()
        get_player_numbers()
        display_board()
        setting_game = False
        
        
def get_player_names():
    """Get the name of the players, so we can call them by their name"""
    getting_names = True
    while getting_names == True:
        
        player_x.name = input("Can somebody give me it's name? :")
        player_y.name = input("What is the name of the other player? :")
    
        getting_names = False   
        
def get_player_numbers():
    """Get the number of the player so we can track them during the game"""
    getting_numbers = True
    while getting_numbers == True:
        dice_number_x = player_x.roll_the_dice()
        if dice_number_x =='q':
            break
        dice_number_y = player_y.roll_the_dice()
        if dice_number_y == 'q':
            break
        if (dice_number_x == 0) and (dice_number_y == 0):
            print('guyes lets play seriously please ... ')
            print(' lets reroll')
        elif dice_number_x == dice_number_y:
            print('You rolled the same numbers, we need to roll the dice again! ')
        elif dice_number_x > dice_number_y:
            player_x.number_player = 1
            player_y.number_player = 2
            print(player_x.name.title() + " will start first!")
            getting_numbers = False
        elif dice_number_x < dice_number_y:
            player_x.number_player = 2
            player_y.number_player = 1
            print(player_y.name.title() + " will start first!")
            getting_numbers = False
    get_symbols()
    
def get_symbols():
    """
    Once you have the number of player, it grants each player a symbol
    it can use
    """
    for player in players:
        if player.number_player == 1:
            player.symbol= 'X'
        else:
            player.symbol = 'O'
         
def play_another_round():
    """asks the player if they wanna play an other game, if so launches an other game"""
    global power_button
    next_round = input("Do you guyes wan't to play another round? (yes/no) : ")
    if next_round.strip() == 'yes':
        pass
    else:
        power_button = False

def clean_board():
    """cleans the board for a new game"""
    global board
    board = ['-','-','-',
        '-','-','-',
        '-','-','-',]          


# function which make the player plays

def first_player_plays():
    """Gets the first player to play"""
    for player in players:
        if player.number_player == 1:
            first_player = player
    choose_first_case = True
    print('\n'+ first_player.name.title() + " it's your turn to play !\n")
    while choose_first_case == True:
        first_case = first_player.choose_case()
        
        if board[first_case] == '-':
            board[first_case] = first_player.symbol
            choose_first_case = False
        else:
            print(first_player.name.title() + " you need to choose another case")
            
    display_board()

def next_player_plays():
    """Gets the second player to play"""
    for player in players:
        if player.number_player == 2:
            second_player = player
    choose_next_case = True
    print('\n'+ second_player.name.title() + " it's your turn to play !\n")
    while choose_next_case == True:
        next_case = second_player.choose_case()
        if board[next_case] == '-':
            board[next_case] = second_player.symbol
            choose_next_case = False
        else:
            print(second_player.name.title() + " you need to choose another case")
    
    display_board()

 

def check_game_end():
    """search if there is a winner or a tie, to end the game"""
    check_rows()
    check_columns()
    check_diagonals()
    check_tie()
  


def check_rows():
    """check the rows to find a winner"""
    global game_still_going
    for i in range(0,7,3):
        if board[i] == board[i+1] == board[i+2] != '-':
            print("\n Game ended ! There is a winner! ...")
            if board[i] == player_x.symbol:
                print("\n... and the winner is " + player_x.name.title() + '!')
            if board[i] == player_y.symbol:
                print("\n... and the winner is " + player_y.name.title() + "!")
            game_still_going = False
    return
    
            
def check_columns():
    """check the columns to find a winner"""
    global game_still_going
    for i in range(0,3) :
        if board[i] == board[i+3] == board[i+6] != '-':
            print("\n Game ended ! There is a winner! ...")
            if board[i] == player_x.symbol:
                print("\n... and the winner is " + player_x.name.title() + '!')
            if board[i] == player_y.symbol:
                print("\n... and the winner is " + player_y.name.title() + "!")
            game_still_going = False
    return 

def check_diagonals():
    """check the diagonals to find a winner"""
    global game_still_going
    i = 4
    if (board[i] == board[i-2]  == board[i+2] != '-') or (
            board[i] == board[i-4] == board[i+4] != '-'):
        print("\n Game ended ! There is a winner! ...")
        if board[i] == player_x.symbol:
            print("\n... and the winner is " + player_x.name.title() + '!')
        if board[i] == player_y.symbol:
            print("\n... and the winner is " + player_y.name.title() + "!")
        game_still_going = False
    return
        
def check_tie():
    """checks if the board is full, to find a tie"""
    global game_still_going
    case_filled = 0
    for i in range(9):
        if board[i] != '-':
            case_filled +=1
    if case_filled == 9 and game_still_going:
        print("\n Game is finished ! it's a TIE ! ")
        game_still_going = False
    else:
        pass
            

# function which display the board

def display_board():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    



# Launch the game
run_morpion()


    