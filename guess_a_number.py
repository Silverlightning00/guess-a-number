import random

# config
low = 1
high = 100
limit = 10

# start game
rand = random.randint(low,high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");
print("You have " + str(limit) + " tries.")

guess = -1
tries = 0

# Helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number")

# play game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

# tell the outcome
if guess == rand:
    print("You win!")

else:
    print("You lose! The number was " + str(rand) + ".")
