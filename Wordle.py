# File: Wordle.py
"""
This file handles the logic of the program for the wordle game
Project Team: Benjamin Schneider, Dallin Stirling, Jared Christensen, Spencer Walker, Stephen Williams
"""
#import functions/packages
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

# main function
def wordle():

  # Get a random word from the list of words in the word dictionary
  correct_word = random.choice(FIVE_LETTER_WORDS)
  
  # display word in first row - Milestone 1 - commented out for final program
  # for i, c in enumerate(correct_word):
  #     gw.set_square_letter(0,i,c)
  
  gw = WordleGWindow()

  #when user presses enter, this function runs:
  def enter_action(s):
    #initialize vars for next guess
    valid = False
    word_in_list = False
    guessed_word = ''
    #array to keep track of which letters were already used in guess letter coloring
    correct_word_array = [0, 0, 0, 0, 0]

    # Sets guessed_word equal to values contained in Wordle view squares
    for col in range(5):
      guessed_word += str(gw.get_square_letter(gw.get_current_row(),col)).lower()
  
    # Check the word to see if it is in the list
    for dictWord in FIVE_LETTER_WORDS:
      if guessed_word.lower() == dictWord:
        word_in_list = True
        valid = True

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

      #loop for finding letters in correct spot
      # for each letter in the guessed word
      for guess_count, guess_letter in enumerate(guessed_word):
        # for each letter in the correct word
        for target_count, target_letter in enumerate(correct_word):
          #if in correct spot, change color to green for letter and keyboard key
          if guess_letter == target_letter and guess_count == target_count:
            gw.set_square_color(gw.get_current_row(), guess_count,CORRECT_COLOR)
            correct_word_array[target_count] = 1
            gw.set_key_color(guess_letter.upper(), CORRECT_COLOR)

      #loop for finding letters in wrong spot and absent letters
      #for each letter in guessed word
      for guess_count, guess_letter in enumerate(guessed_word):
        #check if letter is already colored green. If so, skip.
        if gw.get_square_color(gw.get_current_row(),guess_count) != CORRECT_COLOR:
          #for each letter in correct word
          for target_count, target_letter in enumerate(correct_word):
            #check if letter is in word, but in wrong spot
            if guess_letter == target_letter and guess_count != target_count:
              #check if the letter in the correct word has already been used for another letter in guessed word using correct word array
              if correct_word_array[target_count] == 0:
                #change color to yellow if all conditions met
                gw.set_square_color(gw.get_current_row(), guess_count,PRESENT_COLOR)
                #mark letter in correct word array as used for guess in this row
                correct_word_array[target_count] = 1

                #check if keyboard key color is already green
                if gw.get_key_color(guess_letter.upper()) != CORRECT_COLOR:
                  #if not green, make it yellow
                  gw.set_key_color(guess_letter.upper(), PRESENT_COLOR)
                #break loop to avoid recoloring letter gray in next loop
                break

            #if letter not present in word, color gray
            else:
              gw.set_square_color(gw.get_current_row(), guess_count,MISSING_COLOR)
              # check if keyboard key color is green or yellow
              if gw.get_key_color(guess_letter.upper()) != CORRECT_COLOR and gw.get_key_color(guess_letter.upper()) != PRESENT_COLOR:
                #if not already green or yellow, make gray
                gw.set_key_color(guess_letter.upper(), MISSING_COLOR)
                      
    # if the word is invalid, it should not move to the next row.

    #victory/failure messages
    #if correct
    if (correct_word == guessed_word):
      gw.show_message("VICTORY")
    #if final guess is incorrect
    elif (gw.get_current_row() == 5 and valid):
      gw.show_message("You failed. The correct word was " + correct_word + ".")
    #if incorrect, but they still have more guesses, move on to next row
    elif (valid):
      gw.set_current_row(gw.get_current_row() + 1)
    #if word is invalid, return to current row for user to enter a valid row
    else:
      gw.set_current_row(gw.get_current_row())      

  #add listener for user pressing enter
  gw.add_enter_listener(enter_action)

# Startup code for replit environment
if __name__ == "__main__":
  wordle()
