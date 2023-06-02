# Random Number

# import random                                    # For random numbers library
from random import randint  # only for randint libary

for i in range (1,11):
    guess = int(input("Enter your guess number: "))
    random = randint(1,10)
    # random = random.randint(1,10)                    # For small numbers of random numbers
    # random = random.random()*100                     # For large numbers of random numbers
    if guess == random:
        print ("You Won!!")
    else:
        print ("Opps!! Better luck next time!")
        print ("Random Number was: ",random)
