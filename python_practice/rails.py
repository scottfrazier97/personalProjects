# total_blocks = 900
# counter = 0

# while counter < total_blocks:
#     if counter % 7 == 0:
#         print(f"{counter}: Powered Rail")
#     else:
#         print(f"{counter}: Rail")
#     counter += 1

total_blocks = 900

for index, _ in enumerate(range(total_blocks)): #The underscore is a common placeholder convention here. It is still being assigned to the value of the enumerate function, but not actually being utilized in our code. Therefore, the "_" is just for the reader to see it and recognize as a placeholder.
    if index % 7 == 0:
        print(f"{index}: Powered Rail")
    else:
        print(f"{index}: Rail")