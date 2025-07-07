class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            for i in range(len(str2), 0, -1):
                if len(str2)%i != 0:
                    continue

                l = i
                p = str2[0:l]
                print(l,p)
                pa = True
                if len(str2)%l != 0 or len(str1)%l != 0:
                    pa = False
                for i in range(0,len(str2),l):
                    print(2,str2[i:i+l])
                    if str2[i:i+l] != p:
                        pa = False

                for i in range(0,len(str1),l):
                    print(1, str1[i:i+l])
                    if str1[i:i+l] != p:
                        pa = False

                if pa:
                    return p

            return ""
