"""You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        for i in range(1,amount+1):
            dp[i] = min([dp[i-coin] if i-coin>=0 else MAX for coin in coins])+1
        return [dp[amount], -1][dp[amount] == MAX]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5],11))