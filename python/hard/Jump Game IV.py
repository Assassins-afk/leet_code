class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}  # Словарь для хранения всех индексов одинаковых значений
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)  # Добавляем индекс в список для этого значения
            else:
                graph[arr[i]] = [i]  # Создаем новый список с первым индексом
        
        curs = [0] 
        visited = {0}  
        step = 0  
        
        while curs:
            nex = [] 
            for node in curs:
                if node == n - 1:
                    return step 
                
                # Прыжки на все индексы с таким же значением
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child) 
                
                # Очищаем список индексов для текущего значения, чтобы не обрабатывать их повторно
                graph[arr[node]].clear()
                
                # Прыжки на соседние индексы (влево и вправо)
                for child in [node - 1, node + 1]: 
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)
            
            curs = nex  
            step += 1  
        
        return -1  