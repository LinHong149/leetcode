class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binStart = str(bin(start)[2:])
        binGoal = str(bin(goal)[2:])

        if len(binStart) > len(binGoal):
            longer = binStart
            shorter = binGoal
        else:
            shorter = binStart
            longer = binGoal

        counter = 0
        for i in range(len(shorter)):
            if binStart[-(i+1)] != binGoal[-(i+1)]:
                counter += 1
                # print(binStart[-(i+1)], binGoal[-(i+1)], "index", i+1)
        
        for i in range(len(longer)-len(shorter)):
            if longer[i] == "1":
                counter += 1


        # print(binStart)
        # print(binGoal)

        return counter
