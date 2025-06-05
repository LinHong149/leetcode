class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        initVal = 97
        ref = [chr(i) for i in range(97, 97+26)]

        for i in range(len(s1)):
            in1 = ord(s1[i])-initVal
            in2 = ord(s2[i])-initVal


            ref1 = ref[in1]
            ref2 = ref[in2]
            smaller = min(ref[in1],ref[in2])

            for j in range(26):
                if ref[j] == ref1 or ref[j] == ref2:
                    ref[j] = smaller



        newStr = ""
        for i in range(len(baseStr)):
            newStr += ref[ord(baseStr[i])-initVal]

        return newStr
