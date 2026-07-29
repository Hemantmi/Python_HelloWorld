import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    list=heapq.nsmallest(1,arr)
    return list[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    list = heapq.nsmallest(4,arr)
    return sorted(list)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    list=heapq.nsmallest(2,arr)
    new_list=[]

    new_list.append(list[1])
    new_list.append(list[0])

    return new_list


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

