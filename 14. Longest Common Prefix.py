class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = min(len(x) for x in strs)

        if not strs or minLength == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        for i in range(1, minLength+1, 1):
            prefix = strs[0][:i]
            for word in strs:
                if word[:i] != prefix:
                    return strs[0][:i-1]

        return strs[0][:minLength]
