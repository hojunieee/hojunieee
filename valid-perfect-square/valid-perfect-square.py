class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        
        for i in range(65536):
            temp = i*i
            if temp == n :
                return True
        return False