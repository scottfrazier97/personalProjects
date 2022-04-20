import datetime

#current date
today = datetime.datetime.now()

def print_line(string):
    result = '-' * len(string)
    return result

text1 = "Hello there! This is a tool to use in reference to facts about Halley's Comet."

print(f'{text1}\n{print_line(text1)}')
print("Let's get some basic information about you.")

def input_check(question, dtype):
    while True:
        try:
            result = dtype(input(question))
            break
        except:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue
    return result

class Character:
    def __init__(self, name, age):
        self. name = name
        self.age = age

    @classmethod
    def from_input(cls):  
        return cls(
            ##### Calling the input_check function. Two arguments are passed. One is the question and one is the user input dtype
            input_check('What is your name? ', str),
            input_check('What is your age?', int), 
        )

#for output
user = Character.from_input()

#years until the next comet
years_until_next_comet = 2061 - today.year

#Age when the next comet arrives in 2061
newAge = user.age + years_until_next_comet

#comet_increments

#final output
print(f"Hello there, {user.name}! You are {user.age} years old right now.\nYou will be {newAge} years old the next time Halley's Comet is near Earth again in 2061.")
