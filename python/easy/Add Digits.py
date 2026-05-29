class Solution:
    def addDigits(self, num: int) -> int:
        def sum_digits(x):
            sm = 0
            while x > 0:
                sm += x % 10
                x //= 10
            return sm

        while num >= 10:
            num = sum_digits(num)
        return num