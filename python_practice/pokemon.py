from random import randrange

#pokemon-types
pokemon_starter_types = ["Fire", "Water", "Grass"]

#pokemon-types and names, dictionary
beginning_pokemon = {
    "Charmander": "Fire",
    "Squirtle": "Water",
    "Bulbasaur": "Grass"}    

#beginning messages
###### Added function to print cleaner line

def print_line(string):
    result = '-'*len(string)
    return result

text1 = "Hello there! Welcome to the amazing world of Pokemon!"
###### Using f string to print onjects from functions
print(f'{text1}\n{print_line(text1)}')
print("Let's get some basic information about you.")

###### Added function to consider incorrect user input. Error previously occured if user entered a str for an int() object.
def input_check(question, dtype):
    while True:
        try:
            result = dtype(input(question))
            break
        except:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue
    return result
        
#user info using a class
class Character:
    def __init__(self, name, age, gender, experience):
        self. name = name
        self.age = age
        self.gender = gender
        self.experience = experience

    @classmethod
    def from_input(cls):  
        return cls(
            ##### Calling the input_check function. Two arguments are passed. One is the question and one is the user input dtype
            input_check('What is your name? ', str),
            input_check('What is your age? ***Try entering a Str value to see how input_check function works', int), 
            input_check('What is your gender? ', str),
            input_check('How many years of Pokemon experience do you have? ***Try entering a Str value to see how input_check function works', int)
        )

user = Character.from_input()

print(f"Hello there, {user.name}! You are {user.age} years old, and you are a {user.gender} with {user.experience} years of Pokemon experience.")
print(" ")
print(f"{user.name}! It is time to begin your journey.")
print(" ")

##### Printing a clean line equal to the length of the text using print_line function
text2 = "Would you like some basic information on the different types of pokemon?"
print(f'{text2}\n{print_line(text2)}')

#checking if the user wants more information for the pokemon
##### Added similar function to input_check to simplify logical comparisons. 
def input_uppercase(question, dtype):
    while True:
        try:
            result = dtype(input(question))
            result = result.lstrip()
            result = result.rstrip()
            result = result.upper()
            break
        except:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue
    return result

#pokemon-type descriptions
pokemon_type = {
"fire_description":  "Fire-types are a very strong-willed pokemon type. They are effective against grass-type pokemon but are weak to water-type pokemon.",
"grass_description": "Grass-types are one of the statistically weakest pokemon, but will be an effective ally against water-type pokemon.",
"water_description": "Water-types are one of the most common types of pokemon, and will be very useful against fire-types."
}

##### Adjusted the description input process. This can be done in multiple ways. The pokemon_type var is a json object that can be called by selecting the appropriate key.   
##### You don't have to use a for loop after the user input. If you want to go that route you will need a break statment after each logical condition. That is why the code returned 4 print statements each time.
##### Input_uppercase takes any user input and formats it into one data type. Logical comparisons will be alot easier if you force user inputs into a format that is easy to work wwith.
##### It's best practice to try to make your code as simple as possible. Simple over complex over complicated is a good rule of thumb.

##### Set Done as False. Process starts as not done which is obvious.
done = False

##### As long as the Done variable is False, keep looping.
while done == False:
    ##### Input_uppercase fuction fixes any user error and capitalizes all letters of the input string
    basic_info = input_uppercase("Please type Fire, Water, Grass, or All to see a quick description! If not, type no. ", str)
    ##### FIRE, WATER, GRASS, and ALL can be capital because the input is converted to capital letters. This can be lower case.
    if basic_info == "FIRE":
        print(pokemon_type["fire_description"])
    elif basic_info == "WATER":
        print(pokemon_type["water_description"])
    elif basic_info == "GRASS":
        print(pokemon_type["grass_description"])
        
    ##### Incorperated a for loop so your project showcases how to use one. enumerate loops through a list and the index value for that list. Both iterators are printable.
    elif basic_info == "ALL":
        for num, desc in enumerate(pokemon_type):
            ##### enumerate starts index (num) iterator at 0. Incrementing the iterator by one fixes this issue.
            num = num + 1
            ##### printing the index and iterator value desc for each item in pokemon_type
            print(f"{num}-{pokemon_type[desc]}")
    elif basic_info == "NO":
        print("OK, please continue to pick your pokemon!")
        
        ##### Break statements are your best friend. If user selects no, while loop ends regardless of conditions such as done = false.
        break
    else: 
        print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
        ##### If user enters an incorrect value, the continue statement forces loop to move to the next iteration, skipping the next while true
        continue
    
    ##### Nested While true confirms if the user wants to continue. If yes, the inner while loop breaks, causing the outer while loop push to the next iteration of inputs
    while True:
        continue_prompt = input_uppercase("Would you like info on the other types of Pokemon? If so, write and enter yes. If not, write and enter no. ", str)
        if continue_prompt == "NO":
            ##### If user enters no, the done variable becomes true, then the nested while loop breaks, and the outer while loop because the conditional statement done = false is no longer true
            done = True
            print("OK, please continue to pick your pokemon!")
            break
        elif continue_prompt == 'YES':
            ##### If user enters yes, the nested while loop breaks, causing the outer while loop to move to the next iteration starting at the user input
            break
        else:
            print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
            continue

#list comprehension
# print("Here are your choices for starter pokemon: ")
# print([pokemon for pokemon in pokemon_starter_types])

currently_playing = True
#asking the user which type of pokemon they would like
# ------print(beginning_pokemon)
# ------user_choice = str(input("Which one would you like to accompany you on your journey? "))