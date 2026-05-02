# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]  # пустой узел сбалансирован, высота 0

            left, right = dfs(root.left), dfs(root.right)  # Рекурсивно проверяем левое и правое поддеревья
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)  # Дерево сбалансировано, если оба поддерева сбалансированы и разница высот ≤ 1

            return [balanced, 1 + max(left[1], right[1])]  # Возвращаем [сбалансировано ли, высота текущего поддерева]
        
        return dfs(root)[0] 