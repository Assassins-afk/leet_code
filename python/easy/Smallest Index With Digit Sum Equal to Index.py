from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # Считаем сумму цифр числа
            digit_sum = sum(int(d) for d in str(num))
            
            # Если сумма цифр равна индексу — возвращаем индекс
            if digit_sum == i:
                return i
        
        # Если подходящего индекса нет
        return -1
        