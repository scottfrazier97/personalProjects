# Given a list of words, return a dictionary keyed by the first letter, 
# with values as lists of words starting with that letter

words =  ["cat","dog","apple","pear","creation","belong","inconceivable","people"]

def word_grouping(wordlist):

    tracker = {}

    for word in wordlist:

        word = str(word).strip().lower()

        first_letter = word[0]

        if first_letter not in tracker:
            tracker[first_letter] = []
            tracker[first_letter].append(word)
        else:
            tracker[first_letter].append(word)

    sorted_tracker = dict(sorted(tracker.items(), key=lambda item: item[0]))

    #Python returns None along with appropriate data if no return statement is used.
    return sorted_tracker

result = word_grouping(words)

for k, v in result.items():
    print(f"{k}: {v}")