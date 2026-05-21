class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
           res += n % 2 # узнаем 1 или 0
           n = n >> 1 # сдвигаем на 1 бит в право
        return res