
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        compressed = []
        total=0
        pos = nums[0]>=0
        for i in range(len(nums)):
            if (nums[i] >= 0) is not pos: #if signs change
                pos = not pos
                compressed.append(total)
                total=0
            total+=nums[i]
            # print(total)
        compressed.append(total)

        print(compressed) 
        ans = compressed[0]

        if len(compressed)==1 and (ans<0):
            return max(nums)
        m = compressed[0]
        curr = compressed[0]
        for val in compressed[1:]:
            curr = max(val, curr+val)
            m = max(curr, m)
        # print(ans)
        return m
