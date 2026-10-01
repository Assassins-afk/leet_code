class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        intervals = []
        
        for c in range(26):
            if first[c] == -1:
                continue
            start = first[c]
            end = last[c]
            i = start
            valid = True
            while i <= end:
                idx = ord(s[i]) - ord('a')
                if first[idx] < start:
                    valid = False
                    break
                end = max(end, last[idx])
                i += 1
            if valid:
                intervals.append((start, end))
        
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end+1])
                prev_end = end
        
        return res