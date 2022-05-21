from pickle import TRUE
from secrets import choice



import random
choices = ['rock','papper','scissors']


playerchoice = None

computer = random.choice(choices)
while(playerchoice not in choices):
    playerchoice = input("rock papper or scissor ? ").lower()
        
    print(computer)
    if playerchoice == computer:
            print("empate")

    if playerchoice == "rock" :
        if computer == "papper" :
            print("computer win")
        elif computer == "scissors":
            print("player win")
    
    if playerchoice == "papper" :
        if computer == "scissors" :
            print("computer win")
        elif computer == "rock":
            print("player win")
    if playerchoice == "scissors" :
        if computer == "rock" :
            print("computer win")
        elif computer == "papper":
            print("player win")
                       
