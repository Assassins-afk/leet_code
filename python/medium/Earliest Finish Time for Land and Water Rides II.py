class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime),len(waterStartTime)  
        res = inf  # Инициализируем результат бесконечностью для поиска минимума

        def check(s1, d1, s2, d2): 
            f1 = inf  # Минимальное время
            for i in range(len(s1)):  # Перебираем все доступные единицы первого транспорта
                f1 = min(f1, s1[i] + d1[i])  

            f2 = inf  
            for i in range(len(s2)):  # Перебираем все доступные единицы второго транспорта
                f2 = min(f2, max(f1, s2[i]) + d2[i])  # Стартуем не раньше, чем освободится первый транспорт и будет доступен второй
            return f2  
        
        # Возвращаем минимальное время из двух возможных сценариев порядка использования транспорта
        return min(
            check(landStartTime, landDuration, waterStartTime, waterDuration), 
            check(waterStartTime, waterDuration, landStartTime, landDuration)  
        )