import datetime

#current date
today = datetime.datetime.now()

def print_line(string):
    result = '-' * len(string)
    return result

text1 = "Hello there! This is a tool to use discover facts about Halley's Comet, and space in general!"

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
            input_check('What is your age? ', int), 
        )

#for output
user = Character.from_input()

#years until the next comet
years_until_next_comet = 2061 - today.year

#Age when the next comet arrives in 2061
newAge = user.age + years_until_next_comet

#final output
print(f"Hello there, {user.name}! You are {user.age} years old right now.You will be approximately {newAge} years old the next time Halley's Comet is near Earth again in 2061.\n{print_line(text1)}")

planets = {
    "Mercury": str("6.5 Years"), 
    "Venus": str("6.5 Years"),
    "Moon": str("3 Months"), 
    "Mars": str("7 Months"), 
    "Jupiter": str("6 Years"), 
    "Saturn": str("7 Years"), 
    "Uranus": str("8.5 Years"), 
    "Neptune": str("12 Years"), 
    "Pluto": str("9.5 Years")
    }

#Additional fun facts about your age and space
print(f"Here are some additional fun facts! Below we have times listed for how long it would take to travel to each planet in the Solar System! ")
print(print_line(text1))
print(" PLANET ", " TRAVEL TIME ", sep=" - ")

for x, y in planets.items():
  print(f"|{x}| - {y}")
