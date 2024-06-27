class Solution :
    def best_time_to_buy_and_sell(self, prices:list) -> dict:
        l,r = 0,1
        maxP =  0
        selling = None

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit >= maxP:
                    maxP = profit
                    selling = r
            else : 
                    l = r    

            r+= 1    
            # modified here to get the Exact index that whre to buy and where to sell
        return {
                "profit" : maxP,
                "buying" : l,
                "selling" : selling
            }                


obj = Solution()

print(obj.best_time_to_buy_and_sell([7,1,5,3,6,4]))