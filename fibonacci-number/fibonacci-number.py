class Solution:
    def fib(self, n: int) -> int:
        import math

        def F(num):
            a= (1 + math.pow(5,0.5)) / 2
            return int((math.pow(a,num)-math.pow(-a,-num))/math.pow(5,0.5))

        if n==2:
            return 1
        
        else:
            return F(n-1)+F(n-2)