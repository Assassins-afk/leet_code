# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]  # Инициализируем стек корневым узлом
        visit = [False]  # Параллельный стек для отслеживания состояния посещения узла
        res = [] 

        while stack:  # Продолжаем, пока в стеке есть узлы
            cur, v = stack.pop(), visit.pop()  # Извлекаем текущий узел и флаг его посещения
            if cur:  # Если узел существует 
                if v:  # Если узел уже был посещён ранее
                    res.append(cur.val)
                else:  # Иначе — первый раз видим узел, кладём в стек в обратном порядке
                    stack.append(cur)  # Сам узел снова в стек
                    visit.append(True)
                    stack.append(cur.right)  
                    visit.append(False)
                    stack.append(cur.left)  
                    visit.append(False)
        return res  