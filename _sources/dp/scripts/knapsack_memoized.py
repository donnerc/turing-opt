def knapsack(profits, weights, capacity):
    N = len(profits)
    memo = [[None for _ in range(capacity + 1)] for _ in range(N + 1)]

    def solve(capacity, k):
        if memo[k][capacity] is not None:
            return memo[k][capacity]
        if k >= N:
            return 0

        profit_without = solve(capacity, k + 1)
        if weights[k] <= capacity:
            remaining = capacity - weights[k]
            profit_with = solve(remaining, k + 1) + profits[k]
        else:
            profit_with = -1

        best_profit = max(profit_with, profit_without)
        memo[k][capacity] = best_profit
        return best_profit

    return solve(capacity=capacity, k=0)


value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50
)
print(f"Valeur optimale: {value_opt}")
