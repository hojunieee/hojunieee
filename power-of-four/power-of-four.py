class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==1:
            return True
        elif n==0:
            return False
        elif n<0:
            return False
        
        while n>5:
            n=n/4
        if n==4.0:
            return True
        else:
            return False