class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        # deal with +-
        s = s.strip()
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        print("s",s)
        while s[0] == 0:
            s = s[1:]


        for i in range(len(s)):
            print(i, s[i])
            if s[i] not in ['0', '1', '2', '3','4','5','6','7','8','9']: # is letter
                s = s[:i]
                break

        print("s", "")
        if s == "":
            return 0
        if neg:
            i = max(-int(s), -(2**31))
        else:
            i = min(int(s), 2**31)

        print(i)
        return(i)


