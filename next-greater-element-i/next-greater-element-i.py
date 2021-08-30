class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]

        for i in nums1:
            a=nums2.index(i)
            for j in nums2[a:]:
                if j>i:
                    ans.append(j)
                    break
                elif j==nums2[len(nums2)-1]:
                    ans.append(-1)
                    break
        return ans