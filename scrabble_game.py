"""
WORD GAME
Creating a one-player word game similar to Scrabble
February 15, 2025
Anusha Shrestha
"""

import random

# Define constants
vowels = 'aeiou'
not_vowels = 'bcdfghjklmnpqrstvwxyz'
letters_per_hand = 7

# Points for each letter
points_by_letter = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

wordlist_file = "/Users/anustha/Desktop/Python Projects/WORD GAME/words.txt"
# -----------------------------------
# Helper functions
def import_wordlist():
    """
    Imports a list of words from an external file.
    Returns a list of valid words for the game.
    Words are all in lowercase letters.
    """
    print("Loading word list from file...")
    with open(wordlist_file) as f:
        wordlist = [word.lower() for word in f.read().splitlines()]
    print("  ", len(wordlist), "words loaded.") 
    return wordlist

def into_dictionary(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    """
    freq = {}
    for letter in sequence:
        freq[letter] = freq.get(letter, 0) + 1
    return freq

# -----------------------------------
# Problem #1: Scoring a word
def calc_word_score(word, qty):
    """
    Returns the word score after word is validated.
    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all the letters in hand are used.
    """
    score = sum(points_by_letter[letter] for letter in word)
    if len(word) == qty:
        score += 50
    return score

# -----------------------------------
# Problem #2: Update the hand by removing letters
def hand_update(hand, word):
    """
    After a word is played and validated, removes letters in the word from the hand.
    If hand has 2 a's & an 'a' was used, this updates the hand to 1 'a'.
    """
    hand_copy = hand.copy()
    for letter in word:
        if hand_copy.get(letter, 0) > 0:
            hand_copy[letter] -= 1
    return hand_copy

# -----------------------------------
# Problem #3: Test the word validity
def word_is_valid(word, hand, word_list):
    """
    Returns a boolean: True if the word is in the word list and
    can be constructed from the letters in the hand.
    """
    hand_dict = into_dictionary(hand)
    word_dict = into_dictionary(word)

    # Check if word is in the word list
    if word not in word_list:
        return False
    
    # Check if the hand contains all letters in the word
    for letter, count in word_dict.items():
        if hand_dict.get(letter, 0) < count:
            return False

    return True

# -----------------------------------
# Problem #4: Playing hands
def playing_hands(hand, word_list):
    """
    Allows the user to play the given hand, as follows:
    * Hand is shown
    * User can play a word from hand
    * Invalid words are rejected with a message to player to play a different word
    * If valid word, remove letters from hand
    * If valid word scores, add score to total score
    * Total score is shown to player after each valid word is scored
    * Hand is over when no remaining letters
    * User can stop the game by entering a "." instead of a word
    """
    total_score = 0

    while hand:
        # Show the current hand
        show_hand(hand)

        # Ask the user for a word
        word = input("Enter a word (or '.' to stop): ").lower()

        if word == ".":
            print("Game over!")
            break
        
        # Check if the word is valid
        if word_is_valid(word, hand, word_list):
            word_score = calc_word_score(word, letters_per_hand)
            total_score += word_score
            print(f"Word '{word}' is valid! Score: {word_score}, Total score: {total_score}")
            hand = hand_update(hand, word)
        else:
            print("Invalid word! Try again.")

    print(f"Final score: {total_score}")

# -----------------------------------
# Problem #5: Playing the game
def start_game(word_list):
    """
    Allows players an arbitrary number of hands. The user can enter 'n', 'r', or 'e' for:
    * 'n': Start a new random hand
    * 'r': Replay the previous hand
    * 'e': Exit the game
    """
    hand = dealing_hands(letters_per_hand)
    
    while True:
        user_input = input('Enter n to start a new game, r to replay the last hand, or e to end game: ').lower()
        if user_input == 'n':
            hand = dealing_hands(letters_per_hand)
            playing_hands(hand, word_list)
        elif user_input == 'r':
            playing_hands(hand, word_list)
        elif user_input == 'e':
            break
        else:
            print("Invalid input! Please choose 'n', 'r', or 'e'.")

# -----------------------------------
# Helper function to display the hand
def show_hand(hand):
    """
    Prints the letters in the player's hand.
    """
    for letter in hand:
        for _ in range(hand[letter]):
            print(letter, end=" ")
    print()

# Helper function to deal a random hand
def dealing_hands(qty):
    """
    Returns a random hand with qty lowercase letters for hand.
    A third of the letters are vowels.
    """
    hand = {}
    num_vowels = qty // 3
    
    # Collect vowels
    for _ in range(num_vowels):
        letter = vowels[random.randrange(0, len(vowels))]
        hand[letter] = hand.get(letter, 0) + 1

    # Collect consonants
    for _ in range(num_vowels, qty):
        letter = not_vowels[random.randrange(0, len(not_vowels))]
        hand[letter] = hand.get(letter, 0) + 1

    return hand

# Start the game
if __name__ == '__main__':
    word_list = import_wordlist()
    start_game(word_list)

