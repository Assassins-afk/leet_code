class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []  
        for num in nums:  # проходим по каждому числу в массиве
            str_num = str(num)  # преобразуем число в строку
            for char in str_num:  # проходим по каждому символу строки
                digit = int(char)  # преобразуем символ в целое число
                answer.append(digit)  
        return answer  