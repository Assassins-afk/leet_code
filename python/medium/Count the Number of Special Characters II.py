class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastlower = {} 
        firstupper = {}  

        for i, c in enumerate(word):  # Проходим по строке с индексами
            if c.islower(): lastlower[c] = i  # Обновляем последнюю позицию для строчной буквы
            elif not c in firstupper: firstupper[c] = i  # Сохраняем первое вхождение заглавной буквы (только если еще не встречали)
        
        res = 0  # Счетчик "особых" символов
        for i in range(26):  # Проверяем все буквы алфавита
            c = chr(i + ord('a'))  # Получаем строчную букву по индексу
            if (
                c in lastlower and  # Строчная буква встречалась в слове
                c.upper() in firstupper and  # Соответствующая заглавная буква тоже встречалась
                lastlower[c] < firstupper[c.upper()]  # Последнее вхождение строчной буквы находится до первого вхождения заглавной
            ) : res += 1  
        
        return res 