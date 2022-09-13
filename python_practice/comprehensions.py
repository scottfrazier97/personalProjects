times_four = [x**4 for x in range(5)]
print(times_four)

times_five = {x:x**5 for x in range(5)}
print(times_five)

x_list = [15, 10, 5]
y_list = [5, 10, 15]

print(sum(x*y for x,y in zip(x_list, y_list)))

variable = [x for x in [1,2,3] if x ==1 or x==3]
print(f"{variable} - Printing odd numbers.")

variable2 = [y**2 for x in [[1,2,3,4]] for y in x]
print(variable2)