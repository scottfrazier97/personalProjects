#Return common elements between two lists below, no duplicates.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Given that we do not want duplicates, we can convert to sets which remove duplicates by nature.
#Can then use the set intersection function to find common elements
print(list(set(a).intersection(b)))

#Doing the same thing, not removing duplicates
result = []
for element in a:
    if element in b:
        result.append(element)
