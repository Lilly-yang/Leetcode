class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # print(len(s))
        c = 0
        for ind,j in enumerate(s):
            c_0, c_1 = 0, 0
            for i in s[ind:]:
                if i == '0':
                    c_0 += 1
                else:
                    c_1 += 1

                if c_0 == c_1:
                    c += 1
                    c_0, c_1 = 0, 0
                    break
                
        return c

sol = Solution()
print(sol.countBinarySubstrings('110001111000000'))