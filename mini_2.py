#Radhe Radhe 
#This is a game of random scores

import random

def guess_game():
    print("You are now playing this game!!")
    score=random.randint(1,100)

    file=open("highscore.txt","r+")
    highscore=file.read()

    if(highscore!=""):
        highscore=int(highscore)
    else:
        highscore=0

    print(f"Your Score:{score}")
    if(score>highscore):
        file.seek(0)
        file.write(str(score))
        file.truncate()
        print("Yayyy! You got a new High Score!")
        print(".................................")
    
    else:
        print("Good Score!")
    return score
     

    file.close()

choice='y'
while(choice=='y'):
    guess_game()

    choices=random.choice(["Wanna Play Again?","What  about another match!","One more shot?"])
    print(choices)

    choice=input("y/n:")
    if(choice=='y'):
        continue
    else:
        break