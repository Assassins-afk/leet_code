class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 == arr2, arr1
        
        prefix_set = set()
        for n in arr1:
            while n:
                prefix_set.add(n)  # Добавляем все префиксы числа (само число и его усечения) в множество
                n = n // 10  # Убираем последнюю цифру, получая следующий префикс

        res = 0
        for n in arr2:
            while n and n not in prefix_set:  # Пока число не ноль и его нет в множестве префиксов, усекаем его
                n = n // 10

            if n in prefix_set:  # Если нашли совпадающий префикс, обновляем максимальную длину
                res = max(res, len(str(n)))
        return res