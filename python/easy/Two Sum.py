class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for idx, num in enumerate(nums):
            desire = target - num
            if desire in numbers:
                return [numbers[desire], idx]
            numbers[num] = idx
