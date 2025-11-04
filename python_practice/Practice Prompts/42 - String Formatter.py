# Given a string, format it to clean up unnecessary chars

def string_format(prompt):

    import re

    prompt_lower = str(prompt).strip().lower().capitalize()

    case_adjusted = prompt_lower.capitalize()

    # The pattern [\!\?\.\,]+$ matches any sequence of punctuation at the end of the string 
    # consisting of: # !, ?, ., or , and we replace it with a single period.

    final_string = re.sub(r'[\!\?\.\,]+$', '.', case_adjusted)

    return final_string

result = string_format("HELLO, world!!")
print(result)