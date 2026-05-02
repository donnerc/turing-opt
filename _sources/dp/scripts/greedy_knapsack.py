def greedy_knapsack(profits, weights, capacity):
    solution = [0] * len(weights)
    total_weight = 0
    total_profit = 0
    indices = range(len(weights))
    indices_sorted_by_value_to_weight_ratio = sorted(
        indices, key=lambda i: profits[i] / weights[i], reverse=True
    )
    k = 0
    while total_weight + weights[k] <= capacity:
        i = indices_sorted_by_value_to_weight_ratio[k]
        solution[i] = 1
        total_weight += weights[i]
        total_profit += profits[i]
        k += 1

    return total_profit, solution


N = [4500, 2600, 2600, 2600]
V = [24, 13, 13, 13]
C = 50
value, X = greedy_knapsack(profits=N, weights=V, capacity=C)
print(f"Solution optimale trouvée: X={X}, valeur={value}")
