class Solution:
    def reverse(self, x: int) -> int:
        V = str(x)
        if x==0:
            return 0
        elif x>0:
            L= len(V)
            ans= int(0)
            for i in range(L):
                temp = x%10
                ans = ans+ temp*10**(L-i-1)
                x= x//10
        else:
            x= abs(x)
            L= len(V)-1
            ans= int(0)
            for i in range(L):
                temp = x%10
                ans = ans+ temp*10**(L-i-1)
                x= x//10
            ans=-ans

        mina = -2**31  
        maxa = 2**31 - 1  
        if ans not in range(mina, maxa):  
            return 0
        else:
            return ans