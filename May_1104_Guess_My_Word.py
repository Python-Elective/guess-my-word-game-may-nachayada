# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
# collaborated with chuck

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    
    for char in secret_word:
      if char not in letters_guessed:
        return False
    return True

# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))

def get_guessed_word(secret_word, letters_guessed):
   
    output = ''

    for char in secret_word:
      if char in letters_guessed:
        output = output + char
      else:
        output = output +  '  '
    return output

# print(get_guessed_word('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])) 
# print(get_guessed_word('pineapple', []))

def is_letter_in_word(secret_word, letter_guessed):
    """
    secret_word: string, the word the user is guessing
    letter_guessed: the current letter the user typed in to guess
    returns: boolean, True if the letter_guessed matches at least 1 letter in secret_word;
    False otherwise
    """
    for character in secret_word:
        if character.lower() == letter_guessed.lower():
              return True
        else:
           return False
        
print(is_letter_in_word('Neko', ('O')))