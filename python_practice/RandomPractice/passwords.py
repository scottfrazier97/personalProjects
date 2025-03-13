import string
import random

letters = string.ascii_letters
numbers = string.digits
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

using = True
while using == True:
    
    # Randomizing the potential choices for the passwords. 'k = n' is required to tell variables to grab all potential characters in the respective list.
    letter_randomizer = random.choices(letters, k = 52)
    number_randomizer = random.choices(numbers, k = 10)
    special_randomizer = random.choices(special_characters, k = 10)

    # Concatenating letter and number lists withOUT special characters, then shuffling.
    mixture_no_special = letter_randomizer + number_randomizer
    random.shuffle(mixture_no_special)

    # Concatenating letter and number lists WITH special characters, then shuffling.
    mixture_special = letter_randomizer + number_randomizer + special_randomizer
    random.shuffle(mixture_special)

    # Function for converting all user inputs to uppercase. Insures that inputs will not be denied for casing.
    def input_uppercase(question):
        while True:
            try:
                result = input(question)
                result = result.strip()
                result = result.upper()
                break
            except:
                print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
                continue
        return result

    # Asking user questions regarding their password
    char_count_input = int(input("How many characters do you want your password to be? "))
    
    def dashed_lines():
        print(' - ' * char_count_input)

    special_char_input = str(input_uppercase("Would you like to include special characters (!, @, #, etc.) in your password? Type Y/N: "))
    dashed_lines()

    if special_char_input in ('Y', 'YES'):
        special_char_prompt = True
    elif special_char_input in ('N', 'NO'):
        special_char_prompt = False
    else:
        print('Something is broken. Try again.')
        break

    # Removes all extra list characters from the returned items.
    if special_char_prompt:
        special_pw = mixture_special[:char_count_input]
        print(f'Here is your password: \n{"".join(special_pw)}')
    else:
        no_special_pw = mixture_no_special[:char_count_input]
        print(f'Here is your password: \n{"".join(no_special_pw)}')

   # Asking the user if they are satisfied
    while True:
        dashed_lines()
        
        satisfied_prompt = str(input_uppercase("Are you happy with your password? Type Y/N: "))
        if satisfied_prompt in ('Y', 'YES'):    # If yes, loops will break, ending the program.
            using = False
            print("Thank you! Have a nice day.")
            break
        elif satisfied_prompt in ('N', 'NO'):   # If no, loops break and restart outer most while loop. Effectively restarting the program.
            break
        else:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue
