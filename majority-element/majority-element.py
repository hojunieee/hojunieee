class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        aaa =dict()
        length = len(nums)
        for num in nums:
            aaa[num] = aaa.get(num,0)+1
        
        bbb = sorted(aaa.items(), key=lambda x: x[1], reverse=True)

        return bbb[0][0]