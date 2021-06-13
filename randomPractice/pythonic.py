waters = 'Dasani and Ozarka'

people = []
for randomness in waters:
    people.append(randomness)

print(f'The letters include: {people}')

#LIST COMPREHENSION
waters2 = [lettering for lettering in waters]
print(waters2)

numbers = [54, 8, 97, 19, 14]
def numTest():
    for num in numbers: 
        if num == 54:
            print(f'{num} --- This value is equal to 54')
        elif num > 54:
            print(f'{num} --- This value is greater than 54')
        else:
            print(f'{num} --- This value is less than 54')
numTest()

#BOOLS & LOOPS
light_on = True
print(light_on)

freedom = "AMERICA!"
is_free_country = True
while is_free_country:
    print('America is FREE, That is what I am talking about!', freedom)
    break

bestDamnCountryEver = [liberty for liberty in freedom]
print(bestDamnCountryEver)

for freedom in freedom:
    print(freedom)

for i in range(4):
    print('*************---------------')
for x in range(4):
    print('----------------------------')

yearLiberated = int(1776)
currentYear = int(input("Enter the current year: "))
def yearsSince():
    yearsSince = currentYear - yearLiberated
    print(f"It has been {yearsSince} years since America gained it's independence from Great Britain!")

    if yearsSince == 300:
        print("It has been 300 years since America has gained it's independence.")
    elif yearsSince > 300:
        print("It has been more than 300 years since America has gained it's indepence from Great Britain.")
    elif currentYear < 1776:
        print("Something must have been lost in the shadow realm. QUICK MARTY, WE HAVE TO GO BACK TO THE FUTURE!")
    else:
        pass
yearsSince()
