class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = '123456789'
        nums = []
        for lenght in range(2, 10):
            for i in range(10 - lenght):
                num = int(sample[i:i + lenght])
                if low <= num <= high:
                    nums.append(num)
        return nums