class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1  

        while(l < r):  # Продолжаем поиск, пока указатели не сойдутся
            mid = (l + r) // 2  # Находим средний индекс
            if nums[mid] > nums[r]: 
                l = mid + 1  # Сдвигаем левую границу
            elif nums[mid] < nums[l]:  
                r = mid  # Сдвигаем правую границу
            else:  
                r -= 1  # Уменьшаем правую границу на 1 для обработки дубликатов

        return nums[l]  