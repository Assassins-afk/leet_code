class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Итерируемся в обратном порядке
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] +=1
                return digits

            # Если была 9, она становится 0
            digits[i] = 0

         # Краевой случай: Все цифры были 9   
        return [1] + digits