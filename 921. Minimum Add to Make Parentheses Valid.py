class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        counter = 0
        numOpen = 0

        for i in s:
            if i == "(":
                numOpen += 1
            else:
                if numOpen == 0:
                    counter += 1
                else:
                    numOpen -= 1
        
        return(counter + numOpen)
