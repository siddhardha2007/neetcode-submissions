class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0   # reset when 0 comes
            
            maxones = max(maxones, count)
        
        return maxones