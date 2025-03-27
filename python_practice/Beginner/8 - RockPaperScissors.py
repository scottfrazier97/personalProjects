#Make a two player Rock, Paper, Scissors game

user1 = str(input("User 1, choose Rock/Paper/Scissors: ")).upper()
user2 = str(input("User 2, choose Rock/Paper/Scissors: ")).upper()

if (user1 == 'ROCK' and user2 == 'SCISSORS') or (user1 == 'SCISSORS' and user2 == 'PAPER') or (user1 == 'PAPER' and user2 == 'ROCK'):
    print("User 1 wins!")
elif user1 == user2:
    print('Tie!')
else:
    print('User 2 wins!')