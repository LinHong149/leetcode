import math

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        power = 0
        while n / (k**(power+1)) >= 1:
            power += 1
        print("power is", power)

        sum = 0
        while n > 0:
            sum += n // k**power
            n = n % k**power
            power -= 1
        return sum
