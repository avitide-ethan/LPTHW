# Guess the number game
import random


secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

for guessCount in range(0, 6):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Too low")
    elif guess > secretNumber:
        print("Too high")
    else:
        break

if guess==secretNumber:
    print("Good job, you guessed the number in {} guesses!".format(guessCount))
else:
    print("Sorry, you exhausted your guesses. I was thinking of {}".format(secretNumber))

