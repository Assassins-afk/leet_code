class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Длина входного массива
        res = [0] * n  
        s = []  

        for i in range(n):  # Проходим по всем элементам массива
            v = nums[i]  
            l, r = i, i  # Инициализируем левую и правую границы текущим индексом

            while s and s[-1][0] > nums[i]:  
                lastv, lastl, lastr = s.pop()  # Извлекаем последний элемент из стека
                v = max(v, lastv)  
                l = lastl  # Расширяем левую границу до левой границы извлечённого элемента
            s.append((v, l, r))  

        for v, l, r in s:  
            for i in range(l, r + 1):  # Для каждого индекса в диапазоне [l, r]
                res[i] = v  
        return res  