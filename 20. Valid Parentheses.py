class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for i in s:
            # print(i, brackets, len(brackets))
            if i == "[" or i == "{" or i == "(":
                brackets.append(i)
            elif (i == "]" or i == "}" or i == ")") and len(brackets) > 0:
                # print(i)
                if i == "]" and brackets[-1] == "[":
                    brackets.pop()
                elif i == "}" and brackets[-1] == "{":
                    brackets.pop()
                elif i == ")" and brackets[-1] == "(":
                    brackets.pop()
                else:
                    # print("false cuz they dont equal")
                    return False
            else:
                return False

        # print("final", brackets)
        if len(brackets) > 0:
            return False
        else:
            return True 

            
            

