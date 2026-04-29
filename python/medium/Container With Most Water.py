class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:  # Пока указатели не встретились
            area = (r - l) * min(height[l], height[r])  # Площадь = ширина * минимальная высота
            res = max(res, area)  # Обновляем максимум, если текущая площадь больше

            if height[l] < height[r]:  # Двигаем указатель с меньшей высотой
                l += 1  # Сдвигаем левый указатель вправо
            else:
                r -= 1  # Сдвигаем правый указатель влево
        return res  