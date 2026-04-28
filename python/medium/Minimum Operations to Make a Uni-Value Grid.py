class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. Проверяем, что у всех чисел одинаковый остаток от деления на x
        #    (иначе невозможно привести все числа к одному значению)
        # 2. Превращаем матрицу в плоский список и сортируем
        # 3. Используем префиксные/суффиксные суммы для вычисления стоимости

        for row in grid:
            for n in row:
                # Сравниваем остаток каждого числа с остатком первого элемента
                if n % x != grid[0][0] % x:
                    return -1

        # Превращаем матрицу в список и сортируем по возрастанию
        nums = sorted([n for row in grid for n in row])

        prefix = 0        # Нарастающая сумма элементов слева от текущего
        total = sum(nums) # Общая сумма всех элементов
        res = float('inf') # Изначально ответ — бесконечность

        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix
            cost_right = total - prefix - (nums[i] * (len(nums) - i))
            operations = (cost_left + cost_right) // x
            
            res = min(res, operations) # Запоминаем лучший результат
            
            prefix += nums[i] # Добавляем текущий элемент в префикс для следующей итерации
            
        return res