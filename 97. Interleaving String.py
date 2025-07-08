class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP method
        if Counter(s1+s2)!= Counter(s3):
            return False

        l1, l2 = len(s1), len(s2)
        dp = [[False]*(l2+1) for i in range(l1+1)]
        dp[l1][l2] = True
        
        for i in range(l1, -1,-1):
            for j in range(l2,-1,-1):
                if i < l1 and s3[i+j] == s1[i] and dp[i+1][j]:
                    dp[i][j]= True
                if j < l2 and s3[i+j] == s2[j] and dp[i][j+1]:
                    dp[i][j]= True
        return dp[0][0]









        # Caching Method
        # l1, l2 = len(s1), len(s2)

        # dp = set()
        # def search(i1, i2):
        #     if i1 == l1 and i2 == l2:
        #         return True
        #     if (i1,i2) in dp:
        #         return False

        #     if i1 < l1 and s3[i1+i2] == s1[i1] and search(i1+1, i2):
        #             return True
        #     if i2 < l2 and s3[i1+i2] == s2[i2] and search(i1, i2+1):
        #             return True

        #     dp.add((i1,i2))
        #     return False

        # return search(0, 0)
