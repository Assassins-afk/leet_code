# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #если оба узла пустые,значит мы дошли до конца веток в обоих деревьях одновременно
        if not p and not q:
            return True
        
        #если один узел пустой, а другой нет, ИЛИ значения узлов различаются — деревья точно разные

        if not p or not q or p.val != q.val:
            return False
        
        # Рекурсивный случай: оба текущих узла существуют и имеют одинаковые значения.
        # Проверяем, что левые поддеревья одинаковые И правые поддеревья одинаковые.
        # Используем оператор AND, потому что деревья одинаковы только если
        # и левая, и правая части идентичны
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))