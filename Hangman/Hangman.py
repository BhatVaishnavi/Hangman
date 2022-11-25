import random
from words import words_list
from hangman_visual import lives_visual_dict
import math

def get_valid_words(any_list):
    word = random.choice(any_list) #picks a random word from the list of words in words.py

    return word.upper()


def hangman():
    word = get_valid_words(words_list)
    word_letters = set(word) #a set of the alphabets of the chosen word , sets can only hold unique values
    used_letters = set() #empty set to hold and later display all of the previously guessed alphabets

    lives = math.ceil(len(word)*1.5) #player gets 1.5 times the number of letters to be guessed

    #getting user input
    print("Welcome to Hangman! The word you have to guess has" , len(word), "letters")
    while len(word_letters) > 0 and lives > 0:
        print('You have' , lives , 'lives left and you have used these letters:' , ' '.join(used_letters))
        user_letter = input('Guess a letter:').upper()
        

        if user_letter in word_letters:
                word_letters.remove(user_letter)       #when a letter is guessed correctly the letter is removed from the set of letters from the word
                print('You guessed the right letter!')                                       #a set is used so that the user doesn't have to guess the same letter twice incase the letter has multiple occurences within the word
               
        else:
            lives = lives - 1
            print('Your letter,' , user_letter , 'is not in the word')
        if user_letter not in used_letters:
            used_letters.add(user_letter)


        elif user_letter in used_letters:
            print('Guess something else')


        else:
            print('That is not a valid letter')

        word_list = [letter if letter in used_letters else '_' for letter in word]     
        try:
            print(lives_visual_dict[lives]) #the dictionary for hangman visual only goes up to 7 if there are more than 7 lives(if there are more 4 letters there will be more than 7 lives) then the visual will not be displayed at all
        except:
            pass
        
        print('Current word:' , ' '.join(word_list))
        print()
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died , sorry :( The word was:', word)

    else:
        print('Yay you guessed the word', word)


if __name__ == '__main__':
    hangman()

