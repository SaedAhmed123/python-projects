import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Print a number greater than 0")
        quit()
else:
    print("Type a number greater than 0")
    quit()

random_integer = (random.randrange(0,top_of_range))
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == random_integer:
        print("Congratulations, You got it right!")
        break
    elif user_guess < random_integer:
        print("You were below the number ")
    else:
        print("You were above the number")

print("You got it in", guesses, "guesses")
    
