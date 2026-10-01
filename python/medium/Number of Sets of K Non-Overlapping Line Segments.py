class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        op = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(k + 1):
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
                op[i+1][j] = (op[i+1][j] + op[i][j]) % MOD
                op[i+1][j] = (op[i+1][j] + dp[i][j]) % MOD
                if j + 1 <= k:
                    dp[i+1][j+1] = (dp[i+1][j+1] + op[i][j]) % MOD
                    op[i+1][j+1] = (op[i+1][j+1] + op[i][j]) % MOD
        return dp[n][k] % MOD