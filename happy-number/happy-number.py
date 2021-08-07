class Solution:
    def isHappy(self, n: int) -> bool:
        import math
        temp =n
        ccc=dict()
        ccc[1] = 1

        def Convert(num):
            temp = 0
            a = str(num)
            #square each digit, then retuen sum  
            for i in range(len(a)):
                temp = temp +math.pow(int(a[i]),2)
            return int(temp)

        maxrepeat =0
        while maxrepeat < 2:
            temp = Convert(temp)
            ccc[temp] = ccc.get(temp,0)+1
            maxrepeat = max(ccc.values())

        if temp ==1:
            return True
        else:
            return False
