# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random


secret_number  = 0
chosen_range = 0
guess_count = 7

# helper function to start and restart the game
def new_game(chosen_range):
    global secret_number
    global guess_count
    if chosen_range == 0 or chosen_range == 100:
        print "Starting new game with range from 0 to 100"
        print "You have 7 guesses \n"
        guess_count = 7
        secret_number = range100()
    elif chosen_range == 1000:
        guess_count = 10
        secret_number = range1000()
        print "Starting new game with range from 0 to 1000"
        print "You have 10 guesses \n"
    else:
        print "Error! No such range"


# define event handlers for control panel
def range100():
    return random.randrange(0,100)

def range1000():
    return random.randrange(0,1000)

def input_guess(guess):
    global secret_number
    global guess_count
    guess_count -=1
    print "Guess was " + str(guess)
    if int(guess) < secret_number:
        print "Higher! You have " + str(guess_count) + " guesses remaining \n"
    if int(guess) > secret_number:
        print "Lower! You have " + str(guess_count) + " guesses remaining \n"
    elif int(guess) == secret_number:
        print "Correct!!! You got it with " + str(guess_count) + " guesses left \n"
        new_game(0)


def button_100_handler():
    global guess_count
    guess_count = 7
    new_game(100)
    
def button_1000_handler():
    global guess_count
    guess_count = 10
    new_game(1000)
    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
button100 = frame.add_button('Range is 0 - 100', button_100_handler, 200)
button1000 = frame.add_button('Range is 0 - 1000', button_1000_handler, 200)
user_guess = frame.add_input('Your guess ', input_guess, 50)
new_game(0)


