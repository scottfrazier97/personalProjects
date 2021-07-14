from random import randrange

#pokemon-types
pokemon_starter_types = ["Fire", "Water", "Grass"]

#pokemon-types and names, dictionary
beginning_pokemon = {
    "Charmander": "Fire",
    "Squirtle": "Water",
    "Bulbasaur": "Grass"}

#beginning messages
print("---------------------")
print("Hello there! Welcome to the amazing world of Pokemon!")
print("To get started, would you like some basic information on the different types of pokemon?")
basic_info = str(input("If so, please type Fire, Water, or Grass to see a quick description! If not, type no. "))
print("----------------")

#pokemon-type descriptions
pokemon_type = {
"fire_description":  "Fire-types are a very strong-willed pokemon type. They are effective against grass-type pokemon but are weak to water-type pokemon.",
"grass_description": "Grass-types are one of the statistically weakest pokemon, but will be an effective ally against water-type pokemon.",
"water_description": "Water-types are one of the most common types of pokemon, and will be very useful against fire-types."
}

#checking if the user wants more information for the pokemon
for x in pokemon_type:

    if basic_info == "Fire" or basic_info == "fire":
        print(pokemon_type["fire_description"])
        print("---")
        continue
    elif basic_info == "Water" or basic_info == "water":
        print(pokemon_type["water_description"])
    elif basic_info == "Grass" or basic_info == "grass":
        print(pokemon_type["grass_description"])
    elif basic_info == "No" or basic_info == "no":
        print("OK, please continue to pick your pokemon!")
    else: 
        print("Someting must have gone wrong, SORRY! Make sure you read the instructions carefully!")
        
        for y in pokemon_type:
            continue_prompt = str(input("Would you like info on the other types of Pokemon? If so, enter their type. If not, write and enter continue. "))

            if continue_prompt == "Water" or continue_prompt == "water" or continue_prompt == "Grass" or continue_prompt == "grass":
                print(pokemon_type["water_description"])


print("----------------")

#list comprehension
# print("Here are your choices for starter pokemon: ")
# print([pokemon for pokemon in pokemon_starter_types])

currently_playing = True
#asking the user which type of pokemon they would like
# ------print(beginning_pokemon)
# ------user_choice = str(input("Which one would you like to accompany you on your journey? "))












