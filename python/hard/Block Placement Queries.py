class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Инициализация: максимальная координата, отсортированный список препятствий с границами 0 и mx
        mx = 50000
        from sortedcontainers import SortedList
        st = SortedList([0, mx])
        for q in queries:
            if q[0] == 1:
                st.add(q[1])

        # Дерево Фенвика для хранения максимальных интервалов между препятствиями
        bt = [0] * (mx + 2)  

        # Обновление: установка значения v в позиции x 
        def update(x: int, v: int) -> None:
            x += 1  
            while x < len(bt):
                if v > bt[x]:
                    bt[x] = v
                x += x & -x
            
        # Запрос: получение максимального значения на префиксе
        def query(x: int) -> int:
            x += 1  
            res = 0
            while x > 0:
                if bt[x] > res:
                    res = bt[x]
                x -= x & -x
            return res

        # Построение начальных интервалов: проход по всем препятствиям и обновление дерева
        pre = 0
        for x in st:
            if x > 0:
                update(x, x - pre)
            pre = x

        ans = []

        # Обработка запросов в обратном порядке: удаление препятствий и проверка размещения блоков
        for q in reversed(queries):
            if q[0] == 1:
                # Удаление препятствия: пересчёт интервала для следующего препятствия
                x = q[1]
                st.remove(x)
                idx = st.bisect_left(x)  
                pre = st[idx - 1]
                nxt = st[idx]
                update(nxt, nxt - pre)
            else:
                # Проверка: можно ли разместить блок размера sz перед координатой x
                x, sz = q[1], q[2]
                idx = st.bisect_right(x) 
                pre = st[idx - 1]
                max_space = max(x - pre, query(pre))
                ans.append(max_space >= sz)
        return ans[::-1]