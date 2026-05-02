class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)

        valid_digits = {0, 1, 2, 5, 6, 8, 9}#цифры, которые остаются цифрами после поворота
        changing_digits = {2, 5, 6, 9}#цифры, которые меняются на другую цифру
        @lru_cache(None)
        def dp(pos, tight, has_changing):
            if pos == len(s):
                return 1 if has_changing else 0

            # Определяем limit
            limit = int(s[pos]) if tight else 9
            total= 0

            # Перебираем цифры
            for d in range(limit + 1):
                if d not in valid_digits:
                    continue

                next_tight = tight and (d == limit)
                next_has_changing = has_changing or (d in changing_digits)

                total += dp(pos + 1, next_tight, next_has_changing)
                
            return total

        return dp(0, True, False)