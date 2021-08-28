class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans =list()
        for i in numbers:
            if target-i in numbers:
                first = numbers.index(i)
                ans.append(first+1)
                
                numbers.remove(i)
    
                second = numbers.index(target-i)
                ans.append(second+2)
                break
        return ans