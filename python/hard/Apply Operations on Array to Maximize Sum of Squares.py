class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Считаем количество установленных битов на каждой позиции
        bit_count = [0] * 32
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    bit_count[b] += 1
        
        # Жадно строим k чисел: биты от старшего к младшему
        result_nums = [0] * k
        for b in range(31, -1, -1):
            cnt = min(bit_count[b], k)
            for i in range(cnt):
                result_nums[i] |= (1 << b)
        
        # Сумма квадратов по модулю
        ans = 0
        for num in result_nums:
            ans = (ans + num * num) % MOD
        
        return ans