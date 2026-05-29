class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        # Проходим по всем элементам массива
        while i < len(nums):
            start = nums[i]

            # Пока следующий элемент отличается на 1, расширяем диапазон
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            # Если диапазон состоит более чем из одного числа
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            # Если число одиночное
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans