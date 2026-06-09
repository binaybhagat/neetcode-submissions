def get_longer_word(word1: str, word2: str) -> str:
    pass
    x = len(word1)
    y = len(word2)
    if x > y or x == y:
        return word1
    elif y > x:
        return word2
    else:
        word1        



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
