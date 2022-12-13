class Solution:
    def maxProfit(self, prices):
        # left = 0 #Buy
        # right = 1 #Sell
        # max_profit = 0
        # while right < len(prices):
        #     currentProfit = prices[right] - prices[left] #our current Profit
        #     if prices[left] < prices[right]:
        #         max_profit =max(currentProfit,max_profit)
        #     else:
        #         left = right
        #     right += 1
        # return max_profit
    
        length = len(prices)
        maximum = 0
        i = 0
        while i < length - 1:
            counter = 0
            for j in range(i + 1, length):
                if prices[j] < prices[i]:
                    i = j
                    break

                else:
                    counter += 1
                    local_max = prices[j] - prices[i]
                    if local_max > maximum:
                        maximum = local_max
            else:
                i += counter

        return maximum

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))