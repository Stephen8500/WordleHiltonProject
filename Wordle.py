# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS,CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR



def wordle():

    # Get a random word from the list of words in the word dictionary
    correct_word = random.choice(FIVE_LETTER_WORDS)
    print(correct_word)
    

    # display word in first row - Milestone 1
    # for i, c in enumerate(correct_word):
    #     gw.set_square_letter(0,i,c)   

    gw = WordleGWindow()
    
    def enter_action(s):
            
            word_in_list = False
            guessed_word = ''
            # Sets guessed_word equal to values contained in Wordle view squares
            for col in range(5):
                guessed_word += str(gw.get_square_letter(gw.get_current_row(),col)).lower()
            print(guessed_word)

            # check if the guessed word is in the word list
            if check_the_guess(correct_word, guessed_word) == correct_word.upper():
                print("You win")

            gw.set_current_row(gw.get_current_row()+1)
    gw.add_enter_listener(enter_action) 

    def check_the_guess(correct_word, guessed_word):
        print("in the func: ", correct_word, " ", guessed_word)
        for dictWord in FIVE_LETTER_WORDS:
            if guessed_word.lower() == dictWord:
                word_in_list = True
            else:
                word_in_list = False
        if len(correct_word) != len(guessed_word):
            gw.show_message("Word must be 5 letters")
        elif word_in_list == False:
            gw.show_message("Invalid word")
        else: 
            # Enumerate creates an object which contains each character in
            # given string along with a counter for each character.
            for guess_count, guess_letter in enumerate(guessed_word):
                for target_count, target_letter in enumerate(correct_word):
                    if guess_letter == target_letter and guess_count == target_count:
                        gw.set_square_color(gw.get_current_row(), target_count, CORRECT_COLOR)
                        gw.set_square_letter(gw.get_current_row(), target_count, guess_letter)
                    # TODO Make sure that green squares are not overwritten as yellow if
                    # more than one of the same letter appear in word.
                    elif guess_letter == target_letter:
                        gw.set_square_color(gw.get_current_row(), target_count, PRESENT_COLOR)
                        gw.set_square_letter(gw.get_current_row(), target_count, guess_letter)
                    elif guess_count == target_count:
                        gw.set_square_letter(gw.get_current_row(), target_count, MISSING_COLOR)
                        gw.set_square_letter(gw.get_current_row(), target_count, guess_letter)
            gw.set_current_row(gw.get_current_row() + 1)
            
            # TODO Check if word is in Dictionary file
            
            return (guessed_word.upper())
        # TODO figure out why this function is automatically getting called
        # before ever pressing the enter key in Wordle view

# Startup code
if __name__ == "__main__":
    wordle()
