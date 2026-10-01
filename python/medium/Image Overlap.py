class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a1 = []
        b1 = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    a1.append((i, j))
                if img2[i][j] == 1:
                    b1.append((i, j))

        d = {}
        ans = 0

        for ax, ay in a1:
            for bx, by in b1:
                tr = (bx - ax, by - ay)
                d[tr] = d.get(tr, 0) + 1
                ans = max(ans, d[tr])
        return ans