import random
import math

# config
low = 1
high = 100
limit = math.log(high-low+1,2)
limit = math.ceil(limit)

# helper functions
def show_start_screen():
    print("**************************")
    print("*     Guess a Number!    *")
    print("*     By, Stephen Lee    *")
    print("**************************")

def show_credits():
    print("**************************")
    print("* This awesome game was  *")
    print("* created by Stephen Lee *")
    print("* Thanks to: Coop Dogg   *")
    print("**************************")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print("You have " + str(limit) + " guesses.")
    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("**************************")
        print("     Congratulations!     ")
        print("         You Win!         ")
        print("**************************")
    else:
        print("**************************")
        print("         You lose!        ")
        print("     The Number was: " + str(rand))
        print("**************************")

def play_again():
    while True:
        print("Would you like to play again? (yes/no)")
        decision = input("").lower()
        
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'yes' or 'no'.")

def play():
    guess = -1
    tries = 0

    
    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

