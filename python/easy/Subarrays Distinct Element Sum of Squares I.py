class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            curr = set()
            for j in range(i, n):
                curr.add(nums[j])
                res += len(curr)**2

        return res