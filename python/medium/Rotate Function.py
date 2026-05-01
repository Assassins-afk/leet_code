class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total_sum = sum(nums) 
        n = len(nums)
        ans = val = sum(i * val for i, val in enumerate(nums))  # Начальное значение F(0) как суммы i * nums[i]
        for i in range(n - 1, -1, -1):  # Идем с конца массива
            val = val + total_sum - n * nums[i]
            ans = max(ans, val)  # Обновляем максимум среди всех поворотов
        return ans 