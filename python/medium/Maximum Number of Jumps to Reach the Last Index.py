class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache  # Мемоизация результатов DFS для избежания повторных вычислений
        def dfs(i: int):
            if i == len(nums) - 1:  #достигли последнего индекса
                return 0
            res = -inf  # Инициализация результата как минус бесконечность для максимизации
            for j in range(i + 1, len(nums)):  # Перебор всех возможных следующих индексов
                if abs(nums[i] - nums[j]) <= target:  # Проверка допустимости прыжка по условию
                    res = max(res, dfs(j) + 1)  # Рекурсивный вызов с увеличением счётчика прыжков
            return res 
        
        ans = dfs(0)  # Запуск DFS с начального индекса 0
        return -1 if ans < 0 else ans  