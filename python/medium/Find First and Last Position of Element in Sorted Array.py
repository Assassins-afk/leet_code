class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        found = -1
        
        # Бинарный поиск первого вхождения
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                found = mid
                right = mid - 1  # Ищем левое вхождение
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Если элемент не найден
        if found == -1:
            return [-1, -1]
        
        # Находим последнее вхождение
        left, right = 0, len(nums) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last = mid
                left = mid + 1  # Ищем правое вхождение
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [found, last]