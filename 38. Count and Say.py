class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        
        for i in range(n-1):
            c = ""
            newS = ""
            while s:
                c = s[0]
                count = 0
                for i in range(len(s)):
                    if s[i] == c:
                        count+=1
                    else:
                        break
                newS = newS +str(count)+c
                s = s[count:]
            s = newS

        return s
