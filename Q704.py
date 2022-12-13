from decimal import MAX_EMAX


class Solution:
    def search(self, nums, target):
        s_range = [0, len(nums)-1]
        while s_range[0] != s_range[1]:
            ind = int((sum(s_range)+1)/2)
            if nums[ind] == target:
                return ind
            elif nums[ind] > target:
                s_range[-1] = ind -1
            else:
                s_range[0] = ind
        
        if nums[s_range[0]] == target:
            return s_range[0]

        return -1

sol = Solution()
print(sol.search([2,5], 2))