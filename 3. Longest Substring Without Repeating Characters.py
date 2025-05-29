class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxI = 0
        longest = 0
        visited = []
        
        left = 0
        right = 0
        while right < len(s):
            if s[right] in visited:
                while(s[left]!=s[right]):
                    left+=1
                    longest -= 1
                left+=1
                longest -= 1
            else:
                visited.append(s[right])
                maxI = max(maxI, longest)
            # print(visited)
            longest+=1
            right+=1

        return(maxI+1)
