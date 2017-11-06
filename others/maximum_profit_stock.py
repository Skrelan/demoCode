'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

def maximum_profit_stock(prices):
	if len(prices) < 2:
            return 0

	minimum_cost = prices[0]
	maximum_profit = 0

	for i in range(1,len(prices)):
		minimum_cost = min(minimum_cost,prices[i])
		maximum_profit = max(maximum_profit,prices[i]-minimum_cost)

	return maximum_profit

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

def  maximum_profit_stock_2(prices):
	if len(prices) < 2:
            return 0
        
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            print 'buy', i-1, 'sell', i
            profit += prices[i] - prices[i-1]
    
    return profit

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

def maximum_profit_stock_3(prices):
	if len(prices) < 2:
        return 0

    T = [[0]*len(prices) for i in range(0,2+1)]
        
        # T[i][j] max profit untill day j with i transactions
        
        # We get the formula
        # T[i][j] = max(T[i][j-1],(prices[j]-prices[m])+T[i-1][m]) {for m in (0,j-1)}
        # this O(N*k*k) time complexity, where N is the number of days
        
        #Let's optimize
        # T[i][j] = max(T[i][j-1],max_profit) where max_profit = max(T[i-1][m] - prices[m]) {for m in (0,j-1)}
        print T
        for i in range(1,3):
            max_profit = T[i-1][0] - prices[0]
            for j in range(1,len(prices)):
                max_profit = max(max_profit, T[i-1][j-1] - prices[j-1])
                T[i][j] = max(T[i][j-1], prices[j] + max_profit)
        print T        
        return T[2][len(prices)-1]

 '''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
 '''

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # because the first event is always a buy
    if not prices:
        return 0
    
    b0 = -prices[0]
    b1 = b0
    s0,s1,s2=0,0,0
    for i in range(1,len(prices)):
        b0 = max(b1,s2-prices[i])
        s0 = max(s1,b1+prices[i])
        b1 = b0
        s2 = s1
        s1 = s0
    return s0

