class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last — индекс последнего элемента в результирующем массиве nums1
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]: # Сравниваем текущие максимальные элементы из nums1 и nums2
                nums1[last] = nums1[m - 1] #Если элемент из nums1 больше, помещаем его в конец результирующего массива
                m -= 1# Уменьшаем счётчик оставшихся элементов в nums1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1 # Уменьшаем счётчик оставшихся элементов в nums2
            last -= 1 # Сдвигаем указатель last на одну позицию влево

        while n > 0: # Если после основного цикла остались элементы в nums2
            nums1[last] = nums2[n - 1] # Копируем оставшиеся элементы из nums2 в начало nums1
            n, last = n - 1, last - 1 # Уменьшаем оба счётчика