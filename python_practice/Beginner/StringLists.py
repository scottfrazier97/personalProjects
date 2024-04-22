#Checking for palindromes

running = True
while running == True:
    
    user_input = str(input("Type a word. Maybe try a palindrome: ")).upper()

    if user_input == user_input[::-1]:
        print("Valid Palindrome")
    else:
        print("Not a valid palindrome")

    while True:
        satisfied_prompt = str(input("Would you like to run again? ")).upper()
        if satisfied_prompt in ('N', 'NO'):    # If yes, loops will break, ending the program.
            running = False
            print("Thank you! Have a nice day.")
            break
        elif satisfied_prompt in ('Y', 'YES'):   # If no, loops break and restart outer most while loop. Effectively restarting the program.
            break
        else:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue

