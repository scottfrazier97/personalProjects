#Given a list of numbers, return the sum of only the even ones.

import random

numbers = []

while len(numbers) < 15:

    numbers.append(random.randrange(1, 100))

even_sum = 0
for num in numbers:

    if num % 2 == 0:
        even_sum += num
    else:
        continue

print(numbers)
print(even_sum)