class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        
        nines = sum // 9
        remainder = sum % 9
        
        digits = []
        
        # Add all 9s
        for _ in range(nines):
            digits.append(9)

        if remainder > 0:
            digits.append(remainder)

        while len(digits) < num:
            digits.append(0)
        
        return ''.join(map(str, digits))