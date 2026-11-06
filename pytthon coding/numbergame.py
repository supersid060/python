import random
playing=True
number=str(random.randint(0,15))
print("i will generate a number from 0 to 9,and you have to guess it one number at a time!")
print("the game will end when you get one hero!")
while playing:
    guess=input("give me your best guess! \n")
    if number == guess:
        print("you win the game!")
        print("the number was:", number)
        break
    else:
        print("your guess isnt quite right, try again \n")
