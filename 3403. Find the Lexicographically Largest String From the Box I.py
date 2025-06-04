class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        largestStart = chr(max(ord(x) for x in word))

        maxLen = len(word)-numFriends+1
        strings = []

        if numFriends <2:
            return word

        for c in range(len(word)):
            if word[c] == largestStart:
                string = word[c:min(len(word),c+maxLen)]
                strings.append(string)

        strings.sort(reverse=True)
        return(strings[0])
        
