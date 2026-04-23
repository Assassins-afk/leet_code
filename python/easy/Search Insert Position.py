class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) //2

            if nums[mid] == target:
                return mid# Нашли целевое значение
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid -1# Ищем в левой половине
         # Если не нашли, left указывает на место вставки
        return left