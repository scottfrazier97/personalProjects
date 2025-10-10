# Write a function that removes all vowels from a string.

vowels = ['a', 'e', 'i', 'o', 'u']

def remove_vowels(string):

    lower_string = str(string).strip().lower()

    cleaned_string = [i for i in lower_string if i not in vowels]
    vowel_count = len(lower_string) - len(cleaned_string)

    print(f"Original word: {string}\nVowelless version: {"".join(cleaned_string)}\nVowel Count: {vowel_count}")

remove_vowels("pneumonoultramicroscopicsilicovolcanoconiosis")