class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # col_sum[j][h] — сумма значений в столбце j от строки 0 до h-1 (первые h клеток сверху)
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                col_sum[j][i + 1] = col_sum[j][i] + grid[i][j]

        INF = -10 ** 18
        # dp[i][j][0] — макс счёт для столбцов 0..i, высота j, вклад столбца i УЖЕ учтён
        # dp[i][j][1] — макс счёт для столбцов 0..i, высота j, вклад столбца i НЕ учтён (ждёт правого соседа)
        dp = [[[INF] * 2 for _ in range(n + 1)] for _ in range(n)]

        # Первый столбец: слева никого нет, счёт всегда 0 при любой высоте
        for j in range(n + 1):
            dp[0][j][0] = dp[0][j][1] = 0

        # Перебираем столбцы слева направо
        for i in range(1, n):
            # j — высота чёрной заливки в текущем столбце i
            for j in range(n + 1):

                # Белые клетки левого столбца в строках [k, j) получают чёрного соседа справа → платим за i-1
                for k in range(j + 1):
                    # dp[i-1][k][0] — вклад i-1 уже оплачен, dp[i-1][k][1] — платим сейчас: сумма в i-1 от k до j
                    best_prev = max(dp[i - 1][k][0],
                                    dp[i - 1][k][1] + col_sum[i - 1][j] - col_sum[i - 1][k])
                    dp[i][j][0] = max(dp[i][j][0], best_prev)
                    dp[i][j][1] = max(dp[i][j][1], best_prev)

                # Белые клетки текущего столбца в строках [j, k) получают чёрного соседа слева → платим за i
                for k in range(j + 1, n + 1):
                    # Берём только состояние 0 (столбец i-1 уже оплачен), добавляем сумму в i от j до k
                    base = dp[i - 1][k][0]
                    dp[i][j][0] = max(dp[i][j][0], base + col_sum[i][k] - col_sum[i][j])  # платим за i сейчас
                    dp[i][j][1] = max(dp[i][j][1], base)  # оставляем i неоплаченным, заплатит правый сосед

        # Последний столбец обязан быть оплачен (state=0), так как справа соседа нет
        return max(dp[n - 1][j][0] for j in range(n + 1))