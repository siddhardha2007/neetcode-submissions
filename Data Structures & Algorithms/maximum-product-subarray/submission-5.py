class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=float('-inf')
        def product(x):
            product=1
            for i in x:
                product=product*i
                if product==0:
                    return 0
            return product    
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n+1):
                x=nums[i:j]
                a=product(x)
                max_product=max(max_product,a)
        return max_product        
                
        