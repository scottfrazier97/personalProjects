# Given social media text like "Loving this! #Python #AI @OpenAI", 
# extract hashtags and mentions separately.

def regex_tags_and_mentions(prompt):

    import re

    prompt_lower = str(prompt).strip()

    # r''	This denotes a raw string literal in Python, which is a common practice when working with regular expressions. It ensures that backslashes are treated as literal characters rather than escape sequences.
    # \w+	This part matches one or more word characters immediately following the character identified by the first part of the pattern.
    # +	    This quantifier matches one or more occurrences of the preceding element (\w).
    # The brackets mean "Any of these characters [#@]"

    pattern = r'[#@]\w+'

    tags_and_mentions = re.findall(pattern, prompt_lower)

    tags = []
    mentions = []

    for find in tags_and_mentions:
        if find[0] == '#':
            tags.append(find)
        elif find[0] == '@':
            mentions.append(find)
            
    return tags, mentions

tags, mentions = regex_tags_and_mentions("Loving this! #Python #AI @OpenAI")
print(f"Tags:\n{tags}\n\nMentions:\n{mentions}")