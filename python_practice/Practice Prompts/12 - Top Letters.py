#Given a string, return the most frequent characters.

prompt = """
    In the heart of the city, the library stood as a beacon of knowledge and curiosity. 
    Students, researchers, and casual readers alike wandered its aisles, 
    searching for books that would expand their minds and transport them to different worlds. 
    The library hosted weekly events, including storytelling sessions for children, 
    lectures on history and science, and workshops on writing and literature. 
    Despite the hustle and bustle outside, inside the library there was a calm serenity, 
    where one could lose track of time amidst the pages of countless books. 
    Visitors often remarked that the scent of old pages and polished wood created 
    an atmosphere that was both comforting and inspiring, a reminder that learning 
    was a lifelong adventure.
    """

def word_counter(string):

    tracker = {}

    lower_string = string.lower()
    
    invalid_chars = [".", ","]
    for char in lower_string:

        if char in invalid_chars:
            lower_string = lower_string.replace(char, "")
        else:
            continue
    
    final_string = lower_string.split()

    for item in final_string:
        for letter in item:
            if letter in tracker:
                tracker[letter] += 1
            else:
                tracker[letter] = 1

    # Sort dict based on .items() -> (key, value) tuple pairs, grabbing second "item" in tuple.
    # Then put all items in reverse order based on value (greatest to least), and grab first 3 elements. 
    # Convert back to dict to preserve order.
    top_3 = dict(sorted(tracker.items(), key=lambda item: item[1], reverse=True)[:3])

    print(f"Top 3 letters:")

    for x, y in top_3.items():
        print(f"{x}: {y}")

word_counter(prompt)      