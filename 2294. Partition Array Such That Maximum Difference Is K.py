class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        counter = 1
        m = nums[0]
        for i in range(1, len(nums)):
            if nums[i]-m >k:
                counter+=1
                m = nums[i]
        return counter
