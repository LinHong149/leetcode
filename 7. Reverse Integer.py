class Solution:
    def reverse(self, x: int) -> int:
        newX = 0
        count = 0
        flip = False

        if x < 0:
            x*=-1
            flip = True

        for i in range(10):
            newX *= 10
            digit = x%10
            x = x//10
            newX+=digit

            print(digit, x)

            if digit == 0:
                count +=1
            else:
                count = 0

        print(count,newX)
        if count:
            newX /= 10**count
        if flip:
            newX*=-1
            if newX < -(2**31):
                return 0
        if newX > 2**31 -1:
            return 0
        return(int(newX))


