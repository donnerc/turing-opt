def knapsack(profits, weights, cap, k):
    if k >= len(profits):
        return 0
    profit_without = knapsack(profits, weights, cap, k + 1)
    if weights[k] <= cap:
        rem = cap - weights[k]
        profit_with = knapsack(profits, weights, rem, k + 1) + profits[k]
    else:
        profit_with = -1
    return max(profit_with, profit_without)

value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], cap=50, k=0
)
print(f"Valeur optimale: {value_opt}")
