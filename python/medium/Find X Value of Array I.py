class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        prev = [0] * k
        
        for num in nums:
            val = num % k
            cur = [0] * k
            cur[val] += 1  
            
            for x in range(k):
                if prev[x] > 0:
                    new_x = (x * val) % k
                    cur[new_x] += prev[x]
            
            for x in range(k):
                result[x] += cur[x]
            
            prev = cur
        
        return result