class Solution:
    def romanToInt(self, s: str) -> int:
        temp = 0
        if s.find("CM") != -1:
            temp = temp+900
            s=s.replace("CM", "")
            
        if s.find("M") != -1:
            temp = temp+(s.count("M")*1000)
            s=s.replace("M", "")
            
        
        if s.find("CD") != -1:
            temp = temp+400
            s=s.replace("CD", "")
        else:
            temp = temp+(s.count("D")*500)
            s=s.replace("D", "")
        
        
        if s.find("XC") != -1:
            temp = temp+90
            s=s.replace("XC", "")
        
        if s.find("C") != -1:
            temp = temp+(s.count("C")*100)
            s=s.replace("C", "")
            
        
        if s.find("XL") != -1:
            temp = temp+40
            s=s.replace("XL", "")
        else:
            temp = temp+(s.count("L")*50)
            s=s.replace("L", "")
        
        
        if s.find("IX") != -1:
            temp = temp+9
            s=s.replace("IX", "")
        
        if s.find("X") != -1:
            temp = temp+(s.count("X")*10)
            s=s.replace("X", "")
        
        
        if s.find("IV") != -1:
            temp = temp+4
            s=s.replace("IV", "")
        else:
            temp = temp+(s.count("V")*5)
            s=s.replace("V", "")
        
        temp = temp+(s.count("I")*1)
        
        return temp