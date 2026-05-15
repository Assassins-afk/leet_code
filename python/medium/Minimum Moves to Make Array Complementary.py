class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)  # Массив разностей для хранения изменений количества операций

        for i in range(n // 2):  # Проходим по всем парам чисел с концов массива
            a = nums[i]  
            b = nums[n - 1 - i]  

            curr_sum = a + b  # Текущая сумма пары
            min_sum = min(a, b) + 1  
            max_sum = max(a, b) + limit  

            diff[2] += 2  
            diff[2 * limit + 1] -= 2  

            diff[min_sum] -= 1  
            diff[max_sum + 1] += 1  

            diff[curr_sum] -= 1  
            diff[curr_sum + 1] += 1  

            curr_moves = 0  
            min_moves = float('inf')  # Минимальное количество операций

        for target_sum in range(2, 2 * limit + 1):  # Перебираем все возможные целевые суммы
            curr_moves += diff[target_sum]  # Обновляем текущее количество операций через разностный массив
            min_moves = min(min_moves, curr_moves)  # Находим минимум

        return min_moves  