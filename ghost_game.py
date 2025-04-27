"""
WORD GAME
Creating a two-player word Ghost Game
February 15, 2025
Anusha Shrestha
"""
import random

# Define constants
vowels = 'aeiou'
not_vowels = 'bcdfghjklmnpqrstvwxyz'

wordlist_file = "words.txt"  # Path to the wordlist file

# Helper functions
def import_wordlist():
    """
    Imports a list of words from an external file.
    Returns a list of valid words for the game.
    Words are all in lowercase letters.
    """
    print("Loading word list from file...")
    try:
        with open(wordlist_file) as f:
            wordlist = [word.lower() for word in f.read().splitlines()]
        print("  ", len(wordlist), "words loaded.") 
    except FileNotFoundError:
        print("Error: wordlist file not found.")
        return []
    return wordlist

def is_valid_word(word, word_list):
    """
    Returns True if the word is a valid word in the word list.
    """
    return word in word_list

def is_valid_prefix(fragment, word_list):
    """
    Returns True if the fragment is a valid prefix for any word in the word list.
    """
    for word in word_list:
        if word.startswith(fragment):
            return True
    return False

def ghost_game(word_list):
    """
    Implements the two-player Ghost game.
    Players alternate adding one letter to a growing word fragment.
    The game ends if a player forms a valid word or no valid word can be formed from the fragment.
    """
    fragment = ""
    current_player = 1  # Player 1 starts
    
    while True:
        print(f"\nCurrent word fragment: '{fragment}'")
        
        # Check if the current fragment is a valid word of length 4 or more
        if len(fragment) >= 4 and is_valid_word(fragment, word_list):
            print(f"'{fragment}' is a word! Player {1 if current_player == 1 else 2} wins.")
            break
        
        # Check if no valid word can be formed from the current fragment
        if not is_valid_prefix(fragment, word_list):
            print(f"Player {current_player} wins! No valid word can be formed from the fragment '{fragment}'.")
            break
        
        # Get the player's input
        letter = input(f"Player {current_player}, enter a letter: ").lower()
        
        # Validate the input
        if len(letter) != 1 or letter not in vowels + not_vowels:
            print("Invalid input! Please enter a single letter.")
            continue
        
        # Update the fragment
        fragment += letter
        
        # Switch players
        current_player = 2 if current_player == 1 else 1

# Start the game
if __name__ == '__main__':
    word_list = import_wordlist()  # Load the word list from file
    if word_list:  # Only start the game if the word list is successfully loaded
        ghost_game(word_list)
