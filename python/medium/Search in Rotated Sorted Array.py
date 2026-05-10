class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if  nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1   # ищем слева
                else:
                    left = mid + 1    # ищем справа
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1    # ищем справа
                else:
                    right = mid - 1   # ищем слева
        return -1