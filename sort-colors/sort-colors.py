class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(3):
            for i in nums:
                if i ==j:
                    nums.remove(i)
                    nums.append(i)
                    