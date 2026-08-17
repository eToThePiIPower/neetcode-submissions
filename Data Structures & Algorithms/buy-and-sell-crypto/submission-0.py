class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float("inf")
        for price in prices:
            if (price - minPrice) > maxProfit:
                maxProfit = (price - minPrice)
            if price < minPrice:
                minPrice = price
        return maxProfit