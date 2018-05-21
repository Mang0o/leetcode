"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit_sell_yesterday = 0 #如果持有到昨天的最大利润
        profit_sell_before = 0 #如果没有持有到昨天，因为可能前天卖出更高，虽然昨天今天也有利润，
                               #但是这个利润差不足以弥补前天到昨天的亏损，所以前天或之前卖出就好
        for i in range(len(prices)):
            tmp = profit_sell_yesterday
            profit_sell_yesterday = max(profit_sell_yesterday+(prices[i] - prices[i-1]),profit_sell_before)
            profit_sell_before = max(profit_sell_before,tmp)

        return max(profit_sell_yesterday,profit_sell_before)
