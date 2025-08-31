class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        nums.insert(0,0)
        nums.append(0)
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1] and nums[i+1] > nums[i+2]:
                return i
