class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        middle = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                more.append(i)

        # print(less, middle, more)
        return(less+middle+more)
