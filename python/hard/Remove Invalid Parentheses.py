class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        visited = {s}
        queue = deque([s])
        result = []
        found = False

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                if is_valid(cur):
                    result.append(cur)
                    found = True

                if found:
                    continue

                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue
                    if i > 0 and cur[i] == cur[i - 1]:
                        continue
                    nxt = cur[:i] + cur[i + 1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

            if found:
                break

        return result