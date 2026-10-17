class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for value in prices:
            if value < min_price:
                min_price = value

            profit = value - min_price

            if profit > max_profit:
                max_profit = profit
            
        return max_profit