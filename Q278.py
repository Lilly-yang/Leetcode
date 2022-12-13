
def isBadVersion(b):
    if b >= 1:
        return True

    return False

class Solution:
    def firstBadVersion(self, n) :
        s_range = [1, n]
        result = 1
        while s_range[0] != s_range[1]:
            ind = int((sum(s_range)+1)/2)
            if isBadVersion(ind):
                result = ind
                s_range[-1] = ind - 1
            else:
                s_range[0] = ind
        
        if isBadVersion(s_range[0]):
            result = s_range[0]

        return result

sol = Solution()
print(sol.firstBadVersion(2))