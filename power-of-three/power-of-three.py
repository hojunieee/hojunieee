class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n==1:
            return True
        elif n==0:
            return False
        elif n<0:
            return False
        
        while n>5:
            n=n/3
        if n==3.0:
            return True
        else:
            return False