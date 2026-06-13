class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        @cache
        def sum_same_len(limit):
            # Преобразуем числовой лимит в список цифр для обработки поразрядно
            s = str(limit)
            arr = []
            for c in s: arr.append(int(c))

            n = len(arr)

            @cache
            # Рекурсивная DP-функция: i - текущая позиция, prev - предыдущая цифра, tight - флаг ограничения сверху, curr - текущее количество волн, trend - направление последнего изменения 
            def dp(i, prev, tight, curr, trend):
                if i == n: return curr
                # Определяем максимально допустимую цифру на текущей позиции с учетом флага tight
                mx = arr[i] if tight else 9
                res = 0

                # Перебираем все возможные цифры для текущей позиции
                for d in range(mx + 1):
                    if i == 0 and d == 0: continue

                    # Обновляем флаг tight: остается true только если были на границе и выбрали максимум
                    ntight = tight and d == mx

                    # Увеличиваем счетчик волн если произошла смена направления
                    ncurr = curr
                    if trend == 1 and d < prev: ncurr += 1
                    elif trend == 2 and d > prev: ncurr += 1

                    # Определяем новое направление тренда
                    if d == prev or i == 0: ntrend = 0
                    elif d > prev: ntrend = 1
                    elif d < prev: ntrend = 2

                    # Рекурсивно обрабатываем следующий разряд и суммируем результаты
                    res += dp(i + 1, d, ntight, ncurr, ntrend)
                
                return res
            # Запускаем DP с начальными параметрами:
            return dp(0, 0, True, 0, 0)
        
        @cache
        def sum_up_to(limit):
            # Определяем количество цифр в числе limit
            totald = len(str(limit))
            res = 0

            # Суммируем волны для всех чисел с меньшим количеством разрядов
            for digits in range(1, totald):
                largest = 10 ** digits - 1
                res += sum_same_len(largest)

            # Добавляем волны для чисел с таким же количеством разрядов до limit включительно
            res += sum_same_len(limit)
            return res

        # Вычисляем разность между количеством волн до num2 и до num1
        res = sum_up_to(num2) - sum_up_to(num1)

        # Корректируем результат: проверяем, является ли само число num1 волнистым, и если да - добавляем 1
        s = str(num1)
        for i in range(1, len(s) - 1):
            if s[i - 1] < s[i] > s[i + 1] or s[i - 1] > s[i] < s[i + 1]:
                res += 1
        return res