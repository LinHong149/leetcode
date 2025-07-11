class Solution:
    def lengthLongestPath(self, input: str) -> int:
        commands = input.split("\n")
        stack = []

        maxPath = ""
        for i in commands:
            tabs = 0
            while "\t" in i:
                tabs +=1
                i=i[1:]

            stack = stack[:tabs]
            stack.append(i)

            if "." in i:
                path = "/".join(stack)
                if len(path) > len(maxPath):
                    maxPath = path



        return len(maxPath)
