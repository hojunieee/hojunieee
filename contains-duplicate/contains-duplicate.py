class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ccc= dict()
        answer = False
        for i in nums:
            ccc[i] = ccc.get(i,0)+1
        
        for j in ccc.values():
            if j > 1:
                answer = True
        return answer