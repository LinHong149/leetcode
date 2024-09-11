class Solution:
    def convert(self, s: str, numRows: int) -> str:
    
        newString = ""

        outterJump = (numRows-1)*2

        zigZagNums = numRows-2


        if numRows == 1 or numRows > len(s):
            return s


        # First row
        for i in range(0, len(s), max(1, outterJump)):
            newString += s[i]
        

        # Middle Section
        modNum = 1
        zigModNum = outterJump-1
        for i in range(numRows-2):
            seperation = ((numRows-2)*2)
            for j in range(i, len(s)):
                if j % outterJump == modNum or j % outterJump == zigModNum:
                    newString += s[j]

            seperation -= 1
            modNum += 1
            zigModNum -= 1



        # Last row
        for i in range(numRows-1, len(s), max(1, outterJump)):
            newString += s[i]

        print(newString)
        return(newString)
