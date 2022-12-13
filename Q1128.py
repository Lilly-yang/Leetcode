class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = 0
        while dominoes != []:
            t = dominoes.pop()
            while t in dominoes:
                count += 1
                dominoes.remove(t)
                
            t.reverse()
            while t in dominoes:
                count += 1
                dominoes.remove(t)
                
        return count

print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))