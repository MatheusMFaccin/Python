from pickle import TRUE
from secrets import choice
import threading 
import asyncio
import time


import random


async def computerChoice(computer):
    choices = ['pedra','papel','tesoura']
    
    computer = await random.choice(choices)

    print(computer)
    

async def game(rounds):
    computer1 = ""

    computer2 = ""

    i = 0


    pointsPlayer = 0
    pointsComputer = 0
    while i<=rounds: 
        thread1 =  threading.Thread(target=computerChoice, args=(computer1,))
        thread1.start()
        thread1.join()
        thread2 =   threading.Thread(target=computerChoice, args=(computer2,))
        thread2.start()
        thread2.join()  
        print(computer1)
        print(computer2)
        if computer1 == computer2:
                print("empate")
        if computer2 == "pedra" :
            if computer1  == "papel" :
                print("computador2 ganhou")
                pointsComputer+=1
            elif computer1 == "tesoura":
                print("computador1 ganhou")
                pointsPlayer+=1
        if computer2 == "papel" :
            if computer1 == "tesoura" :
                print("computador1 ganhou")
            elif computer1 == "pedra":
                print("computador2 ganhou")
        if computer2 == "tesoura" :
            if computer1 == "pedra" :
                print("computador1 ganhou")
            elif computer1 == "papper":
                print("computador2 ganhou")
        i+=1

rounds = int(input("digite o numero de rodadas "))
asyncio.run(game(rounds))

