class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] 
        for i in range(1, rowIndex + 1):  # Итеративно строим строки от 1 до rowIndex
            new_row = [1]  # Каждая новая строка начинается с 1
            for j in range(len(row) - 1):  # Проходим по парам соседних элементов текущей строки
                new_row.append(row[j] + row[j + 1])  # Вычисляем внутренний элемент как сумму двух соседних сверху
            new_row.append(1)  # Завершаем новую строку 1
            row = new_row
        return row 