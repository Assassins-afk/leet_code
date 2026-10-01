class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        
        # isPal[i][j] = True, если s[i..j] палиндром
        isPal = [[False] * n for _ in range(n)]
        
        # База: одиночные символы
        for i in range(n):
            isPal[i][i] = True
        
        # База: пары
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                isPal[i][i + 1] = True
        
        # Заполняем по длине
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and isPal[i + 1][j - 1]:
                    isPal[i][j] = True
        
        # dp[i] = максимум палиндромов в суффиксе s[i..]
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            # Вариант 1: пропустить символ i
            dp[i] = dp[i + 1]
            

            for j in range(i + k - 1, n):
                if isPal[i][j]:
                    dp[i] = max(dp[i], 1 + dp[j + 1])
                    break  
        
        return dp[0]