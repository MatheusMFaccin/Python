from coffe import Coffe,Espresso

coffeetype = input("if you want make your coffee write 1. if you want espresso write 2")

if(coffeetype == "1"):
    howmany = input("how many coffee you want ? ")
    milk = input("how much milk you want ? ")
    warter = input("how much warter you want ? ")
    coffe = Coffe(howmany,milk,warter)
    print(coffe.howmany)
    print(coffe.milk)
    print(coffe.water)

if(coffeetype == "2"):
    espresso = Espresso()
    print(espresso.howmany)
    print(espresso.milk)
    print(espresso.water)



