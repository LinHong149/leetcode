class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            x = "-" + str(x)
        else:
            x = str(x)

        xLen = len(x)

        for i in range(len(x)//2):
            if x[i] != x[xLen-1-i]:
                return False

        return True
