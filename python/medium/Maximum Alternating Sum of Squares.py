from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(nums)
        neg = n // 2          
        
        small = sq[:neg]    
        big = sq[neg:]        
        
        return sum(big) - sum(small)