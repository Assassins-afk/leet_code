class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Сортируем задачи по разнице actual - minimum 
        tasks.sort(key = lambda x: x[0] - x[1])
        res = cur = 0

        for actucal, minn in tasks:
            # Если текущей энергии недостаточно для минимального порога задачи, добавляем разницу в ответ и пополняем энергию
            if minn > cur:
                res += (minn - cur)
                cur = minn
            # Тратим энергию на выполнение задачи
            cur -= actucal

        return res