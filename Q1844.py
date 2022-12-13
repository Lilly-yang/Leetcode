class Solution:
    def shift(self, st, fi):
        if ord(st) + fi > 26:
            return 'z'
        else:
            return chr(ord(st) + fi)
    
    def replaceDigits(self, s: str) -> str:
        if len(s) >1:
            for i in range(1, len(s), 2):
                print(s[i-1], int(s[i]))
                print()
                s[i] = self.shift(s[i-1], int(s[i]))
        
        return s

print(Solution().replaceDigits("a1c1e1"))