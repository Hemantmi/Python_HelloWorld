import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    negative_nums=[]
    for num in nums:
        negative_nums.append(-1 * num)

    heapq.heapify(negative_nums)

    negative_nums.sort()

    corrected_nums=[]
    for num in negative_nums:
        corrected_nums.append(-1 * num)

    return corrected_nums









# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
