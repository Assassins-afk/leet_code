# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  
            return None

        # переворачиваем поддеревья
        tmp = root.left  # сохраняем левого потомка во временную переменную
        root.left = root.right  # меняем местами: левый потомок становится правым
        root.right = tmp  # правый потомок становится левым

        # рекурсивно инвертируем поддеревья
        self.invertTree(root.left)  # инвертируем левое поддерево
        self.invertTree(root.right)  # инвертируем правое поддерево 
        return root  