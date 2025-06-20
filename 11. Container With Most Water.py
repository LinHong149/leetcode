class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        a = 0

        while (l<r):
            v = min(height[r], height[l])*(r-l)
            a = max(a, v)

            if height[l] > height[r]:
                r -=1
            else:
                l+= 1

        return a
