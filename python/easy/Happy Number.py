class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()  

        while n not in visit:  # Продолжаем, пока число не повторится (не войдём в цикл)
            visit.add(n)  # Добавляем текущее число в посещённые
            n = self.sumOfSquares(n)  # Заменяем число суммой квадратов его цифр

            if n == 1: 
                return True
        
        return False  

    def sumOfSquares(self, n: int) -> int:
        output = 0  

        while n:  # Пока в числе есть цифры (n > 0)
            digit = n % 10  # Извлекаем последнюю цифру числа
            digit = digit ** 2  # Возводим цифру в квадрат
            output += digit  
            n = n // 10  # Убираем последнюю цифру числа (целочисленное деление)
        return output  