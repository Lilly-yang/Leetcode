class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        sum_l = []
        for i in range(k-1, len(nums)):
            sum_l.append(nums[i]-nums[i-k+1])
            
        return min(sum_l)

print(Solution().minimumDifference([9,4,1,7], 2))