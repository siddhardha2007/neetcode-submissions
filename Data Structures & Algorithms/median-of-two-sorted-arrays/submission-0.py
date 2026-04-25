class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        for i in nums1:
            nums.append(i)
        for j in nums2:
            nums.append(j)
        x=sorted(nums)
        l=len(x)
        if l%2==0:
            median=(x[(l//2)-1]+x[l//2])/2
        else:
            median=x[(l//2)]
        return median        

        