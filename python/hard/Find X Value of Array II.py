class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        # Инициализация листьев (только реальные элементы)
        for i in range(n):
            v = nums[i] % k
            prod[size + i] = v
            cnt[size + i][v] = 1
        # Пустые листья: prod=1, cnt=[0]*k (нейтральные)

        def pull(i):
            left = 2 * i
            right = 2 * i + 1
            prod[i] = (prod[left] * prod[right]) % k
            ci = cnt[i]
            cl = cnt[left]
            cr = cnt[right]
            for r in range(k):
                ci[r] = cl[r]
            pl = prod[left]
            for pr in range(k):
                c = cr[pr]
                if c:
                    ci[(pl * pr) % k] += c

        for i in range(size - 1, 0, -1):
            pull(i)

        def update(idx, value):
            pos = size + idx
            v = value % k
            for r in range(k):
                cnt[pos][r] = 0
            prod[pos] = v
            cnt[pos][v] = 1
            pos //= 2
            while pos >= 1:
                pull(pos)
                pos //= 2

        def merge(prod1, cnt1, prod2, cnt2):
            new_prod = (prod1 * prod2) % k
            new_cnt = [0] * k
            for r in range(k):
                new_cnt[r] = cnt1[r]
            for pr in range(k):
                c = cnt2[pr]
                if c:
                    new_cnt[(prod1 * pr) % k] += c
            return new_prod, new_cnt

        def query(l, r):
            # Нейтральные аккумуляторы: пустой сегмент
            left_prod = 1
            left_cnt = [0] * k

            right_prod = 1
            right_cnt = [0] * k

            l += size
            r += size
            while l <= r:
                if l % 2 == 1:
                    left_prod, left_cnt = merge(left_prod, left_cnt, prod[l], cnt[l])
                    l += 1
                if r % 2 == 0:
                    right_prod, right_cnt = merge(prod[r], cnt[r], right_prod, right_cnt)
                    r -= 1
                l //= 2
                r //= 2
            return merge(left_prod, left_cnt, right_prod, right_cnt)

        res = []
        for idx, val, start, x in queries:
            update(idx, val)
            _, c = query(start, n - 1)
            res.append(c[x])
        return res