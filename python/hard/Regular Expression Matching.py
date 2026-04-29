class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] - совпадают ли первые i символов s с первыми j символами p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Пустая строка == пустой шаблон
        dp[0][0] = True

        # Пустая строка vs шаблон (может совпасть только если шаблон можно обнулить через *)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # пропускаем "X*"

        # Заполняем таблицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sc, pc = s[i - 1], p[j - 1]

                if pc == '.' or pc == sc:
                    # Символы совпали -> смотрим предыдущий результат
                    dp[i][j] = dp[i - 1][j - 1]
                elif pc == '*':
                    # Вариант 1: ноль повторений "X*"
                    dp[i][j] = dp[i][j - 2]
                    # Вариант 2: одно+ повторений, если символ перед * совпадает
                    if p[j - 2] == '.' or p[j - 2] == sc:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]