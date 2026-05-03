class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = { 
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        if not digits: return []  # Если входная строка пустая, возвращаем пустой список
        output = ['']  # Инициализируем список с одной пустой строкой для начала комбинаций

        for d in digits:  # Проходим по каждой цифре во входной строке
            tmp = []  # Временный список для хранения новых комбинаций
            for v in nums[d]:  # Для каждой буквы, соответствующей текущей цифре
                for o in output:  # Для каждой существующей комбинации в output
                    tmp.append(o+v)  # Добавляем новую комбинацию: старая комбинация + текущая буква
            output = tmp  # Обновляем output новыми комбинациями
        return output