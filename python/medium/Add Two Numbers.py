import math  

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        # Продолжаем пока есть хотя бы один непросмотренный узел в l1 или l2
        # ИЛИ пока есть непогашенный перенос
        while l1 or l2 or carry:
            # Получаем значение текущего узла первого числа
            v1 = l1.val if l1 else 0
            
            # Получаем значение текущего узла второго числа
            v2 = l2.val if l2 else 0

            # Суммируем цифры текущего разряда + перенос с предыдущего разряда
            val = v1 + v2 + carry
            
            # Вычисляем новый перенос (целочисленное деление на 10)
            carry = val // 10
            
            # Оставляем только последнюю цифру результата для текущего разряда
            val = val % 10
            
            # Создаем новый узел с полученной цифрой и добавляем в результат
            cur.next = ListNode(val)

            # Перемещаем указатель cur на следующий узел
            cur = cur.next
            
            # Переходим к следующим узлам исходных списков 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next