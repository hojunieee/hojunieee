class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:
            return False
        else:
            while n%2==0:
                n=n/2
            
            if int(n)==1:
                return True
            else:
                return False
