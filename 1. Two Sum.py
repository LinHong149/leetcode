class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            a = target-nums[i]
            if a in hash:
                return [hash[a], i]
            hash[nums[i]]=i
