class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        p = 0
        m = prices[0]
        for price in prices:
            if price < m:
                m = price
                continue
            p = max(price-m,p)
        return p
        