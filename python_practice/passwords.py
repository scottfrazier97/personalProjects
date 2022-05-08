import string
import random

from numpy import number

#lists of letters, numbers, and special characters
letters = string.ascii_letters
numbers = string.digits
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

#randomizing the potential choices for the passwords
letter_randomizer = random.choices(letters, k = 52)
number_randomizer = random.choices(numbers, k = 10)
special_randomizer = random.choices(special_characters, k = 10)

mixture_no_special = letter_randomizer + number_randomizer
random.shuffle(mixture_no_special)

mixture_special = letter_randomizer + number_randomizer + special_randomizer
random.shuffle(mixture_special)

using = True

while using == True:

    def input_uppercase(question):
        while True:
            try:
                result = input(question)
                result = result.lstrip()
                result = result.rstrip()
                result = result.upper()
                break
            except:
                print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
                continue
        return result

    #Asking user questions regarding their password
    char_count_input = int(input("How many characters do you want your password to be? "))
    print(' - ' * char_count_input)

    special_char_input = str(input_uppercase("Would you like to include special characters (!, @, #, etc.) in your password? Type Y/N: "))
    print(' - ' * char_count_input)

    while True:
        if special_char_input in ('N', 'NO', 'Y', 'YES'):
            break
        else:
            print('Answer not accepted. Please try again by typing Y or N.')
            break

    if special_char_input in ('Y', 'YES'):
        special_char_prompt = True
    elif special_char_input in ('N', 'NO'):
        special_char_prompt = False
    else:
        print('Something is brokey. Try again.')
        break

    if special_char_prompt:
        special_pw = mixture_special[:char_count_input]
        print(''.join(special_pw))
    else:
        no_special_pw = mixture_no_special[:char_count_input]
        print(''.join(no_special_pw))
   
    while True:
        satisfied_prompt = str(input_uppercase("Are you happy with your password? Type Y/N: "))
        print(' - ' * char_count_input)
        if satisfied_prompt in ('Y', 'YES'):
            using = False
            print("Thank you! Have a nice day.")
            break
        elif satisfied_prompt in ('N', 'NO'):
            break
        else:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue
