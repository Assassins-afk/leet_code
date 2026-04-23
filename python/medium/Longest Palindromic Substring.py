class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Функция находит самый длинный палиндром в строке s.
        :param s: входная строка
        :return: самая длинная палиндромная подстрока
        """
        res = ""      # хранит найденный палиндром
        res_len = 0   # длина текущего максимального палиндрома

        for i in range(len(s)):  # проходим по каждому символу строки
            # Проверка нечётной длины палиндрома
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:  
                if (right - left + 1) > res_len:  # обновляем максимальный палиндром
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1

            # Проверка чётной длины палиндрома
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:  # аналогично предыдущему циклу
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1

        return res