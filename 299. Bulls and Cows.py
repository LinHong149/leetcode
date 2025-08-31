class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = Counter(secret)
        g = Counter(guess)

        correct = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                correct +=1

        wrongPos = 0
        for i in s:
            if i in g:
                wrongPos += min(s[i], g[i])

        return f"{correct}A{wrongPos-correct}B"

        
