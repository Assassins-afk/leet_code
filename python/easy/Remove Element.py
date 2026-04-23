class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # указатель для элементов,не равных val
        
         # Проходим по всем элементам массива с помощью индекса i
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k