class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if len(nums) <= 1:
                if target < nums[0]:
                    return 0
                else:
                    return 1
            elif target < nums[0]:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            else:
                for x in range(len(nums)-1):
                    if target in range(nums[x], nums[x+1]):
                        return x+1