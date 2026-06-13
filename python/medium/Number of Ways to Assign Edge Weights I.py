class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        abj = defaultdict(list)
        for a, b in edges:
            abj[a].append(b)
            abj[b].append(a)

        q = deque([(1, 0, -1)])
        mxlvl = 0
        while q:
            node, lvl, par = q.popleft()
            mxlvl = max(mxlvl, lvl)
            for nei in abj[node]:
                if nei != par: q.append((nei, lvl + 1, node))


        return pow(2, mxlvl - 1, MOD)