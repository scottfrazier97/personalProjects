#Write a function that takes a string and returns it reversed without using slicing ([::-1]).

def reverse_word(word):

    bucket = []

    word = str(word)
    
    max_length = len(word) * -1
    i = -1

    while i >= max_length:

        bucket.append(word[i])
        i -= 1

    #Actually return the object instead of just printing. Returning allows re-use of output.
    return "".join(bucket)

result = reverse_word("Guacamole")
print(result)