# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head  # Текущий указатель, идём от головы списка
        
        while cur and cur.next:  # Пока есть текущий и следующий узел
            if cur.val == cur.next.val:  # Нашли дубликат
                cur.next = cur.next.next  # Пропускаем следующий узел (удаляем его)
            else:
                cur = cur.next  # Переходим к следующему уникальному узлу
                
        return head  # Возвращаем голову очищенного списка