class Solution:
    def canThreePartsEqualSum(self, arr):
        if not sum(arr) % 3:
            target = sum(arr) // 3
            temp_sum = 0
            count = 0
            for i in range(len(arr)):
                temp_sum += arr[i]
                if temp_sum == target:
                    count += 1
                    if count == 3:
                        return True
        else:
            return False

sol = Solution()
print(sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))