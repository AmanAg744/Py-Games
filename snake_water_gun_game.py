# rules snake drinks water,  gun kills snake,  water drowns gun !

import random

def gameWin(comp,you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        elif you=='s':
            print("tie")
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
        elif you=='w':
            print("tie")
    elif comp=='g':
        if you=='w':
            return False
        elif you=='s':
            return True
        elif you=='g':
            print("tie")

print("Computer's Turn : Snake(s) Water (w) or Gun(g)")
randNO = random.randint(1,3)
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

you = input("Player's Turn : Snake(s) Water (w) or Gun(g)")
print(f"comp chose {comp}")
a = gameWin(comp,you)
if a == True:
    print("you win")
elif a == False:
    print("you lose")
