#Make a two player Rock, Paper, Scissors game

user1 = str(input("User 1, choose Rock/Paper/Scissors: ")).upper()
user2 = str(input("User 2, choose Rock/Paper/Scissors: ")).upper()

if (user1.upper() == 'ROCK' and user2.upper() == 'SCISSORS') or (user1.upper() == 'SCISSORS' and user2.upper() == 'PAPER') or (user1.upper() == 'PAPER' and user2.upper() == 'ROCK'):
    print("User 1 wins!")
elif user1 == user2:
    print('Tie!')
else:
    print('User 2 wins!')