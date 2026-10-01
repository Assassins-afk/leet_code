class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        f = [0] * 26
        for c in s: 
            f[ord(c) - ord('a')] += 1

        oddc = ''
        for i, freq in enumerate(f):
            if freq % 2 == 1:
                if oddc == '': 
                    oddc = chr(i + ord('a'))
                else: 
                    return ''
            f[i] //= 2

        half = []
        
        def backtrack(pos):
            if pos == n // 2:
                result = ''.join(half)
                pal = result + oddc + result[::-1]
                return pal if pal > target else None
            
            for ci in range(26):
                if f[ci] == 0:
                    continue
                    
                c = chr(ci + ord('a'))
                
                if c < target[pos]:
                    continue
                
                f[ci] -= 1
                half.append(c)
                
                if c > target[pos]:
                    result = ''.join(half)
                    for j in range(26):
                        if f[j] > 0:
                            result += chr(j + ord('a')) * f[j]
                    pal = result + oddc + result[::-1]
                    f[ci] += 1
                    half.pop()
                    return pal
                
                result = backtrack(pos + 1)
                if result is not None:
                    f[ci] += 1
                    half.pop()
                    return result
                
                f[ci] += 1
                half.pop()
            
            return None
        
        result = backtrack(0)
        return result if result is not None else ''