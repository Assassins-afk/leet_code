class Solution:
    MOD = 1_000_000_007 

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        res = [[0] * m for _ in range(n)]  # Инициализация результирующей матрицы
        for i in range(n):  # Перебор строк A
            for k in range(len(a[0])):  # Перебор столбцов A / строк B
                r = a[i][k]
                if r == 0: continue
                for j in range(m):  # Перебор столбцов B
                    res[i][j] = (res[i][j] + r * b[k][j]) % self.MOD  # Умножение с накоплением по модулю
        return res

    def powMul(self, base, exp, res):
        while exp > 0:  # Бинарное возведение матрицы в степень
            if exp & 1:
                res = self.mul(res, base)  # Умножаем результат на base
            base = self.mul(base, base)  # Возводим base в квадрат
            exp >>= 1  # Сдвигаем степень вправо
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        if n == 1:  
            return r - l + 1  # Любое число из диапазона
            
        m = r - l + 1  
        if n == 2:  # Базовый случай: массив длины 2
            return (m * (m - 1)) % self.MOD  # Количество строго убывающих/возрастающих пар
        
        base = [[0] * (2 * m) for _ in range(2 * m)]  # Матрица переходов 2m x 2m

        for i in range(m):  # Заполнение матрицы переходов для состояний "подъём" (peak) и "спуск" (valley)
            for j in range(i):  # Переход из "подъёма" в "спуск" с меньшим значением
                base[i][m + j] = 1
            for j in range(i + 1, m):  # Переход из "спуска" в "подъём" с большим значением
                base[m + i][j] = 1
                
        res = [[0] * (2 * m)]  # Начальный вектор длиной 2m
        for i in range(m):  
            res[0][i] = i
            res[0][m + i] = m - 1 - i 

        res = self.powMul(base, n - 2, res)  # Возведение матрицы переходов в степень n-2 и умножение на начальный вектор
        
        return sum(res[0]) % self.MOD  # Сумма всех способов по модулю