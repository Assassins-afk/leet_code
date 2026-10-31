class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Отрицательные числа не могут быть квадратами
        if num < 0:
            return False
        
        left, right = 0, num
        
        while left <= right:
            mid = (left + right) // 2  
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
