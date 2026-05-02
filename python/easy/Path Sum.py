# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):  # Внутренняя рекурсивная функция DFS, принимает узел и текущую сумму пути
            if not node:  # Если узел None — пути нет, возвращаем False
                return False
            
            curSum += node.val  # Добавляем значение текущего узла к накопленной сумме
            if not node.left and not node.right:  # Если это листовой узел 
                return curSum == targetSum  # Проверяем, равна ли сумма пути целевому значению
            
            return (dfs(node.left, curSum) or dfs(node.right, curSum))  # Рекурсивно ищем путь в левом ИЛИ правом поддереве
        return dfs(root, 0)  # Запускаем DFS с корневого узла и начальной суммой 0