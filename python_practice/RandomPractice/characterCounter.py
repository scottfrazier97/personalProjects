def nameCharCounter():
    name = str(input('Type your first name: '))
    lettCount = len(name)

    avgLength = 6
    name_shorter_length = avgLength - lettCount
    name_longer_length = lettCount - avgLength
    print("-" * len(name))
    print(f"Your name is {name}, and it is {lettCount} letters long.")

    if lettCount > avgLength:
        print(f"Your name is pretty long. To be specific, it is {name_longer_length} letter(s) longer than the average first name length, which is:", avgLength)
    elif lettCount < avgLength:
        print(f"Your name is pretty short. To be specific, it is {name_shorter_length} letter(s) shorter than the average first name length, which is:", avgLength)
    elif lettCount == 6:
        print(f"Your name is equal to the average first name length, which is", avgLength, "letters.")

nameCharCounter()