class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Создаём словарь для быстрого поиска значений по ключу
        knowledge_dict = {k: v for k, v in knowledge}
        
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Находим закрывающую скобку
                j = s.index(')', i)
                key = s[i + 1:j]
                # Заменяем на значение или '?'
                result.append(knowledge_dict.get(key, '?'))
                i = j + 1
            else:
                # Обычный символ — добавляем как есть
                result.append(s[i])
                i += 1
        
        return ''.join(result)