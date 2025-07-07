class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        a=[]
        for t in range(n-2):
            if nums[t]>0:
                break
            if t > 0 and nums[t]==nums[t-1]:
                continue
            l=t+1
            r=n-1
            target = -nums[t]

            while l < r:
                s = nums[l]+nums[r]
                if s < target:
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif s>target:
                    r-=1
                    while l<r and nums[r]== nums[r+1]:
                        r-=1
                else:
                    a.append([-target, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]== nums[r+1]:
                        r-=1

        return a
