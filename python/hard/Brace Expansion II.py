class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        self.s = expression
        
        def parse() -> set[str]:
            result = set()      # объединение всех слагаемых (union)
            current = {""}      # текущее слагаемое (конкатенация), стартуем с пустой строки
            
            while self.i < len(self.s):
                c = self.s[self.i]
                
                if c == '{':
                    self.i += 1                 # пропускаем '{'
                    group = parse()             # рекурсивно разбираем содержимое
                    self.i += 1                 # пропускаем '}'
                    # декартово произведение: конкатенация
                    current = {a + b for a in current for b in group}
                    
                elif c == ',':
                    result |= current           # завершаем слагаемое
                    current = {""}              # начинаем новое
                    self.i += 1
                    
                elif c == '}':
                    break                       # конец группы, возвращаемся наверх
                    
                else:                           # буква
                    current = {a + c for a in current}
                    self.i += 1
            
            result |= current                   
            return result
        
        return sorted(parse())