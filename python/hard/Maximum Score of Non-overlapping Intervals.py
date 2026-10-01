class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        indexed = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        starts = [x[0] for x in indexed]

        @cache
        def dp(i: int, rem: int):
            if rem == 0 or i == n:
                return (0, ())

            skip_w, skip_idx = dp(i + 1, rem)


            l, r, w, orig_i = indexed[i]

            nexti = bisect_left(starts, r + 1)
            next_w, next_idx = dp(nexti, rem - 1)
            take_w = w + next_w
            take_idx = tuple(sorted(next_idx + (orig_i,)))

            if take_w > skip_w:
                return (take_w, take_idx)
            if take_w < skip_w:
                return (skip_w, skip_idx)

            if take_idx < skip_idx:
                return (take_w, take_idx)
            return (skip_w, skip_idx)

        return list(dp(0, 4)[1])