# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # Пустое дерево считается симметричным

        def dfs(left, right):
            # Вспомогательная рекурсивная функция для сравнения двух поддеревьев
            
            if not left and not right:
                return True  # Оба узла пустые - симметрия соблюдена на этом уровне
            
            if not left or not right:
                return False  # Один узел существует, а другой нет - нарушение симметрии
            
            if left.val != right.val:
                return False  # Значения узлов различаются - нарушение симметрии
            
            # Рекурсивно сравниваем зеркальные пары:
            # левое поддерево левого узла с правым поддеревом правого узла (внешние ветви)
            # правое поддерево левого узла с левым поддеревом правого узла (внутренние ветви)
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        # Запускаем сравнение левого и правого поддеревьев корневого узла
        return dfs(root.left, root.right)