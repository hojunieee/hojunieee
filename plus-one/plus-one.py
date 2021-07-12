class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string =""
        
        for i in digits:
            string = string + str(i)
        
        intString = int(string)
        intString = intString + 1
        string = str(intString)
        
        ansList = []
        
        for i in range(len(string)):
            a = int(string[i])
            ansList.append(a)
        
        return ansList
            