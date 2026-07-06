class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0
        for c in s:
            if c.islower(): l += 1
            elif c == '*' and l: l -= 1
            elif c == '#': l *= 2
            elif c == '%': pass
        if k >= l: return '.'

        for c in reversed(s):
            if c.islower():
                if k == l - 1: return c
                l -= 1
            elif c == '*': l += 1
            elif c == '#':
                l //= 2
                if k >= l: k -= l
            elif c == '%': k = l - 1 - k