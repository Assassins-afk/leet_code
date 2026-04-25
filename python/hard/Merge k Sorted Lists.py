# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Объединяет k отсортированных связных списков в один отсортированный список.
        
        Args:
            lists: Массив из k связных списков (каждый список отсортирован по возрастанию)
            
        Returns:
            Один объединенный отсортированный связный список
        """
        # Если массив списков пуст, возвращаем None
        if not lists:
            return None

        # Итеративно объединяем списки парами, пока не останется один список
        while len(lists) > 1:
            # Временный массив для хранения результатов попарного слияния
            merged_lists = []
            lists_len = len(lists)
            
            # Проходим по спискам с шагом 2 (берем пары для слияния)
            for idx in range(0, lists_len, 2):
                # Берем первый список из пары
                l1 = lists[idx]
                
                # Вычисляем индекс второго списка в паре
                next_id = idx + 1
                
                # Берем второй список, если он существует, иначе None
                l2 = lists[next_id] if next_id < lists_len else None
                
                # Сливаем два списка в один отсортированный
                new_list = self.merge_two_sorted_lists(l1, l2)
                
                # Добавляем результат в массив объединенных списков
                merged_lists.append(new_list)
            
            # Заменяем исходный массив на массив объединенных списков
            # Количество списков уменьшается примерно в 2 раза
            lists = merged_lists

        # Когда остался один список, возвращаем его
        return lists[0]
    
    def merge_two_sorted_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Сливает два отсортированных связных списка в один отсортированный список.
        
        Args:
            list1: Первый отсортированный связный список
            list2: Второй отсортированный связный список
            
        Returns:
            Объединенный отсортированный связный список
        """
        # Создаем фиктивный узел для упрощения логики слияния
        dummy = ListNode()
        
        # Указатель на текущий последний узел в результирующем списке
        tail = dummy
        
        # Пока оба списка не пусты
        while list1 and list2:
            # Сравниваем значения текущих узлов
            if list1.val < list2.val:
                # Добавляем узел из первого списка
                tail.next = list1
                # Двигаем указатель первого списка вперед
                list1 = list1.next
            else:
                # Добавляем узел из второго списка
                tail.next = list2
                # Двигаем указатель второго списка вперед
                list2 = list2.next
            
            # Двигаем указатель результирующего списка вперед
            tail = tail.next
        
        # Добавляем оставшиеся узлы из непустого списка (если есть)
        # list1 or list2 вернет тот список, который не None
        tail.next = list1 or list2
        
        # Возвращаем результат, пропуская фиктивный первый узел
        return dummy.next