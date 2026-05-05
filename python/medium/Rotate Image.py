class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)  # Транспонируем матрицу (строки становятся столбцами)
        self.reflect(matrix)    # Отражем матрицу по вертикали для поворота на 90° по часовой стрелке

    def transpose(self, matrix):
        n = len(matrix)  # Получаем размер матрицы n x n
        for i in range(n):  # Проходим по всем строкам
            for j in range(i + 1, n):  # Меняем элементы выше главной диагонали с элементами ниже
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]  # Обмен элементов симметрично относительно главной диагонали

    def reflect(self, matrix):
        n = len(matrix)  # Получаем размер матрицы n x n
        for i in range(n):  # Проходим по всем строкам
            for j in range(n // 2):  # Проходим только до середины строки
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]  # Меняем левый и правый элементы местами