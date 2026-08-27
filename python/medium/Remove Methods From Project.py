class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        abj = defaultdict(list)
        indegree = [0] * n
        for a, b in invocations:
            abj[a].append(b)
            indegree[b] += 1

        susp = set()
        def dfs(node):
            susp.add(node)
            for nei in abj[node]:
                indegree[nei] -= 1
                if not nei in susp: dfs(nei)
        dfs(k)

        for node in susp:
            if indegree[node]: return list(range(n))

        return [node for node in range(n) if not node in susp]