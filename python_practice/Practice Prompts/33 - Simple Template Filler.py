# Given a text template, fill in placeholders dynamically

def template_filler(name):

    data = [
        {"name": "Scott", "amount": 250},
        {"name": "Bob", "amount": 175},
        {"name": "Linda", "amount": 200},
        {"name": "Tina", "amount": 50},
        {"name": "Gene", "amount": 35},
        {"name": "Louise", "amount": 10}
    ]
    
    name = str(name).strip().lower()

    for dict in data:

        if dict["name"].lower() == name:
            return f"Hello {name.capitalize()}, your balance is ${dict["amount"]}"
        
    # only reached if no match found in loop
    return "Name not found"

result = template_filler("Scott")
print(result)