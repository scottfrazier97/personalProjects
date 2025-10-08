#Given a string, return a dictionary with the frequency of each character.

def character_count(word):

    prompt = str(word).strip().lower()

    tracker = {}

    for letter in prompt:

        #Can use: tracker[letter] = tracker.get(letter, 0) + 1 ... instead of if/else

        if letter not in tracker:
            tracker[letter] = 1
        else:
            tracker[letter] += 1

    # Sort by value in key:value pair (descending). If tie, sort ties by ascending alphabetical order.
    sorted_tracker = dict(sorted(tracker.items(), key=lambda item: [-item[1], item[0]]))

    for k, v in sorted_tracker.items():
        print(f"{k}: {v}")

character_count("supercalifragilisticexpialidocious")