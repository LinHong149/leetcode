class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m=0
        for i in nums:
            if i-1 not in nums:
                c=1
                while i+c in nums:
                    c+=1
                m = max(c, m)

        return(m)
