class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp =int()
        for i in range(len(nums)+1):
            if i not in nums:
                temp = i
        return temp