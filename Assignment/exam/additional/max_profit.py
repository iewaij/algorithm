def max_profit(k, prices):
    """Find the maximum profit given the price list of a given stock."""
    profit = 0
    diff_list = [p_1-p_0 for p_0, p_1 in zip(prices[:-1], prices[1:])]
    profit_list = [0]
    for d in diff_list:
        if d >= 0:
            profit_list[-1] += d
        elif d < 0 and profit_list[-1] != 0:
            profit_list.append(0)
    sorted_profit_list = sorted(profit_list, reverse=True)
    return sum(sorted_profit_list[:k])
