from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Result array and position pointer
        result = [0] * n
        pos = n - 1
        
        left, right = 0, n - 1
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        
        return result