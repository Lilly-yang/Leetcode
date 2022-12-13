class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        print(str(int(s.count(letter)/len(s)*100)))

print(Solution().percentageLetter('fooler', 'o'))