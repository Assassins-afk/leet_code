class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A) 
        prefix_common_array = [0] * n 

        for current_index in range(n):  # Перебираем текущий индекс префикса от 0 до n-1
            common_count = 0  
            for a_index in range(current_index + 1):  # Перебираем элементы в префиксе A от 0 до current_index
                for b_index in range(current_index + 1):  # Перебираем элементы в префиксе B от 0 до current_index
                    if A[a_index] == B[b_index]:  # Если нашли совпадение элемента из A с элементом из B
                        common_count += 1 
                        break  

            prefix_common_array[current_index] = common_count  # Записываем количество общих элементов для префикса

        return prefix_common_array  