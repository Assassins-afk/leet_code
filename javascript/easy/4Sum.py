class Solution:
    def two_sum(self, start: int, target: int) -> None:
        nums = self.nums  
        left = start  # Левый указатель начинается с позиции start
        right = len(nums) - 1  # Правый указатель начинается с конца массива

        while left < right:  # Пока указатели не встретились
            left_value = nums[left]  # Значение левого элемента
            right_value = nums[right]  # Значение правого элемента
            val = left_value + right_value  # Сумма двух элементов
            if val < target:  
                left += 1
            elif val > target:
                right -= 1
            else:  # Нашли пару, сумма равна цели
                self.results.append(self.prefix + [left_value, right_value])  # Добавляем комбинацию в результаты
                left += 1  # Сдвигаем левый указатель
                while left < right and nums[left] == nums[left - 1]:  # Пропускаем дубликаты слева
                    left += 1  

    def k_sum(self, k: int, start: int, target: int) -> None:
        if k == 2:  #+ если осталось найти 2 числа, используем метод двух указателей
            self.two_sum(start, target) 
            return

        nums = self.nums  # Получаем отсортированный массив
        for idx in range(start, len(nums) - k + 1):  # Перебираем элементы, оставляя место для k-1 элементов
            if idx > start and nums[idx] == nums[idx - 1]:  # Пропускаем дубликаты для избежания повторных комбинаций
                continue
            value = nums[idx]  # Текущее значение
            self.prefix.append(value)  # Добавляем значение в префикс текущей комбинации
            self.k_sum(k - 1, idx + 1, target - value)  # Рекурсивно ищем оставшиеся k-1 чисел с новой целью
            self.prefix.pop()  # Удаляем значение из префикса (backtracking)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Сортируем массив для работы с указателями и пропуска дубликатов
        self.nums = nums  # Сохраняем отсортированный массив
        self.prefix = []  # Инициализируем список для хранения текущей комбинации
        self.results = []  # Инициализируем список для хранения всех найденных комбинаций
        self.k_sum(4, 0, target)  # Запускаем рекурсивный поиск 4 чисел
        return self.results