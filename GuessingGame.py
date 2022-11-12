import random
Answer = random.randint(1,100)
#Game Rules!
print("""Welcome to GuessingGame!
Here are the rules:
-- You will be guessing a number between 1 and 100
-- If the number is -10 of the key it is WARM and +10 will be COLD
-- You win when you guess the right number!
GOOD LUCK!""")
next = True #while loop constraint
GuessList = [0] #records of all the previous  guess
round = 1
while next: 
    currentGuess = int(input("Take a guess:")) #taking a guess as input from player 
    GuessList.append(currentGuess)  #adding current guess to the record 
    print(f"Your guesses so far:{GuessList}")
    if currentGuess < 1 or currentGuess > 100: 
        #validation of guess
        print("OUT OF BOUNDS.")
    if currentGuess == Answer:
        print("Yay! you won!!")
        next = False
        break
    else:
        if round == 1:
            if abs(Answer - currentGuess) <= 10: 
                #if the random number is + or - 10 of the guessed number 
                print("You're either 10 up or 10 down")
                round += 1
            elif abs(Answer - currentGuess) >= 10 :
                print("Too far")
        if  round == 2:
            if abs(Answer - currentGuess) > abs(currentGuess - GuessList[-2]):  
                print("Not even close")
            if abs(Answer - currentGuess) < abs(currentGuess - GuessList[-2]):   
            #if current guess is closer to answer than it is to the previous guess
                print("Almost there!")