"""
Best Time to Buy and Sell Stock — LeetCode #121
Category: Kadane's Algorithm
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on day i.
You want to maximize profit by choosing a single day to buy and a different day in the future to sell.
Return the maximum profit. If no profit possible, return 0.

Approach: Track min price seen so far + max profit
- Single pass: keep track of min price seen to the left
- At each day, calculate profit if sold today (price - min_price)
- Update max profit
- Time: O(n), Space: O(1)
"""


def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


# --- Tests ---
assert max_profit([7, 1, 5, 3, 6, 4]) == 5,    "Buy at 1, sell at 6"
assert max_profit([7, 6, 4, 3, 1]) == 0,        "Never profitable"
assert max_profit([2, 4, 1]) == 2,                "Buy at 2, sell at 4"
assert max_profit([3, 3, 3, 3]) == 0,            "No movement"
assert max_profit([1]) == 0,                      "Single day"
print("All tests passed!")
