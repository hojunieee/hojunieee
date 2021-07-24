class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        dictionary = dict()
        dictionary[1] = "A"
        dictionary[2] = "B"
        dictionary[3] = "C"
        dictionary[4] = "D"
        dictionary[5] = "E"
        dictionary[6] = "F"
        dictionary[7] = "G"
        dictionary[8] = "H"
        dictionary[9] = "I"
        dictionary[10] = "J"
        dictionary[11] = "K"
        dictionary[12] = "L"
        dictionary[13] = "M"
        dictionary[14] = "N"
        dictionary[15] = "O"
        dictionary[16] = "P"
        dictionary[17] = "Q"
        dictionary[18] = "R"
        dictionary[19] = "S"
        dictionary[20] = "T"
        dictionary[21] = "U"
        dictionary[22] = "V"
        dictionary[23] = "W"
        dictionary[24] = "X"
        dictionary[25] = "Y"
        dictionary[26] = "Z"
        dictionary[0] = "Z"
        
        
        temp=columnNumber
        tsdigit = 0
        string =""

        while temp !=0:
            tsdigit = (temp % 26)
            string = dictionary[tsdigit] + string
            
            if tsdigit==0:
                temp =int(temp/26)-1
            else:
                temp =int(temp/26)
                
        return string