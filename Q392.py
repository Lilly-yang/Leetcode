class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s != "":
            for i in range(len(s)):
                try:
                    idx = t.index(s[i])
                except:
                    return False

                if idx == len(t)-1 and i==len(s)-1:
                    return True
                t = t[idx+1:]
            return True
        else:
            return True

if __name__ == "__main__":
    Sol = Solution()
    print(Sol.isSubsequence('abc', 'ahbgdc'))