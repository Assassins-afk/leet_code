class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        opt1 = nums[-1] * nums[-2] * nums[-3]
        opt2 = nums[0] * nums[1] * nums[-1]
        return max(opt1, opt2)