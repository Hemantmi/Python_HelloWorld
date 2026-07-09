class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bool = False
        countMap={}
        for num in nums:
            if num not in countMap:
                countMap[num]=1
            else:
                bool= True
                break;
        return bool
        