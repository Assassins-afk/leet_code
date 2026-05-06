# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode, k: int) -> ListNode:
        new_head = None
        prev = head

        while k:
            next_node = prev.next
            prev.next = new_head
            new_head = prev
            prev = next_node
            k -= 1

        return new_head 

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        ktail = None
        new_head = None

        while cur:
            count = 0
            temp = cur  

            
            while count < k and temp:
                temp = temp.next
                count += 1

            if count == k:
                rev_head = self.reverse(cur, k)

                if not new_head:
                    new_head = rev_head

                if ktail:
                    ktail.next = rev_head  # Соединяем предыдущую группу с перевернутой
                
                ktail = cur  # Сохраняем текущий узел как хвост группы
                cur = temp  # Переходим к следующей группе
            else:
                break

        # Присоединяем оставшиеся узлы (меньше k) к последней перевернутой группе
        if ktail:
            ktail.next = cur

        return new_head if new_head else head