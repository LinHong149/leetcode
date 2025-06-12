class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        def greedy(i, j):
            nJumps = nums[i]
            # print(i, nJumps)
            nextv = 0
            nexti = 0
            for idx in range(1, nJumps+1):
                if i+idx < n-1:
                    v = nums[idx+1]
                    # print("jumps:", idx+1, v)
                    potential = nums[i+idx]+idx
                    if potential > nextv:
                        nextv = potential
                        nexti = i+idx
                
                else:
                    # print("returning", j)
                    return j

            # print("nexti", nexti, nextv)
            return greedy(nexti, j+1)

        return greedy(0, 1)
