class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums) < 3:
            return max(nums)

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(nums):
                return 0

            print(i)
            houseVal = nums[i]
                
            nextVal = max(dfs(i+2), dfs(i+3))
            dp[i] = houseVal + nextVal
            return houseVal + nextVal

        return dfs(-2) - nums[-2]
