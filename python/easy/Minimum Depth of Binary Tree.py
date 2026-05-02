# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        leftDepth = self.minDepth(root.left)  # Рекурсивно вычисляем глубину левого поддерева
        rightDepth = self.minDepth(root.right)  # Рекурсивно вычисляем глубину правого поддерева

        if leftDepth == 0 or rightDepth == 0:  # Если одно из поддеревьев отсутствует 
            return max(leftDepth,rightDepth) + 1  # Берем глубину существующего поддерева + текущий узел
        else:  
            return min(leftDepth,rightDepth) + 1  # Берем минимальную глубину + текущий узел