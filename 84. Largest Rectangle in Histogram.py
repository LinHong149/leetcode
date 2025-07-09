class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        
        for i,h in enumerate(heights):

            start = i
            while stack and stack[-1][1] > h: # graph lowers
                index, height = stack.pop()
                ans = max(ans, height*(i-index))
                start = index

            stack.append((start,h))

        for i in stack:
            ans = max(ans, i[1]*(len(heights)-i[0]))

        return ans
        
        #  TLE stores height as the index, and index as the value
        #  Edits stack for every change in height, while ^ only edits for every rectangle
        # stack = []
        # ans = set()
        # l = len(heights)

        # for i in range(l):
        #     h = heights[i]
        #     while h < len(stack):
        #         ans.add(len(stack)*(i-stack.pop())) 

        #     while h > len(stack):
        #         stack.append(i)

        # for i in range(len(stack)):
        #     ans.add(len(stack)*(l-stack.pop()))

        # return max(ans) if len(ans) else 0
