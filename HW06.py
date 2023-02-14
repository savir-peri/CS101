#Task1
import random
number = random.randint(1, 20)
numGuesses = 6
while numGuesses > 0:
  guess = input("What is a number between 1 and 20?")
  guess = int(guess)
if guess