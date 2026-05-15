class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1
        filtered = ''

        #2
        for char in s:                          # перебираем каждый символ
            if char.isalnum():                  # проверяем: буква или цифра?
                filtered = filtered + char.lower()  # добавляем в нижнем регистре

        return filtered == filtered[::-1] # сравниваем с перевёрнутой

        