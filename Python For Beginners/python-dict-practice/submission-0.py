from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    countDict = {}
    for char in word:
        if char in countDict:
            countDict[char]+=1
        else:
            countDict[char]=1

    return countDict;




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
