from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Получаем размеры массивов
        m, n = len(nums1), len(nums2)
        
        # Индексы текущих позиций в каждом массиве
        p1, p2 = 0, 0
    
        # Функция для получения следующего наименьшего элемента
        def get_min():
            nonlocal p1, p2
            
            # Проверяем оба массива одновременно
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:  # Берём меньший элемент
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            # Если второй массив исчерпан, берём из первого
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            # Иначе берём из второго
            else:
                ans = nums2[p2]
                p2 += 1
                
            return ans
    
        # Обрабатываем случай чётной суммы длин
        if (m + n) % 2 == 0:
            # Перемещаемся до предпоследнего центрального элемента
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            # Возвращаем среднее между двумя центральными элементами
            return (get_min() + get_min()) / 2
        else:
            # Для нечётной суммы перемещаемся ровно до центра
            for _ in range((m + n) // 2):
                _ = get_min()
            # Возвращаем единственный центральный элемент
            return get_min()