# Given a string with brackets ()[]{}, determine if it’s balanced.

def bracket_balance_check(prompt):

    prompt_clean = str(prompt).strip().lower()

    count = 0
    for char in prompt_clean:
        if char in ("(", "[", "{"):
            count += 1
        elif char in (")", "]", "}"):
            count -= 1

    if count == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    
result = bracket_balance_check("Will you and your friend(s) be joining?")
print(result)