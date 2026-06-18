from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    name_dict = {}
    name_dict[name] = age
    return name_dict
    pass


def list_to_dict(words: List[str]) -> Dict[str, int]:
    list_dict = {}
    index = 0
    for i in words:
        list_dict[i] = index
        index = index + 1
    return list_dict
    pass



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
