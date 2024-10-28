### Part Four -- your code goes here. 
import random
randoml=random.sample(range(1,100),10)
print("Before:",randoml)
randoml2=randoml.copy()
for number in randoml2:
    while number in randoml:
        if number%2==0:
            randoml.remove(number)
        else:
            break
print("After",randoml)


