class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        abj = defaultdict(list)  # Строим список смежности для неориентированного дерева
        for a, b in edges:
            abj[a].append(b)
            abj[b].append(a)

        mp = {}  # Храним уровень и родителя для каждого узла (предполагаем, что узлы нумеруются с 1)
        q = deque()
        q.append((1, 0, -1))  # Начинаем BFS от корня 1 с уровнем 0 и родителем -1

        while q:
            node, lvl, par = q.popleft()
            mp[node] = [lvl, par]  # Записываем уровень и родителя текущего узла
            for nei in abj[node]:
                if nei != par:  # Избегаем возврата к родителю
                    q.append((nei, lvl + 1, node))

        @cache  # Кэшируем результаты LCA для повторяющихся пар запросов
        def lca(a, b):
            while mp[a][0] > mp[b][0]: a = mp[a][1]  # Поднимаем более глубокий узел a до уровня b
            while mp[a][0] < mp[b][0]: b = mp[b][1]  # Поднимаем более глубокий узел b до уровня a
            while a != b:  # Поднимаем оба узла, пока не встретим общего предка
                a = mp[a][1]
                b = mp[b][1]
            return a

        res = []
        for a, b in queries:
            l = lca(a, b)  # Находим наименьшего общего предка для узлов a и b
            lvls = (mp[a][0] - mp[l][0]) + (mp[b][0] - mp[l][0])  # Вычисляем общее количество рёбер между a и b
            res.append(0 if lvls == 0 else pow(2, lvls - 1, 10**9 + 7))  # Если путь пустой - 0, иначе 2^(lvls-1) по модулю

        return res