def generate_pairs(prompt):
    
    import random

    prompt = [name.strip() for name in prompt]

    tracker = {name: "" for name in prompt}

    for name in prompt:
        finished = False

        # Create a list of possible recipients LEFT
        available = [n for n in prompt if n not in tracker.values()]

        # Randomize order once 
        random.shuffle(available)

        while not finished:
            if not available:
                # No recipients left — RESTART the whole process
                return generate_pairs(prompt)

            candidate = available.pop()

            if candidate != name:    
                tracker[name] = candidate
                finished = True

    return tracker
        
result = generate_pairs(['Scott','Tamara','Karen','Randy','Ben','Sophia','Johnny','Julianna','Becky','Norma','Steve','Robert'])
{print(f"{k} --> {v}") for k,v in result.items()}