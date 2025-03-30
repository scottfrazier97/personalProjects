#Checking for palindromes

while True:
    user_input = input("Type a word. Maybe try a palindrome: ").lower()

    if user_input == user_input[::-1]:
        print("Valid Palindrome")
    else:
        print("Not a valid palindrome")

    satisfied_prompt = input("Would you like to run again? (Y/N): ").strip().upper()
    if satisfied_prompt in ('N', 'NO'):
        print("Thank you! Have a nice day.")
        break
    elif satisfied_prompt not in ('Y', 'YES'):
        print("Invalid input. Exiting program.")
        break
