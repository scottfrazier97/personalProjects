# Return True if a string has all unique characters, False otherwise.

def uniqueness_check(prompt):

    prompt = str(prompt)

    if len(prompt) != len(set(prompt)):
        print("Duplicate values found")
    else:
        print("No duplicate values found")

uniqueness_check("Hello")