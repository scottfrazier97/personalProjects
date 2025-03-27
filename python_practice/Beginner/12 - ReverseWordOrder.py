#Reverse order of words in sentence

def reverse_order(words):
    beg_words = []
    for i in words:
        i = i.split()
        beg_words.append(i.reverse())
    print(beg_words)
reverse_order("My name is Scott")