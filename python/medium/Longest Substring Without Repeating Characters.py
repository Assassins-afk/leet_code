class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Хранит символы текущего окна
        l = 0            # Левый указатель (начало окна)
        res = 0          # Максимальная длина
        
        for r in range(len(s)):  # r - правый указатель (конец окна)
            # Если символ уже есть в окне - удаляем символы слева пока не уберем его
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Добавляем новый символ в окно
            charSet.add(s[r])
            
            # Обновляем максимум 
            res = max(res, r - l + 1)
            
        return res