class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])

        # Шаг 1: Применяем гравитацию — камни падают вправо
        for r in range(rows):
            i = cols - 1  # позиция, куда должен упасть следующий камень
            for c in reversed(range(cols)):
                if box[r][c] == '#':  # камень
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == '*':  # препятствие
                    i = c - 1  # сбрасываем позицию перед препятствием

        # Шаг 2: Поворот на 90 градусов по часовой стрелке
        res = []
        for c in range(cols):
            col = []
            for r in reversed(range(rows)):  # идём снизу вверх для поворота по часовой
                col.append(box[r][c])
            res.append(col)
        
        return res