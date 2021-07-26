class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        a=str(math.factorial(n))
        i=0

        while a[len(a)-1] == "0":
            i=i+1
            a=a[:len(a)-1]
            
        return i