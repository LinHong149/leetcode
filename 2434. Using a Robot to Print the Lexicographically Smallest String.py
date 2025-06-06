class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        minSuf = [None]*n
        minSuf[-1] = s[-1]
        for i in range(n-2, -1, -1):
            minSuf[i] = min(minSuf[i+1], s[i])

        print(minSuf)
        
        stack = []
        res = []
        for i in range(n):
            stack.append(s[i])
            while stack and (i == n-1 or stack[-1] <= minSuf[i+1]):
                res.append(stack.pop())

        return "".join(res)

            
