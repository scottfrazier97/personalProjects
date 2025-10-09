#Find the second largest number in a list without using sorted().

def second_largest():
    import random

    # Generating our random list of five numbers
    nums = []
    
    while len(nums) < 5:

        nums.append(random.randint(1,50))

    print(nums)

    #nums.remove(max(nums)) #Only removes FIRST instance of max, doesn't account for dupes

    nums = [i for i in nums if i != max(nums)]

    return max(nums)

result = second_largest()
print(f"The second largest value in our given list is: {result}")