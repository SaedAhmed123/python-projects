import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("print a number greater than 0")
        quit()
else:
    print("Type a number greater than 0")
    quit()
