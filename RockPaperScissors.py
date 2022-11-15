import random

p_score = 0
o_score = 0
def play():
        n = int(input("Choose number of rounds (max 5):"))
        game_play(n)
        win_check(p_score , o_score)


        

def game_play(n):
    global p_score , o_score
    round = 0
    while round < n:
        player = input("Choose 'S' for stone 'P' for paper or 'X' for scissor: '").upper()
        opponent = random.choice(['S','P','X'])
        if player == opponent:
            print(f"computer chose {opponent}, Tie!")

        elif (player == 'S' and opponent == 'X') or (player == 'P' and opponent== 'S')  or (player == 'X' and opponent== 'P') :
            print(f"computer chose {opponent}, You win!")
            p_score +=1
        else:
            print(f"computer chose {opponent} , you lose :(")
            o_score +=1
    
        round +=1
    return(p_score , o_score)
    


def win_check(p_score , o_score):
    print(p_score , o_score)
    if p_score == o_score:
        print("it's a tie")
    elif p_score > o_score:
        print("you win yay")
    else:
        print("you lose ouch")
play()


