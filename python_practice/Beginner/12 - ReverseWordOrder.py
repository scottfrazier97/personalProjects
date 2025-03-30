def reverse_order_and_letters(words):
    # Reverse the order of words
    reversed_order = words[::-1]
    # Reverse the letters in each word
    result = [word[::-1] for word in reversed_order]
    # Join the result into a string if needed, or return the list
    print(" ".join(result))
    
reverse_order_and_letters(["My", "name", "is", "Scott"])
