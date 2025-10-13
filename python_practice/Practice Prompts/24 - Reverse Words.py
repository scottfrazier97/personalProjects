#Given a sentence, reverse the order of words but keep each word intact.

def reverse_sentence():

    prompt = input("Input a sentence:\n")

    reversed_prompt = " ".join(prompt.split()[::-1])

    return reversed_prompt

result = reverse_sentence()
print(result)