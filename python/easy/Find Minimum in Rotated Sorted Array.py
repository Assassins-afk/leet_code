class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Если массив не ротирован или ротирован n раз
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Сравниваем с правым элементом
            if nums[mid] > nums[right]:
                # Минимум в правой половине
                left = mid + 1
            else:
                # Минимум в левой половине (включая mid)
                right = mid
        
        return nums[left]