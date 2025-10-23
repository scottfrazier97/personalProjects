#Replace all words in a text file that appear in a “banned words”
#list with "****", preserving punctuation and spacing.

def censor_tool(user_input):

    import re

    banned_words = {'crap', 'crud', 'dang', 'heck', 'dumb', 'stupid', 'idiot'}

    user_input_lower = str(user_input).strip()

    #Splits on whitespace, commas, and periods to retain the punctuation during split
    user_input_split = re.split(r'( |,|\\.)', user_input_lower)

    for idx, word in enumerate(user_input_split):
        if word.lower() in banned_words:
            censored_word = '*' * len(word)
            user_input_split[idx] = censored_word

    cleaned_string = "".join(user_input_split)
    return cleaned_string.capitalize()

result = censor_tool("What the heck is wrong with that dumb guy. He is always on some stupid powertrip, I don't give a crap if he hears me talking about him")
print(result)