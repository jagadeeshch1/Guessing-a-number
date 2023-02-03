import random
def guess(x,name):
    random_number=random.randint(1,x)
    guess=0
    count=0
    while guess!=random_number:
        count+=1
        guess=int(input(f" guess a number from 1 to {x}:"))
        if guess>random_number and guess<=x:
            print("you have enterd a high value")
        elif guess<random_number and guess>0:
            print("you have enterd a low value")
        elif guess==random_number:
            print("yay congracts")
            print(f"{name} have guessed in {count} no.of attempts")
        else:
            print("guess the numbrer in the correct range ")
name=input("enter the name of player:")
y=int(input("enter the upper bound to fix for playing this game:"))      
guess(y,name)
            




