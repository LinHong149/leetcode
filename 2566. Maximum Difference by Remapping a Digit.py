class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max = ""
        min = ""
        fromMax = s[0]
        for i in s:
            if i != "9":
                fromMax = i
                break

        fromMin = s[0]
        for i in s:
            if i != "0":
                fromMin = i
                break

        for i in s:
            if i == fromMax:
                max+="9"
            else:
                max+=i

        for i in s:
            if i == fromMin:
                min+="0"
            else:
                min+=i

        ans = int(max)-int(min)

        print(ans)
        return ans
