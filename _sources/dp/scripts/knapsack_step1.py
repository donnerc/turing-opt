def knapsack(profits, weights, capacity):
    if len(profits) == 0:
        return 0

    profit_without = knapsack(profits[1:], weights[1:], capacity)
    remaining = capacity - weights[0]
    profit_with = knapsack(profits[1:], weights[1:], remaining) + profits[0]

    return max(profit_with, profit_without)


value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50
)
print(f"Valeur optimale: {value_opt}")
