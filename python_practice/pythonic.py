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
candies = ["Sour Patch Kids", "Swedish Fish", "Reeses", "Sour Skittles", "Kazoozles", "Hershey's Chocolate", "Kit Kats"]
print(candies)

#adding an item to a specific spot within list
additional_candies = candies.insert(5, "LemonHeads")

candy_cart = []
allowance = 3

for candy in candies:
    number = candies.index(candy)
    print(f"|{number}| {candy}")

#removing last element of a list
# candies.pop()
# print(candies)

#removing specific item using index from list
# candies.pop(3)
# print(candies)

currently_spent = 0
while currently_spent < allowance:
    currently_spent = currently_spent + 1
    candy_prompt = int(input("Which candy would you like? Enter a number: "))
    candy_cart.append(candies[candy_prompt])
print(f"You chose {candy_cart} as your candies. Enjoy!")










