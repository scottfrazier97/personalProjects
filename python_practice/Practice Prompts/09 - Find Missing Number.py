# Given a list of numbers from 1 to n with one missing, return the missing number.
import random

def missing_numbers():

    number_range = range(1, 11)
    number_list = list(number_range)

    num_to_remove = random.choice(number_list)
    number_list.remove(num_to_remove)

    counter = 1

    print(number_list)
    for n in number_list:

        if n == counter:
            counter += 1
        else:
            print(f"Missing: {counter}")
            break

missing_numbers()