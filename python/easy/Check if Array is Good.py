from collections import Counter  

class Solution:  
    def isGood(self, nums: List[int]) -> bool:  
        n = max(nums) 

        if len(nums) != n + 1:  # Проверяем, что длина массива равна n+1 
            return False 

        count = Counter(nums)  # Подсчитываем частоту каждого числа в массиве

        for i in range(1, n):  # Проходим по всем числам от 1 до n-1
            if count.get(i, 0) != 1:  # Каждое число от 1 до n-1 должно встречаться ровно 1 раз
                return False  
        if count.get(n, 0) != 2:  # Число n должно встречаться ровно 2 раза
            return False  
        if len(count) != n:  # Проверяем, что в массиве присутствуют числа ровно от 1 до n (нет посторонних чисел)
            return False 
        return True  