# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minimum, profit = prices[0], 0
        for x in prices:
            if x < minimum:
                minimum = x
            elif profit < x - minimum:
                profit = x - minimum
        return profit
