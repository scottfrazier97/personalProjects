def nameCharCounter():
    name = str(input('Type your first name: '))
    lettCount = len(name)

    avgLength = 6
    shorterName = avgLength - lettCount
    longerName = lettCount - avgLength
    print("-" * len(name))
    print(f"Your name is {name}, and it is {lettCount} letters long...Don't believe me?! Go ahead and count 'em!")

    if lettCount > avgLength:
        print(f"Your name is pretty long. To be specific, it is {longerName} letter(s) longer than the average first name length, which is:", avgLength)
    elif lettCount < avgLength:
        print(f"Your name is pretty short. To be specific, it is {shorterName} letter(s) shorter than the average first name length, which is:", avgLength)
    elif lettCount == 6:
        print(f"Your name is equal to the average first name length, which is", avgLength, "letters.")
    else:
        pass
nameCharCounter()