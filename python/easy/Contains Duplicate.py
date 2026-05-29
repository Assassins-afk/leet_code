class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        know = set()
        for num in nums:
            if num in know:
                return True
            know.add(num)
        return False