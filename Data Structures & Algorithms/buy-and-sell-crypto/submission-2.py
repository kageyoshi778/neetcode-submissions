class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]

        for sell in prices:
            profit= max(profit,sell-buy)
            buy= min(sell,buy)
        return profit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP'''