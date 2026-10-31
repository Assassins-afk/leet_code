class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            seen.add((i, j))
            closed = 0 < i < n - 1 and 0 < j < m - 1
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni == n or nj < 0 or nj == m: continue
                if grid[ni][nj] == 1 or (ni, nj) in seen: continue
                if not dfs(ni, nj): closed = False
            return closed

        res = 0
        seen = set()
        for i in range(n):
            for j in range(m):
                if (i, j) in seen or grid[i][j] == 1: continue
                if dfs(i, j): res += 1
        return res