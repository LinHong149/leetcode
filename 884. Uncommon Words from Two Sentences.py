class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string1 = s1.split() + s2.split()
        words = list(set(string1))

        # print(string1)
        
        for i in string1:
            if string1.count(i) > 1 and i in words:
                words.remove(i)

        return(words)
