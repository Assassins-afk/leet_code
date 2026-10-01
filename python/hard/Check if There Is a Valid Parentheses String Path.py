class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        memo = [[set() for _ in range(n)] for _ in range(m)]
        
        def dfs(i: int, j: int, bal: int) -> bool:
            bal += 1 if grid[i][j] == '(' else -1
            
            if bal < 0:
                return False
            
            steps_left = (m - 1 - i) + (n - 1 - j)
            if bal > steps_left:
                return False

            if i == m - 1 and j == n - 1:
                return bal == 0
            
            if bal in memo[i][j]:
                return False
            
            if i + 1 < m and dfs(i + 1, j, bal):
                return True
            if j + 1 < n and dfs(i, j + 1, bal):
                return True
            
            memo[i][j].add(bal)
            return False
        
        return dfs(0, 0, 0)