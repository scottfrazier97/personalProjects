x = 'Pluto is a planet'
y = "Pluto is a planet"
z = x == y
print(z)

print("----------")
#using \ to insert ' inside 'str 
pluto = 'Pluto\'s a planet!'
print(pluto)

print("----------")
hello = "hello\nworld"
print(hello)

print("----------")
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello

print("----------")
print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

print("----------")
#strings can be thought of as sequences, the same as lists. Although, strings are immutable.
planet = 'Pluto'
first_letter = planet[0]
print(first_letter)

print("----------")
#last three letters
last_few_letters = planet[-3:]
print(last_few_letters)

print("----------")
#looping over string
letter_loop = [char+'! ' for char in planet]
print(letter_loop)

print("----------")
#all CAPS, all lower
claim = "Pluto is a planet!"
caps = claim.upper()
lower = claim.lower()
print(caps)
print(lower)

print("----------")
#indexing letters
char_counter = claim.index('to')
print(char_counter)

print("----------")
#splitting, defaults to on whitespace
words = claim.split()
print(words)

print("----------")
#splitting on -
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)

print("----------")
#joining strings
planet_list = ["Uranus", "Neptune", "Pluto"]
planet_join = '/'.join(planet_list)
print(planet_join)

sassy_planets = ' 👏 '.join([word.upper() for word in words])
print(sassy_planets)

print("----------")
#concatenating strings
print(planet + ", we miss you.")
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("----------")
#str.format
str_format = "{}, you'll always be the {}th planet to me.".format(planet, position)
print(str_format)

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
str_format_2 = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
print(str_format_2)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

print("----------")
print("----------")

#DICTIONARIES
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

numbers['eleven'] = 11
print(numbers)

#change value associated with existing value
numbers['one'] = 'Pluto'
print(numbers)

#dictionary comprehension
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

#in operator varifies if value is in dict
checkUp = 'Saturn' in planet_to_initial
print(checkUp)

#for loop over dict loops over keys
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

#access a collection of all the keys or all the values with dict.keys() and dict.values(), respectively.
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
variable = ' '.join(sorted(planet_to_initial.values()))
print(variable)

#dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. 
# (In Python jargon, an item refers to a key, value pair)
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

#dict documentation
help(dict)