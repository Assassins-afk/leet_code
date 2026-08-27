class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        new_coins = []
        for x in coins:
            if all(x % y for y in new_coins):
                new_coins.append(x)
        coins = new_coins

        n = len(coins)
        m = 1 << n
        lcm = [1] * m

        left = k
        right = coins[0] * k + 1

        for mask in range(1, m):
            pre_mask = mask & (mask - 1)
            i = (mask & -mask).bit_length() - 1

            tmp = lcm[pre_mask] * coins[i] // math.gcd(lcm[pre_mask], coins[i])
            if tmp <= right:
                lcm[mask] = tmp
            else:
                lcm[mask] = right + 1

        def count(x: int) -> int:
            res = 0
            for mask in range(1, m):
                if mask.bit_count() % 2 == 1:
                    res += x // lcm[mask]
                else:
                    res -= x // lcm[mask]
            return res

        while left < right:
            mid = (left + right) // 2  
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left