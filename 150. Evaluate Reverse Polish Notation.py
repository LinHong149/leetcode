class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*","/"}
        s = []
        for t in tokens:
            # print(t, s)
            if t not in op:
                s.append(int(t))
            else:
                b = s.pop()
                a = s.pop()
                if t == "+":
                    s.append(a+b)
                elif t == "-":
                    s.append(a-b)
                elif t == "*":
                    s.append(a*b)
                else:
                    s.append(int(a/b))

        return int(s[0])
            