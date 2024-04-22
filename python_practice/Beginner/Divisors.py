#Ask user for number, print numbers that evenly divide into that input

user_input = int(input("Type a number: "))

for n in range(1,user_input):
    if user_input % n == 0:
        print(n)