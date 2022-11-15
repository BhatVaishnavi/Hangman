import random
def play():
    round = 0
    while round < 5:
        u_choice = input("Choose 'S' for stone 'P' for paper or 'X' for scissor: '").upper()
        c_choice = random.choice(['S','P','X'])
        game_play(u_choice , c_choice)
        
        round +=1
    


        

def game_play(player , opponent):
    if player == opponent:
        print(f"computer chose {opponent}, Tie!")

    elif (player == 'S' and opponent == 'X') or (player == 'P' and opponent== 'S')  or (player == 'X' and opponent== 'P') :
        print(f"computer chose {opponent}, You win!")

    else:
        print(f"computer chose {opponent} , you lose :(")


def win_check(p_score , o_score):
    if p_score == o_score:
        return "It's a tie"
    if p_score > o_score:
        return "You win the game!"
    else:
        return "Computer wins"

play()
