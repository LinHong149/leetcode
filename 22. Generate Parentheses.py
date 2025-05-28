class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = set()

        def dfs(o, c, s):
            if len(s) == 2*n:
                comb.add(s)
                return

            if o < n:
                dfs(o+1, c, s+"(")

            if c < o:
                dfs(o, c+1, s+")")

        dfs(0,0,"")
        return(list(comb))
