class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = len(nums)-1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                k = i


        if target < nums[0]:
            for i in range(len(nums)-1, k, -1):
                if nums[i] == target:
                    return i
        else:
            for i in range(k+1):
                if nums[i] == target:
                    return i

        return -1
