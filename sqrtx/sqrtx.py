class Solution:
    def mySqrt(self, x: int) -> int:
        a=0
        i=0
        while a <= x:
            i=i+1
            a=i*i
        return i-1