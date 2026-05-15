# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # Медленный указатель 
        fast = head  # Быстрый указатель 

        while fast and fast.next != None:  # Проверяем, что быстрый указатель и следующий за ним узел существуют
            slow = slow.next  # Медленный указатель двигается на 1 шаг
            fast = fast.next.next  # Быстрый указатель двигается на 2 шага
            if slow == fast:  # Если указатели встретились, значит цикл существует
                return True 
            
        return False  