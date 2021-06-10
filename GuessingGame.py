# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# solution

import random

user_input = int(input('Enter a number between 1 and 9: '))

def user_selection(user_input):
    random_num = random.randint(1, 9)
# print(round(random_num))
    while True:   
        if user_input == random_num:
            return(f'Congrats! You guessed correct the random number is {random_num}')
        elif user_input < random_num:
            return(f'Guess Higher, the random number is {random_num}')
        elif user_input > random_num:
            return(f'Guess Lower, the random number is {random_num}')
        break

# calling user_selection(user_input) function
print(user_selection(user_input))