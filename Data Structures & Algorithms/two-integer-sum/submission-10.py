class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map ={}

        for i in range(len(nums)):
            complement = target - nums[i]

            if nums[i] not in hash_map:
                hash_map[complement]=i
            else:
                return[hash_map[target-complement],i]