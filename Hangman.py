import random
import string

from words import words

def valid_words(words):
    word = random.choice(words)
    return word

def hangman():
 word = valid_words(words)
 word_letter = set(word)
 alphabet = set(string.ascii_uppercase)
 used_letters = set()

 while len(word_letter) > 0:
    
    user_input = input("Enter a letter: ").upper()
    if user_input in alphabet - used_letters:
        used_letters.add(user_input)
        if user_input in word_letter:
            word_letter.remove(user_input)
    elif user_input in used_letters:
        print("You have already used that letter")

    else:
        print("Invalid character")

    print('You have used the letters ', ' '.join(used_letters))
    
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word:' ' '.join(word_list))

hangman()






