class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums=sorted(nums)
        res=[]
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        if [nums[i],nums[j],nums[k]] not in res:
                            res.append([nums[i],nums[j],nums[k]])
        return res                    
                        
             

        