class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-inf] * (k + 1) for _ in range(m)]for _ in range(n)]  # Трехмерный DP массив
        dp[0][0][0] = 0  # Начальная позиция

        for i in range(n):  # Перебираем строки
            for j in range(m):  # Перебираем столбцы
                for c in range(k + 1):  # Перебираем количество использованных ненулевых значений
                    if dp[i][j][c] == -inf: continue
                    if i + 1 < n:  # Если можно двигаться вниз
                        nv = grid[i + 1][j]  # Значение в клетке снизу
                        nc = 1 if nv != 0 else 0  # Увеличиваем счетчик ненулевых, если значение не ноль
                        if nc + c <= k:  
                            dp[i + 1 ][j][nc + c] = max(dp[i +1 ][j][nc + c], dp[i][j][c] + nv)  # Обновляем максимум для клетки снизу
                    if j + 1 < m:  # Если можно двигаться вправо
                        nv = grid[i][j + 1]  # Значение в клетке справа
                        nc = 1 if nv != 0 else 0 
                        if nc + c <= k:  # Проверяем, не превышает ли общее число ненулевых k
                            dp[i][j + 1][nc + c] = max(dp[i][j + 1][nc + c], dp[i][j][c] + nv)  # Обновляем максимум для клетки справа
        res = max(dp[-1][-1])  # Находим максимальный счет среди всех состояний в правом нижнем углу
        return res if res != -inf else -1  