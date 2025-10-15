# Return both the word and its length, ignoring punctuation. Account for ties.

def longest_word(sentence):

    lower_string = str(sentence).lower().strip()

    invalid_chars = [".", ",","'"]
    for char in lower_string:

        if char in invalid_chars:
            lower_string = lower_string.replace(char, "")

    #Removing spaces and duplicate words
    final_string = set(lower_string.split())

    max_word_length = 0
    longest_words = set()

    for word in final_string:

        current_length = len(word)

        if max_word_length < current_length:
            max_word_length = current_length
            longest_words.clear()
            longest_words.add(word)

        elif max_word_length == current_length:
            longest_words.add(word)

    return longest_words, max_word_length
    

words, length = longest_word("What you've just said is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it.")
print(f"Longest word(s): {words}\nLength: {length}")
