# Created by Animesh Patel on 05/05/19.
# Copyright @ 2019 Animesh Patel. All rights reserved.
# Title: A two player tic tac toe game in Python 3.

from random import *

def display_board(board):
    # to display the updated board with certain spacing
    print (' ' * 5000)
    #os.system('cls')
    print (board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print (board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print (board[1] + '|' + board[2] + '|' +board[3])

def who_goes_first():
    x = randint(0,1)
    if (x == 0):
        return (x + 1, x + 2) # player 1, player 2
    else:
        return (x + 1, x)  # player 2, player 1

first, second = who_goes_first()  # player 1 and 2 turns

# takes in the player input 'X' or 'O'
def player_input():
    marker = ''

    while True:
        marker = input('Player ' + str(first) + ' choose X or O: ').upper()
        
        if marker not in ['X','O']:
            print("try again")
            continue
        
        if 'X' in marker:
            player1 = marker
            return ('X','O')
        elif 'O' in marker:
            player1 = marker
            return ('O','X')

board = ['k','a','a','a','a','a','a','a','a','a']

def rules_for_valid_input(sign, player):
    while True:
        
        # check for the integer value
        try:
            user_inp = int(input('Player {} please enter a valid input (0 to 9) for your {}: '.format(player,sign)))
        except ValueError:
            print ('Invalid value, please input only digits')
            continue
    
        # check if the user choice is between 1 to 9 inclusive
        if user_inp not in range(1,10):
            print ('The value must be between 1 and 9 (inclusive)')
        
        # check if the board space is already taken
        elif board[user_inp] != 'a':
            print ('User must select an empty space')

        else:
            return user_inp

def rules_for_win(board, player, player_sign):
    """ This function determines if any of the player has won """
    if ((board[7] == board[8] == board[9] == player_sign) or (board[7] ==  board[4] == board[1] == player_sign)
    or (board[7] == board[5] == board[3] == player_sign) or (board[8] ==  board[5] == board[2] == player_sign)
    or (board[9] == board[6] ==  board[3] == player_sign) or (board[9] == board[5] == board[1] == player_sign)
    or (board[4] ==  board[5] ==  board[6] == player_sign) or (board[1] == board[2] == board[3] == player_sign)):
        print('Player {} won'.format(player))
        return True
    return False

def rules_for_tie(board):
    """ This function determines if the game is a tie """
    if 'a' not in board:
        print("It's a tie")
        return True
    return False

def game_on():
    """ This function takes care of when the game is over """
    sign1, sign2 = player_input()  # to retrive players selection player_input() # sets 'X' and 'O' for player 1 and 2 for the first time
    won = False
    tie = False
    
    # for determining right player's turn
    count = 1
    
    # loop runs until it's a tie or someone wins
    while not (won or tie):
        if count % 2 == 1:
            player_turn, player_sign = first, sign1
        else:
            player_turn, player_sign = second, sign2

        user_inp = rules_for_valid_input(player_sign, player_turn)
        # enter the input to board
        board[user_inp] = player_sign
        
        # display the board
        display_board(board)
        
        won = rules_for_win(board,player_turn, player_sign)
        tie = rules_for_tie(board)
        count += 1
game_on()
