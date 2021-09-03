class Solution:
    def countBits(self, n: int) -> List[int]:
        ccc =[]

        if n==0:
            return [0]

        def decimalToBinary(n):
            return bin(n).replace("0b", "")
  
        for i in range(n+1):
            temp=decimalToBinary(i)
            a=0
            for i in temp:
                if i=='1':
                    a=a+1
            ccc.append(a)

        return ccc