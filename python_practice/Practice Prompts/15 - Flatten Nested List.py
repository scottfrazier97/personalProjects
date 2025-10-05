#Given [[1,2],[3,4],[5]], return [1,2,3,4,5]

full_list = [[1,2],[3,4],[5]]
flattened = []

for x in full_list:
    for y in x:
        flattened.append(y)

print(flattened)


## Pythonic and faster solution
# import itertools
# merged = list(itertools.chain(*full_list))

# print(merged)