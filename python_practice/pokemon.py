pokemon_starter_types = ["Fire", "Water", "Grass"]

fire_type_description = "Fire-types are a very strong-willed pokemon type. They are effective against grass-type pokemon but are weak to water-type pokemon."
grass_type_description = "Grass-types are one of the statistically weakest pokemon, but will be an effective ally against water-type pokemon."
water_type_description = "Water-types are one of the most common types of pokemon, and will be very useful against fire-types."

print("---------------------")
print("Hello there! Welcome to the amazing world of Pokemon!")
print("To get started, please pick the type of pokemon you would like!")
print("----------------")

#list comprehension
print("Here are your choices for starter pokemon: ")
print([pokemon for pokemon in pokemon_starter_types])
user_choice = str(input("Which one would you like to accompany you on your journey? "))






