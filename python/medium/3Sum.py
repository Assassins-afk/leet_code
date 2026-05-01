class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = [] 
        nums.sort()  # Сортируем массив для использования двух указателей
        
        for i, a in enumerate(nums):  # Перебираем каждый элемент как первый в тройке
            if i and a == nums[i - 1]:  # Пропускаем дубликаты первого элемента
                continue

            left = i + 1  # Левый указатель начинается сразу после текущего элемента
            right = len(nums) - 1  # Правый указатель начинается с конца массива
            while left < right:  # Поиск пары для текущего первого элемента
                three_sum = a + nums[left] + nums[right]  # Вычисляем сумму тройки
                if three_sum < 0:  # Если сумма меньше нуля, сдвигаем левый указатель вправо
                    left += 1
                elif three_sum > 0:  # Если сумма больше нуля, сдвигаем правый указатель влево
                    right -= 1
                else:
                    result.append([a, nums[left], nums[right]]) 
                    left += 1  # Сдвигаем левый указатель для поиска новых комбинаций
                    while nums[left] == nums[left - 1] and left < right:  # Пропускаем дубликаты второго элемента
                        left += 1

        return result