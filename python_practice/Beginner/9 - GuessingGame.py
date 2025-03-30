#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether 
#they guessed too low, too high, or exactly right.

import random

count = 0
while True:
    random_num = random.choice(range(0,10))
    user_guess = input("Guess a number, or type exit: ")
    count += 1

    if user_guess.lower() == 'exit':
        print(f"Total number of guesses: {count-1}")
        break
    elif int(user_guess) == random_num:
        print("Correct guess!")
        continue
    elif int(user_guess) > random_num:
        print("User guess too high!")
        continue
    elif int(user_guess) < random_num:
        print("User guess too low!")
        continue
    else:
        print("Something is wrong")