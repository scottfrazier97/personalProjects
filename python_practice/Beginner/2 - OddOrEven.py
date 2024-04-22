#Ask the user for a number. Depending on whether the number is 
#even or odd, print out an appropriate message to the user.

user_number = int(input('Input a number: '))

if user_number % 2 == 0:
    print("Even")
elif user_number % 1 == 0:
    print("Odd")
else:
    print("Something is wrong.")