# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []    # Список для хранения результата обхода
        stack = []  # Стек для имитации рекурсии (хранения узлов)

        # Продолжаем, пока есть узлы для обработки 
        # или узлы в стеке, к которым нужно вернуться
        while root or stack:
            # Спускаемся максимально влево, сохраняя все пройденные узлы в стек
            while root:
                stack.append(root)   # Сохраняем текущий узел в стек
                root = root.left     # Переходим к левому потомку
            
            # Когда дошли до крайнего левого узла (root стал None),
            # извлекаем последний сохранённый узел из стека
            root = stack.pop()
            
            # Добавляем значение узла в результат 
            res.append(root.val)
            # Переходим к правому поддереву текущего узла
            root = root.right
            
        return res  # Возвращаем список значений