class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def bottomUp(r):
            if r == 0:
                return triangle[0][0]

            for c in range(len(triangle[r])-1):
                triangle[r-1][c] += min(triangle[r][c], triangle[r][c+1])

            return bottomUp(r-1)
            

        return bottomUp(len(triangle)-1)




        # TLE (top down)
        # def dfs(l, i):
        #     if l == len(triangle)-1:
        #         return triangle[l][i]
            
        #     return triangle[l][i] + min(dfs(l+1, i),dfs(l+1, i+1))
            


        # return dfs(0,0)
