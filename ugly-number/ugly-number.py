class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        
        while n%2 ==0:
            n=int(n/2)
        while n%3 ==0:
            n=int(n/3)

        while n%5 ==0:
            n=int(n/5)

        if n==1:
            return True
        else:
            return False
            