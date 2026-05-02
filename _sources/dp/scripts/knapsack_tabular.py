def derive_solution(memo, profits, weights, capacity):
    N = len(weights)
    # Vecteur de variables de décisions initialisées à None au début
    X = [None for _ in range(N)]
    
    c = capacity
    for k in range(N):
        if memo[k+1][c] + profits[k] == memo[k][c]:
            # l'objet k a été rajouté dans le sac puisque la valeur a augmenté
            # de profits[k] par rapport à la ligne précédente
            X[k] = 1
            c -= weights[k]
        else:
            X[k] = 0

    return X


def knapsack(profits, weights, capacity):
    N = len(profits)
    memo = [[None for _ in range(capacity + 1)] for _ in range(N + 1)]
    # initialisation du tableau de mémoïsation
    for c in range(capacity + 1):
        memo[N][c] = 0

     # on parcourt dans l'ordre décroissant de k
    for k in range(N - 1, -1, -1):
        # parcours dans l'ordre croissant de la capacité
        for c in range(capacity + 1):
            profit_without = memo[k+1][c]
            if weights[k] <= c:
                remaining = c - weights[k]
                profit_with = memo[k+1][remaining] + profits[k]
            else:
                profit_with = -1

            best_profit = max(profit_with, profit_without)
            memo[k][c] = best_profit

    return memo[0][capacity]

def knapsack_with_assignment(profits, weights, capacity):
    N = len(profits)
    memo = [[None for _ in range(capacity + 1)] for _ in range(N + 1)]
    # initialisation du tableau de mémoïsation
    for c in range(capacity + 1):
        memo[N][c] = 0

     # on parcourt dans l'ordre décroissant de k
    for k in range(N - 1, -1, -1):
        # parcours dans l'ordre croissant de la capacité
        for c in range(capacity + 1):
            profit_without = memo[k+1][c]
            if weights[k] <= c:
                remaining = c - weights[k]
                profit_with = memo[k+1][remaining] + profits[k]
            else:
                profit_with = -1

            best_profit = max(profit_with, profit_without)
            memo[k][c] = best_profit

    X = derive_solution(memo, profits, weights, capacity)

    return memo[0][capacity], X


value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50
)
print(f"Valeur optimale: {value_opt}")

value_opt, X = knapsack_with_assignment(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50
)
print(f"Valeur optimale: {value_opt}. Solution: {X}")

