# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.
import random

nums = []
target = random.randint(2,5)

# Generating our random list of five numbers
while len(nums) < 5:

    nums.append(random.randint(1,5))

print(nums)
print(target)

# Creating dictionary with index as key, and values as value
tracker = {}

for i, n in enumerate(nums):

    # Check if the complement exists
    complement = target - n

    if complement in tracker:
        # If it does, return indices
        print("Indexes found:", [tracker[complement], i])
        print("Numbers found:", [complement, n])
        break

    # Otherwise, store this number with its index
    tracker[n] = i