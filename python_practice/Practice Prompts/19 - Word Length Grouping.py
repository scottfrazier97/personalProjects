# Given a list of words, group them by their length

words =  ["cat","dog","apple","pear"]

def word_grouping(wordlist):

    tracker = {}

    for word in wordlist:

        len_key = len(word)

        if len_key not in tracker:
            tracker[len_key] = []
            tracker[len_key].append(word)
        else:
            tracker[len_key].append(word)

    sorted_tracker = dict(sorted(tracker.items(), key=lambda item: item[0]))

    return sorted_tracker

result = word_grouping(words)

print(result)