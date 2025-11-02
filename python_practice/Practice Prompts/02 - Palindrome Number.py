#Given an integer x, return true if x is a palindrome, and false otherwise.

def palindrome_finder(num):

    num = str(num).strip()
    num_reversed = num[::-1]

    print(f"{num}\n{num_reversed}")

    if num == num_reversed:
        print("Palindrome")
    else:
        print("Not a palindrome")
        
palindrome_finder(12345654321)