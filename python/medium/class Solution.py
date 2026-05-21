class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(i):
            if i < 0 or i >= n or i in seen: return False  # Выход за границы или уже посещённая вершина - False
            if arr[i] == 0: return True  # Достигнут индекс со значением 0 - True
            seen.add(i) 
            return dfs(i + arr[i]) or dfs(i - arr[i])  # Рекурсивно проверяем оба возможных прыжка

        seen = set()  # Множество для отслеживания посещённых индексов
        n = len(arr)  # Длина массива для проверки границ
        return dfs(start)class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(i):
            if i < 0 or i >= n or i in seen: return False  # Выход за границы или уже посещённая вершина - False
            if arr[i] == 0: return True  # Достигнут индекс со значением 0 - True
            seen.add(i) 
            return dfs(i + arr[i]) or dfs(i - arr[i])  # Рекурсивно проверяем оба возможных прыжка

        seen = set()  # Множество для отслеживания посещённых индексов
        n = len(arr)  # Длина массива для проверки границ
        return dfs(start)