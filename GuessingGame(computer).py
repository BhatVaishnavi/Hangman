import random
def comp_guess(n):
    upper = n
    lower = 0
    guess = 0
    validation = ''
    guess_lst = []
    while validation != 'c':
        guess = random.randint(lower , upper)
        if guess not in guess_lst:
            guess_lst.append(guess)
            validation = input(f"Is the number {guess} correct('c') or too high?('h') or too low('l')?")
            if validation == 'l':
                lower = guess
            if validation == 'h':
                upper = guess
    else:
        print(f"yay! we guessed your number correctly it is {guess}")

comp_guess(100)