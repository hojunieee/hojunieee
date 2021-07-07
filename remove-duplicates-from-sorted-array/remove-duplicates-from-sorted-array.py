class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        temp = nums[0]
        maxnum = nums[len(nums) - 1] 
        counter = 0
        i=0
        
        while temp != maxnum+1:
            if temp == maxnum:
                break
            if nums[counter+1] == temp:
                del nums[counter]
            else:
                while nums[counter+1] != temp:
                    temp = temp + 1
                counter = counter + 1
                
        nums[:] = (value for value in nums if value != maxnum)
        nums.append(maxnum)

        return counter+1