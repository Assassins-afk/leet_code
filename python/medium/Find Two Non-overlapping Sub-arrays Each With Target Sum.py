class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        
        left = [INF] * n
        best = INF
        window_sum = 0
        start = 0
        
        for end in range(n):
            window_sum += arr[end]
            while window_sum > target:
                window_sum -= arr[start]
                start += 1
            if window_sum == target:
                best = min(best, end - start + 1)
            left[end] = best
        
        right = [INF] * n
        best = INF
        window_sum = 0
        end = n - 1
        
        for start in range(n - 1, -1, -1):
            window_sum += arr[start]
            while window_sum > target:
                window_sum -= arr[end]
                end -= 1
            if window_sum == target:
                best = min(best, end - start + 1)
            right[start] = best
        
        ans = INF
        for i in range(n - 1):
            if left[i] != INF and right[i + 1] != INF:
                ans = min(ans, left[i] + right[i + 1])
        
        return -1 if ans == INF else ans