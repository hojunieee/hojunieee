class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numofz = nums.count(0)
        for i in range(numofz):
            nums.remove(0)

        for i in range(numofz):
            nums.append(0)
        
        