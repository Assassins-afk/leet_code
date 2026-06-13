class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])  # Находим минимальное время завершения среди всех задач первой фазы

            finish2 = inf  
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])  # Для каждой задачи второй фазы: нельзя начать раньше finish1, добавляем длительность и берём минимум
            return finish2 

        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)  # 1 Вариант: сначала наземные работы, потом водные
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)  # 2 Вариант: сначала водные работы, потом наземные
        return min(land_water, water_land)class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])  # Находим минимальное время завершения среди всех задач первой фазы

            finish2 = inf  
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])  # Для каждой задачи второй фазы: нельзя начать раньше finish1, добавляем длительность и берём минимум
            return finish2 

        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)  # 1 Вариант: сначала наземные работы, потом водные
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)  # 2 Вариант: сначала водные работы, потом наземные
        return min(land_water, water_land)