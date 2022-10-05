# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from operator import truediv
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
            valid = False
            word_in_list = False
            guessed_word = ''

            # Sets guessed_word equal to values contained in Wordle view squares
            for col in range(5):
                guessed_word += str(gw.get_square_letter(gw.get_current_row(),col)).lower()
            print(guessed_word, " vs ", correct_word)

            # Check the word to see if it is in the list
            for dictWord in FIVE_LETTER_WORDS:
                if guessed_word.lower() == dictWord:
                    word_in_list = True
                    valid = True
            
            # Debug
            print("Word is in wordlist: ", word_in_list)

            # check word length
            if len(correct_word) != len(guessed_word):
                gw.show_message("Word must be 5 letters")
                print("Word must be 5 letters")

            # Check if the word was in the list
            elif word_in_list == False:
                gw.show_message("Invalid word")
                print("Invalid word")

            # if the word is 5 letters and in the list
            else: 
                valid = True
                # for each letter in the guessed word
                for guess_count, guess_letter in enumerate(guessed_word):
                    # for each letter in the correct word
                    for target_count, target_letter in enumerate(correct_word):
                        #green
                        if guess_letter == target_letter and guess_count == target_count:
                            gw.set_square_color(gw.get_current_row(), target_count, CORRECT_COLOR)
                            gw.set_square_letter(gw.get_current_row(), target_count, guess_letter.upper())
                        # TODO Make sure that green squares are not overwritten as yellow if
                        # more than one of the same letter appear in word.

                        # yellow
                        elif guess_letter == target_letter:
                            gw.set_square_color(gw.get_current_row(), target_count, PRESENT_COLOR)
                            gw.set_square_letter(gw.get_current_row(), target_count, guess_letter.upper())

                        # grey
                        elif guess_count == target_count:
                            gw.set_square_letter(gw.get_current_row(), target_count, MISSING_COLOR)
                            gw.set_square_letter(gw.get_current_row(), target_count, guess_letter.upper())

            # if the word is invalid, it should not move to the next row.
            if(valid):
                gw.set_current_row(gw.get_current_row()+1)
            else:
                gw.set_current_row(gw.get_current_row())

    gw.add_enter_listener(enter_action) 

   
        

# Startup code
if __name__ == "__main__":
    wordle()
