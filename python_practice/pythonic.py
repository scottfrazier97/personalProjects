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

#LOOPING through a list
candies = ["Sour Patch Kids", "Swedish Fish", "Reeses", "Sour Skittles", "Kazoozles"]
candy_cart = []
allowance = 3

for candy in candies:
    number = candies.index(candy)
    print(f"|{number}| {candy}")

currently_spent = 0
while currently_spent < allowance:
    currently_spent = currently_spent + 1
    candy_prompt = int(input("Which candy would you like? "))
    candy_cart.append(candies[candy_prompt])
    
print(f"You chose {candy_cart} as your candies. Enjoy!")










