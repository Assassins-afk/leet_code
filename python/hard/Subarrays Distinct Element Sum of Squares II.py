MOD = 10**9 + 7

class ST:
    def __init__(self, n):
        self.st = [[0, 0, 0] for _ in range(4 * n)]

    def apply(self, node, l, r, val):
        s, sq, lazy = self.st[node]
        length = r - l + 1
        self.st[node][0] = (s + length * val) % MOD
        self.st[node][1] = (sq + 2 * val * s + length * val ** 2) % MOD
        self.st[node][2] += val

    def update(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            self.apply(node, l, r, 1)
            return
        lazy = self.st[node][2]
        mid = (l + r) // 2
        if lazy > 0 and l != r:
            self.apply(node * 2, l, mid, lazy)
            self.apply(node * 2 + 1, mid + 1, r, lazy)
        self.st[node][2] = 0

        if ql <= mid: 
            self.update(node * 2, l, mid, ql, qr)
        if qr > mid: 
            self.update(node * 2 + 1, mid + 1, r, ql, qr)
            
        left = self.st[node * 2]
        right = self.st[node * 2 + 1]
        self.st[node][0] = (left[0] + right[0]) % MOD
        self.st[node][1] = (left[1] + right[1]) % MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        st = ST(n)
        last = {}
        res = 0

        for i, num in enumerate(nums):
            p = last.get(num, -1)
            st.update(1, 0, n - 1, p + 1, i)
            res = (res + st.st[1][1]) % MOD
            last[num] = i

        return res