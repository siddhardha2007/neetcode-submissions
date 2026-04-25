class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            curr_sum=0
            for j in range(i, len(nums)):
                curr_sum=curr_sum+nums[j]
                res=max(res,curr_sum)
        return res         