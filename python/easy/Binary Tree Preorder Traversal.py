# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:  # Если дерево пустое, возвращаем пустой список
            return []

        stack = [root]  # Инициализируем стек корневым узлом
        result = []  

        while stack:  # Пока стек не пуст, продолжаем обход
            node = stack.pop()  # Извлекаем узел с вершины стека 
            result.append(node.val)  # Добавляем значение текущего узла в результат

            if node.right:  # Сначала добавляем правый узел в стек 
                stack.append(node.right)
            if node.left:  # Затем добавляем левый узел
                stack.append(node.left)
        return result  