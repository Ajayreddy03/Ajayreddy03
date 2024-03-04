def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    min_price = prices[0]  # Initialize the minimum price to the first day's price
    max_profit = 0  # Initialize the maximum profit to 0
    
    for price in prices[1:]:
        # Update the minimum price seen so far
        min_price = min(min_price, price)
        
        # Calculate the profit if we sell the stock at the current price
        current_profit = price - min_price
        
        # Update the maximum profit if the current profit is greater
        max_profit = max(max_profit, current_profit)
    
    return max_profit

# Example usage:
if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    print("Max Profit (Example 1):", maxProfit(prices1))  # Output: 5
    
    prices2 = [7,6,4,3,1]
    print("Max Profit (Example 2):", maxProfit(prices2))  # Output: 0
