class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = n // 2

        total_freq = [0] * 26
        for ch in s:
            total_freq[ord(ch) - ord('a')] += 1
        freq = [f // 2 for f in total_freq]
        
        def count_permutations_capped(limit=k+1):

            total = sum(freq)

            res = 1
            rem = total
            for f in freq:
                if f == 0:
                    continue

                c = 1
                for i in range(1, f + 1):
                    c = c * (rem - f + i) // i
                    if c > limit:
                        return limit 
                res *= c
                if res > limit:
                    return limit 
                rem -= f
            return res
        
        if count_permutations_capped() < k:
            return ""
        
        left = []
        remaining = sum(freq)
        
        for _ in range(half):
            for ci in range(26):
                if freq[ci] == 0:
                    continue
                
                freq[ci] -= 1
                
                perms = count_permutations_capped()
                
                if perms >= k:
                    left.append(chr(ci + ord('a')))
                    remaining -= 1
                    break
                else:
                    k -= perms
                    freq[ci] += 1
        
        h1 = ''.join(left)
        mid = s[n//2] if n % 2 == 1 else ''
        return h1 + mid + h1[::-1]