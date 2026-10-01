class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, start=1):
            # Позиция в обратном алфавите: 'a' -> 26, 'z' -> 1
            reversed_pos = 26 - (ord(ch) - ord('a'))
            total += reversed_pos * i
        return total