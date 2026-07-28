class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i-1] * 10 % MOD

        sum_arr = [0] * (n + 1)    
        cnt = [0] * (n + 1)      
        x = [0] * (n + 1)          
        
        for i, c in enumerate(s):
            d = int(c)
            cnt[i + 1] = cnt[i] + (d > 0)

            if d > 0:
                x[i + 1] = (x[i] * 10 + d) % MOD
                sum_arr[i + 1] = sum_arr[i] + d    
            else:
                x[i + 1] = x[i]
                sum_arr[i + 1] = sum_arr[i]      

        res = [0] * len(queries)
        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][1] + 1

            length = cnt[r] - cnt[l]

            if length == 0:
                res[i] = 0
            else:
                x_val = (x[r] - x[l] * pow10[length]) % MOD
                s_val = sum_arr[r] - sum_arr[l]
                res[i] = (x_val * s_val) % MOD

        return res