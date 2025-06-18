class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        
        for i in range(0, n, 3):
            if nums[i] + k < nums[i+2]:
                return []
            ans.append([nums[i], nums[i+1], nums[i+2]])
        
        
        return ans
