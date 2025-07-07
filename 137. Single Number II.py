class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        prev = nums[0]
        # print(nums)
        for i in range(3,len(nums),3):
            # print(prev, nums[i-1],nums[i])
            if nums[i-1] != prev:
                # print(prev)
                return prev
            prev = nums[i]
        return nums[-1]

    
