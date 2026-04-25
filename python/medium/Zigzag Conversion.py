class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Если всего одна строка - зигзаг не нужен, возвращаем строку как есть
        if numRows == 1: 
            return s

        res = ""  # Результирующая строка
        
        # Проходим по каждой строке зигзага (0, 1, 2, ..., numRows-1)
        for r in range(numRows):
            # Шаг между главными столбцами в зигзаге
            increment = 2 * (numRows - 1)
            
            # i - индекс символа в исходной строке
            for i in range(r, len(s), increment):
                # Вертикальная часть зигзага (всегда есть)
                res += s[i]
                
                # Диагональная часть (для внутренних строк, не первой и не последней)
                # Проверяем, что символ существует в пределах строки
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):   
                    # Добавляем символ на диагонали
                    res += s[i + increment - 2 * r]
                    
        return res