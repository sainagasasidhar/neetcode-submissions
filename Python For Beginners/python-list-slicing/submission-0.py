from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    last_three = [];
    for i in range(0,3,1):
        last_three.append(len(my_list)-i-1)
    return last_three


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
