class Solution:
    def maxDiff(self, num: int) -> int:
        if len(str(num))==1:
            return 8

        xMax = "9"
        for i in str(num):
            if i != "9":
                xMax = i
                break
        xMin = "0"

        yMax = "9"
        yMin="0"
        
        if str(num)[0] != "1":
            xMin = str(num)[0]
            yMin = "1"
        else: # is 1
            xMin = str(num)[1]
            if int(str(num).replace(xMin, "0")) == 0:
                print("a")
                yMin = "1"
            else:
                for i in range(1, len(str(num)),1):
                    if str(num)[i] != "0" and str(num)[i] != "1":
                        xMin = str(num)[i]
                        yMin = "0" 
                        break


        max = str(num).replace(xMax, yMax)
        min=str(num).replace(xMin, yMin)
        return int(max)-int(min)
