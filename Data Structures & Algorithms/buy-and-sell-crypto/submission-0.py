class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy at a lower price
        #sell at a higher price on a future day
        #maximise selling price - buying price
        #if no profit is possible return 0
        min_price =prices[0]
        max_profit=0
        for curr_price in prices:
            profit=curr_price-min_price
            if profit>max_profit:
                max_profit=profit
            if curr_price<min_price:
                min_price=curr_price
        
        return max(max_profit,0)
