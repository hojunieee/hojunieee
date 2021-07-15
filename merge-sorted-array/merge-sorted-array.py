class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr1=nums1
        arr2=nums2
        ans=[0]*(n+m)
        i=0
        j=0
        k=0
        while i<m and j<n:
            if arr1[i]<arr2[j]:
                ans[k]=arr1[i]
                k+=1
                i+=1
            else:
                ans[k]=arr2[j]
                k+=1
                j+=1
        while i<m:
            ans[k]=arr1[i]
            k+=1
            i+=1
        while j<n:
            ans[k]=arr2[j]
            k+=1
            j+=1
        for i in range(n+m):
            nums1[i]=ans[i]
        return nums1