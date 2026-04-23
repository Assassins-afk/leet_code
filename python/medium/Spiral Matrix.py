class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def insideMatrixAndNotNone(i, j):
            return (0<=i<m) and (0<=j<n) and (matrix[i][j] != None)
            # Проверяем находятся ли индекс и ячейки внутри матрицы,
            #и не были ли они уже поищены

        m, n = len(matrix), len(matrix[0])
        result = [] #сохраняем результат 
        i, j = 0, 0 # Первая ячейка
        diri, dirj = 0, 1

        while True:
            result.append(matrix[i][j]) # текущий элмент результата
            matrix[i][j] = None # очищаем ее

            nexti = i + diri
            nextj = j + dirj
            if insideMatrixAndNotNone(nexti, nextj): # Проверяем находятся ли следующие функции есть ли они в матрице или не были ли они уже посищены
                i = nexti
                j = nextj
            else: # В противном случае нам нужно повернуть на право
                diri, dirj = dirj, -diri
                i += diri
                j += dirj
                if not insideMatrixAndNotNone(i, j):# Проверяем можем ли мы двигаться дальше после поворота на право, если нет то мы дошли до конца
                    break
        return result
