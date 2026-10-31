class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                top = stack.pop()
                score = 1 if top == 0 else 2 * top
                stack[-1] += score
        
        return stack[0]