class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 37  # Максимально возможная сумма цифр 
        for num in nums:  # Перебираем каждое число в массиве
            dig = 0  
            while num > 0:
                dig += num % 10  # Прибавляем последнюю цифру к сумме
                num //= 10  # Отбрасываем последнюю цифру числа
            ans = min(ans, dig)  
        return ans 