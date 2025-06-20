import copy
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        s = sorted(nums)
        l = []
        t = [s[0]]
        for i in range(1, len(s)):
            if s[i] - s[i-1] <= limit:
                t.append(s[i])
            else:
                l.append(t)
                t = [s[i]]
        l.append(t)
        c=[x[:]for x in l]


        m = {}
        for i, g in enumerate(c):
            for v in g:
                m[v] = i

        print(m)
        for i in range(len(nums)):
            nums[i] = l[m[nums[i]]].pop(0)

        print(nums, l, c)
        return(nums)
