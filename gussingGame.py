from random import randint
n=int(input("Enter how many times  do you want to play: "))
for i in range(n):
    gussNumber = int(input("Enter your guss between 1 to 5 : "))
    randomNumber = randint(1, 5)
    if gussNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was ", randomNumber)
