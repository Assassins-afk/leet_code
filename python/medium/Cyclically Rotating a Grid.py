class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])  # Получаем размеры матрицы: m строк, n столбцов
        nlayer = min(m // 2, n // 2)  # Вычисляем количество слоёв для обхода

        for layer in range(nlayer):  # Обрабатываем каждый слой от внешнего к внутреннему
            r = [] 
            c = [] 
            val = [] 
            for i in range(layer, m - layer - 1):  # Проходим по левому столбцу сверху вниз
                r.append(i)  
                c.append(layer)  
                val.append(grid[i][layer]) 
            for j in range(layer, n - layer - 1):  # Проходим по нижней строке слева направо
                r.append(m - layer - 1)  
                c.append(j)  
                val.append(grid[m - layer - 1][j])  #
            for i in range(m - layer - 1, layer, - 1):  # Проходим по правому столбцу снизу вверх
                r.append(i) 
                c.append(n - layer - 1) 
                val.append(grid[i][n - layer - 1])  
            for j in range(n - layer - 1, layer, -1):  # Проходим по верхней строке справа налево
                r.append(layer) 
                c.append(j)  
                val.append(grid[layer][j])  
            total = len(val)  # Общее количество элементов в текущем слое
            kk = k % total  # Эффективное количество сдвигов с учётом периодичности
            for i in range(total):  # Расставляем элементы на новые позиции после сдвига
                idx = (i - kk + total) % total  # Вычисляем исходный индекс со сдвигом на kk позиций
                grid[r[i]][c[i]] = val[idx]  # Записываем значение в соответствующую позицию
        return grid  