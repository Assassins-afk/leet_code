class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Сортируем массив для работы двух указателей
        closest = float('inf')  # Инициализируем ближайшую сумму как бесконечность
        
        for i in range(len(nums)-2):  # Фиксируем первый элемент тройки (до 3-го с конца)
            left = i + 1  # Левый указатель — следующий после фиксированного
            right = len(nums) - 1  # Правый указатель — конец массива

            while left < right:  # Ищем пару для фиксированного элемента
                current_sum = nums[i] + nums[left] + nums[right]  # Текущая сумма тройки
                if abs(current_sum - target) < abs(closest - target):  # Обновляем ближайшую сумму если нашли лучше
                    closest = current_sum

                if current_sum < target:  # Сумма мала 
                    left += 1
                elif current_sum > target:  # Сумма велика
                    right -= 1
                else:  # Точное совпадение
                    return target

        return closest