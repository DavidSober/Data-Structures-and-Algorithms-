# beats 63% in time and 91% in space

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            return int(n/2)
        else:
            return n