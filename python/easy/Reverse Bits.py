class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range(32):  # проходим по всем 32 битам
            bit = (n >> i) & 1  # извлекаем i-й бит из исходного числа
            res = res | (bit << (31 - i))  # помещаем бит в зеркальную позицию результата
        return res  