class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q, farthest = deque([0]), 0  

        while q:
            i = q.popleft()  # Извлекаем текущий индекс для обработки
            start = max(i + minJump, farthest + 1)  # Начало диапазона прыжка
            for j in range(start, min(i + maxJump + 1, len(s))):  # Перебираем все возможные позиции для прыжка
                if s[j] == "0":  # Если позиция доступна 
                    q.append(j)
                    if j == len(s) - 1:  # Если достигли последнего индекса
                        return True 
            farthest = i + maxJump  # Обновляем максимальную границу, до которой уже проверили переходы
        return False 