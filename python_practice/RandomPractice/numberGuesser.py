from random import randrange

play = True
correctCounter = 0
playCounter = 0

def dashes():
    print("=================================")

computer_choice = randrange(5)

while play: 
    userPrompt = int(input("Choose a number between 0 and 5: "))
    dashes()
    if userPrompt == computer_choice:
        correctCounter += 1
        playCounter += 1
        print(f"You guessed correctly! You and the computer both chose the number: {computer_choice}. Well done!")
    elif userPrompt != computer_choice:
        playCounter += 1
        print(f"Sorry! you guessed incorrectly. The computer chose the number: {computer_choice}.")
    else: 
        print("I do not understand, input a valid number (0-10).")

    dashes()

    print(f"STATS:\nYou have correctly guessed the number {correctCounter} time(s), with a total guess count of {playCounter}.")
    
    win_calculation = round((correctCounter / playCounter) * 100, 1)
    print(f"This brings your win percentage to: {win_calculation}%")
    
    dashes()
    
    again = str(input("Do you want to play again? Type yes or no: "))
    dashes()
    if again not in ('yes', 'YES', 'Yes', 'y', 'Y'):
      break