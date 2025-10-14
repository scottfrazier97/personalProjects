# Return both the word and its length, ignoring punctuation.

def longest_word(sentence):

    lower_string = str(sentence).lower().strip()

    invalid_chars = [".", ",","'"]
    for char in lower_string:

        if char in invalid_chars:
            lower_string = lower_string.replace(char, "")
        else:
            continue

    #Removing spaces and duplicate words
    final_string = set(lower_string.split())

    word_length = 0
    longest_word = ""


    for word in final_string:

        length = len(word)
        word_length = length






    return print(final_string)
    
longest_word("What you've just said is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it.")