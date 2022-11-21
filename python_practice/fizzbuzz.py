for n in range(100):
    if n % 5 == 0 and n % 3 == 0:   #If value is divisible by 5 and 3, print FizzBuzz
        print(n, "FizzBuzz", sep="-")
        continue
    elif n % 5 == 0:    #If value is divisible by just 5, print Fizz
        print(n, "Fizz", sep="-")
        continue
    elif n % 3 == 0:
        print(n, "Buzz", sep="-")   #If value is divisible by just 3, print Buzz
        continue
    print(n)