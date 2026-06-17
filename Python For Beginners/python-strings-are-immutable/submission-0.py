def remove_fourth_character(word: str) -> str:
    before_fourth_character = word[:3]
    after_fourth_character = word[4:]
    new_string = before_fourth_character + after_fourth_character
    return new_string

    pass


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
