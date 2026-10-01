class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        
        # Если весь массив нужно удалить
        if target == 0:
            return len(nums)
        
        # Если даже весь массив меньше x — невозможно
        if target < 0:
            return -1
        
        # Ищем самый длинный подмассив с суммой target
        prefix_sum = {0: -1}
        cur = 0
        max_len = -1
        
        for i, num in enumerate(nums):
            cur += num
            if cur - target in prefix_sum:
                max_len = max(max_len, i - prefix_sum[cur - target])
            if cur not in prefix_sum:
                prefix_sum[cur] = i
        
        return -1 if max_len == -1 else len(nums) - max_len