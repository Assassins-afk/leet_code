class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # проверка всех пробелов в начале 

        if not s:  # проверка пустой строки после удаления пробелов
            return 0

        i = 0
        sign = 1

        # Проверка является ли число отрицательным или положительным
        if s[i] == "+":
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        
        parsed = 0
        while i < len(s):  # проход по всем цифрам пока не встретится не цифра
            cur = s[i]

            if not cur.isdigit():  # проверка является ли текущий символ цифрой
                break
            else:
                parsed = parsed * 10 + int(cur)  # сдвиг числа влево и добавление новой цифры
                i += 1
        
        parsed *= sign  # применение знака к числу
        
        if parsed > 2**31 - 1:  # проверка верхней границы int32
            return 2**31 - 1
        elif parsed <= -2**31:  # проверка нижней границы int32
            return -2**31
        else:
            return parsed  