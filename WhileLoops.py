### Part Two -- your code goes here. 
import random 
x=random.randint(1,100)
y=False
while y==False:
    userx=int(input("PLease Guess a number between 1 and 100"))
    if userx==x:
        y=True 
        print("Well done, you guessed correctly.")
    elif userx!=x or userx<1 or userx>100:
        print("Please try again to guess the correct number between 1 and 100")
    
