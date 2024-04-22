#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells 
#them the year that they will turn 100 years old.

user_name = str(input('What is your name? '))
user_age = int(input('What is your age? '))

import datetime

current_date = datetime.datetime.now()
current_year = int(current_date.strftime('%Y'))

if user_age < 100:
    birth_year = current_year - user_age
    year_100 = birth_year + 100
    print(year_100)
else:
    pass
    

                   
