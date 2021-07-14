class Solution:
    def addBinary(self, a: str, b: str) -> str:
        atemp = 0
        btemp = 0
        maxlen = max(len(a),len(b)) + 1
        ansinbinary = ""
        
        for i in range(len(a)):
            atemp = atemp + (2**i)*int(a[len(a)-1-i])
        
        for j in range(len(b)):
            btemp = btemp + (2**j)*int(b[len(b)-1-j])
            
        ansindecimal = atemp + btemp
        
        if ansindecimal == 0:
            return "0"
        if ansindecimal == 1:
            return "1"
        
        for i in range(maxlen,-1,-1):
            if ansindecimal >= (2**i):
                ansinbinary = ansinbinary + "1"
                ansindecimal =ansindecimal - 2**i
  
            else:
                ansinbinary = ansinbinary + "0"

        while ansinbinary.find("0")==0:
            ansinbinary = ansinbinary[1:]
        
        return ansinbinary