class Solution:
    def addDigits(self, num: int) -> int:
        strnum=""
        strnum=str(num)


        while len(str(num)) != 1:
            summ = 0
            strnum=str(num)
            for i in strnum:
                summ =summ + int(i)
            num = summ
        
        return num