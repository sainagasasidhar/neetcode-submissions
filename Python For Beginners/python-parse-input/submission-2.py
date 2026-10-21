from typing import List

def read_integers() -> List[int]:
    input_string = input().split(",");
    input_int = [];
    for i in input_string:
        input_int.append(int(i))
    return input_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
