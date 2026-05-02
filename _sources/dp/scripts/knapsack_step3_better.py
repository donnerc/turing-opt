def knapsack(profits, weights, capacity):
    def solve(capacity, k):
        if k >= len(profits):
            return 0

        profit_without = solve(capacity, k + 1)
        if weights[k] <= capacity:
            remaining = capacity - weights[k]
            profit_with = solve(remaining, k + 1) + profits[k]
        else:
            profit_with = -1

        return max(profit_with, profit_without)

    return solve(capacity=capacity, k=0)

value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50
)
print(f"Valeur optimale: {value_opt}")
