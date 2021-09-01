class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        values, ans = set(nums), []
        for i in range(1,len(nums)+1):
            if i not in values: ans.append(i)
        return ans
        
        return ans