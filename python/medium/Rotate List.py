# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head 
        cur = head  # Указатель для прохода по списку
        N = 1  # Счётчик длины списка
        while cur.next:  # Идём до последнего узла
            N += 1
            cur = cur.next  # Переход к следующему
        cur.next = head  # Замыкаем список в кольцо

        M = N - (k % N)# Вычисляем, сколько шагов нужно сделать до нового хвоста
        
        i = 0  
        cur = head  
        while i < M:
            prev = cur  # Сохраняем предыдущий узел
            cur = cur.next  # Переход к следующему
            i += 1

        prev.next = None  # Разрываем кольцо
        head = cur  

        return head  