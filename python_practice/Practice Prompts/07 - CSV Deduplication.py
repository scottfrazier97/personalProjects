#Return a list with duplicates removed but preserve the first occurrence order.

data = [("Alice", "Sales"), ("Bob", "HR"), ("Alice", "Sales"), ("Charlie", "Tech")]

#My naive solution:
#Naive because lists use linear search..So this check takes O(n) time in worst case.
#Since we do this for every item in data, the overall runtime is O(n^2)
deduped = []
for item in data:

    if item not in deduped:
        deduped.append(item)
    else:
        continue

print(deduped)


#Optimized solution: 
#set-backed solution is much more efficient because it avoids repeatedly searching through a growing list.
deduped = []
seen = set()

for item in data:
    if item not in seen:
        deduped.append(item)
        seen.add(item)
