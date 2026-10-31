class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        
        if sum(diffs) <= total_k:
            return 0
        
        cnt = Counter(diffs)
        
        for d in range(max(diffs), 0, -1):
            if d not in cnt:
                continue
            c = cnt[d]
            if total_k >= c:
                total_k -= c
                cnt[d - 1] = cnt.get(d - 1, 0) + c
                del cnt[d]
            else:
                cnt[d] = c - total_k
                cnt[d - 1] = cnt.get(d - 1, 0) + total_k
                total_k = 0
                break
        
        ans = 0
        for d, c in cnt.items():
            ans += c * d * d
        return ans