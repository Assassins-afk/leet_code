class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
         # Получаем длины строк
        h_len = len(haystack)
        n_len = len(needle)

         # Получаем длины строк
        if n_len > h_len:
            return -1

        # Получаем длины строк
        for i in range(h_len - n_len +1):
             # Получаем длины строк
            if haystack[i:i + n_len] == needle:
                return i  # Получаем длины строк
        # Если ничего не нашли
        return -1