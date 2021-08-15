# #if value is divisible by 5, print Fizz
for n in range(100):
    if n % 5 == 0:
        print("Fizz")
        continue
    elif n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
        continue
    elif n % 3 == 0:
        print("Buzz")
        continue
    print(n)

