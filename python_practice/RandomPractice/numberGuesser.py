from random import randrange

play = True
correctCounter = 0
playCounter = 0

def dashes():
    print("=================================")

while play: 
    compChoice = randrange(10)
    userPrompt = int(input("Choose a number between 0 and 10: "))
    dashes()
    if userPrompt == compChoice:
        correctCounter += 1
        playCounter += 1
        print(f"You guessed correctly! You and the computer both chose the number: {compChoice}. Well done!")
    elif userPrompt != compChoice:
        playCounter += 1
        print(f"Sorry! you guessed incorrectly. The computer chose the number: {compChoice}.")
    else: 
        print("I do not understand, input a valid number (0-10).")

    dashes()

    print("STATS:")
    print(f"You have correctly guessed the number {correctCounter} time(s), with a total guess count of {playCounter}.")
    print("This brings your win percentage to:", correctCounter / playCounter)
    
    dashes()
    
    again = str(input("Do you want to play again, type yes or no?"))
    dashes()
    if again not in ('yes', 'YES', 'Yes', 'y', 'Y'):
      play = False
      break
