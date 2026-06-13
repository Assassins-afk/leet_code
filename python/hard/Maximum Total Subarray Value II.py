class ST:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.st = [(0, 0) for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.st[node] = (self.arr[l], self.arr[l])
            return
    
        mid = l + (r - l) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)
        self.st[node] = (
            max(self.st[node * 2][0], self.st[node * 2 + 1][0]),
            min(self.st[node * 2][1], self.st[node * 2 + 1][1])
        )

    def query(self, ql, qr, node = 1, l = 0, r = None):
        if r is None: r = self.n - 1

        if ql > r or qr < l:
            return (-inf, inf)

        if ql <= l and qr >= r:
            return self.st[node]

        mid = l + (r - l) // 2
        lmx, lmn = self.query(ql, qr, node * 2, l, mid)
        rmx, rmn = self.query(ql, qr, node * 2 + 1, mid + 1, r)
        return (
            max(lmx, rmx),
            min(lmn, rmn)
        )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = ST(nums)
        mh = []

        mx, mn = st.query(0, n - 1)
        heapq.heappush(mh, (-(mx - mn), 0, n - 1))
        seen = set()
        seen.add((0, n - 1))
        res = 0

        while k:
            k -= 1
            v, l, r = heapq.heappop(mh)
            v = -v
            res += v

            if l + 1 <= r and (l + 1, r) not in seen:
                mx, mn = st.query(l + 1, r)
                heapq.heappush(mh, (-(mx - mn), l + 1, r))
                seen.add((l + 1, r))
            if r - 1 >= l and (l, r - 1) not in seen:
                mx, mn = st.query(l, r - 1)
                heapq.heappush(mh, (-(mx - mn), l, r - 1))
                seen.add((l, r - 1))

        return res