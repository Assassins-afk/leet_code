class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""# создаем пустую строку для хранения римских чисел
        pairs = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]
        # перебираем пары
        for symbol, value in pairs:
            while num >= value: 
                result += symbol# добавляем символ
                num -= value# вычитаем значение
        return result
