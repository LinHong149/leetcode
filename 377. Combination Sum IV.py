class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= target:  
                break
            nums.pop()

        if len(nums) == 0:
            return 0


        dp = {}
        def combination(t):
            if t in dp:
                return dp[t]
            if t == target:
                return 1

            res = 0
            if t < target:
                for num in nums:
                    res += combination(t + num)
            dp[t] = res
            return res

        return combination(0)

            
