class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        sorted_values = sorted(hash_map.items(), key=lambda item: item[1])

        result = []

        for i in range(k):
            result.append(sorted_values[-1-i][0])

        return result
        