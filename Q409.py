class Solution:
    def longestPalindrome(self, s: str) -> int:
        len_p = 1
        i = 0
        while len(s) > 1 and i < len(s) -1:
            l = s[i]
            if l in s[i+1:]:
                s = s.replace(l, "", 2)
                len_p += 2
            else:
                i += 1
        
        if not len(s):
            len_p -= 1
        
        return len_p

sol = Solution()
print(sol.longestPalindrome('abccccdd'))
