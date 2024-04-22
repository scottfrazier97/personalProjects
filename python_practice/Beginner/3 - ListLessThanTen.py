#Look for numbers in list less than 10

OG_nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []
for n in OG_nums:
    if n < 10:
        new_list.append(n)
    else:
        pass
print(new_list)

#Same thing as above, but list comprehension
#FORMAT: [DO THIS | FOR THIS COLLECTION | IN THIS SITUATION]
# [print(n) | for n in OG_nums | if n < 10]
[print(n) for n in OG_nums if n < 10]

user_input = int(input("Input a number: "))

OG_GT_User = []
for i in OG_nums:
    if user_input > i:
        OG_GT_User.append(i)
    else:
        pass
print(OG_GT_User)