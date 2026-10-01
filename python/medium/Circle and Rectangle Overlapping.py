class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Находим ближайшую точку прямоугольника к центру круга
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Вычисляем квадрат расстояния от центра круга до ближайшей точки
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        dist_sq = dx * dx + dy * dy
        
        # Если расстояние не больше радиуса — фигуры пересекаются
        return dist_sq <= radius * radius