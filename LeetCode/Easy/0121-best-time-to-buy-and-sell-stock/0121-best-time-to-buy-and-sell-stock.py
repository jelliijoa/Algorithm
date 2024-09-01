class Solution(object):
    def maxProfit(self, prices):
        minPrice = float('inf')
        maxProfit = 0

        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice

        return maxProfit