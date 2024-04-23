#Write a function that checks a list for duplicates and removes them, then reappends to new list

def list_dupe_check(nums):
    nums_set = set()
    for i in nums:
        nums_set.add(i)
    new_list = list(nums_set)
    print(new_list)
list_dupe_check(nums = [1,1,1,2,3,4,4,5,5,7,8,9,10])