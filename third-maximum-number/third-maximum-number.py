class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        #Create a dict to eleminate the repetitions
        temp = dict()
        for i in nums:
            temp[i] = temp.get(i,0)+1
        
        #Sort the dict to get a list of keys
        temp = sorted(temp, reverse =True)

        #Return answer 
        if len(temp)<3:
            return temp[0]
        else:
            return temp[2]