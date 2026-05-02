from visualiser.visualiser import Visualiser as vs

config = {
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey",
}

# Valeurs nutritives
N = [2600, 2600, 2600, 500, 4500, 960]

# Volume des items
V = [13, 13, 13, 10, 24, 11]

# Capacité du sac à dos
C = 50

# Contrainte
def volume(X, V):
    return sum(X[i] * V[i] for i in range(len(X)))


def constraint_max_volume(X, V, C):
    return volume(X, V) <= C


# fonction objective
def f(X, N):
    return sum(X[i] * N[i] for i in range(len(X)))


# Solution faisable, mais non optimale, qui prend uniquement les trois paquets de pâtes
X1 = [1, 1, 1, 0, 0, 0]
print(f"Contrainte respectée? : {constraint_max_volume(X1, V, C)}")
print(f"Valeur nutritive emportée : {f(X1, N)}")

# Solution non faisable, qui prend tous les articles (il n'y a pas la place)
X_unfeasible = [1, 1, 1, 1, 1, 1]
print(f"Contrainte respectée? : {constraint_max_volume(X_unfeasible, V, C)}")
print(f"Valeur nutritive emportée : {f(X_unfeasible, N)}")




def knapsack(N, V, C):
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def solve_knapsack(C, k=None):
        k = k if k is not None else len(V) - 1
        if k == 0:
            value, X = (N[k], [1]) if V[k] <= C else (0, [0])
            return value, X
        else:
            value_without, X_without = solve_knapsack(C, k - 1)

            if C - V[k] >= 0:
                value_with, X_with = solve_knapsack(C - V[k], k - 1)
            else:
                value_with = -N[k]

            if value_without < value_with + N[k]:
                return (value_with + N[k], X_with + [1])
            else:
                return (value_without, X_without + [0])

    return solve_knapsack(C, k=len(V) - 1)


def knapsack1(N, V, C):
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def solve_rec(C, k=None):
        if k == 0:
            return N[k] if V[k] <= C else 0
        else:
            value_without = solve_rec(C, k - 1)

            if C - V[k] >= 0:
                value_with = solve_rec(C - V[k], k - 1)
            else:
                value_with = -N[k]

            if value_without < value_with + N[k]:
                return value_with + N[k]
            else:
                return value_without

    return solve_rec(C, k=len(V) - 1)


def knapsack_memoized(N, V, C):
    memo = {}
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def solve_rec(C, k):
        if (C, k) in memo:
            return memo[(C, k)]

        if k >= len(V):
            return 0

        value_without = solve_rec(C, k + 1)
        value_with = solve_rec(C - V[k], k + 1) + N[k] if C >= V[k] else 0

        value = max(value_without, value_with)
        memo[(C, k)] = value
        return value

    return solve_rec(C, k=0)


class Knapsack:
    def __init__(self, weights, values, capacity):
        if len(values) != len(weights):
            raise ValueError("weights and values should be of the same length")
        if len(values) == 0:
            raise ValueError("weight should contain at least one item")
        self.W = weights
        self.V = values
        self.size = len(values)
        self.C = capacity

    def solve(self):
        return self.solve_recursive(self.C, len(self.V))

    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def solve_recursive(self, C, k):
        if k == 0:
            value, X = (self.V[k], [1]) if self.V[k] <= C else (0, [0])
            return value, X
        else:
            value_without, X_without = self.solve_recursive(c, k - 1)

            if C - self.V[k] >= 0:
                value_with, X_with = self.solve_recursive(C - self.V[k], k - 1)
            else:
                value_with = -self.V[k]

            if value_without < value_with + self.V[k]:
                return (value_with + self.V[k], X_with + [1])
            else:
                return (value_without, X_without + [0])

# def kp_step1(profits: list[int], weights: list[int], capacity: int):
@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def knapsack__(profits, weights, capacity: int) -> int:
    if len(profits) == 0:
        return 0

    profit_without = knapsack(profits[1:], weights[1:], capacity)
    remaining = capacity - weights[0]
    profit_with = knapsack(profits[1:], weights[1:], remaining) + profits[0]

    return max(profit_with, profit_without)

@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def knapsack(profits, weights, capacity: int) -> int:
    if len(profits) == 0:
        return 0

    profit_without = knapsack(profits[1:], weights[1:], capacity)
    if weights[0] <= capacity:
        remaining = capacity - weights[0]
        profit_with = knapsack(profits[1:], weights[1:], remaining) + profits[0]
    else:
        profit_with = -1

    return max(profit_with, profit_without)

@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def knapsack(profits, weights, capacity, k):
    if k >= len(profits):
        return 0

    profit_without = knapsack(profits, weights, capacity, k + 1)
    if weights[k] <= capacity:
        remaining = capacity - weights[k]
        profit_with = knapsack(profits, weights, remaining, k + 1) + profits[k]
    else:
        profit_with = -1

    return max(profit_with, profit_without)

def knapsack(N, V, C):
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def kp(C, k):
        if k >= len(V):
            return 0

        value_without = kp(C, k + 1)
        value_with = kp(C - V[k], k + 1) + N[k] if C >= V[k] else 0

        return max(value_without, value_with)

    return kp(C, k=0)

def knapsack(profits, weights, capacity):
    N = len(profits)
    # Tableau de `capacity` colonnes et `N` lignes rempli de valeurs None
    # memo[k][c] contiendra la mémoïsation de solve(c, k)
    memo = [[None for _ in range(capacity + 1)] for _ in range(N + 1)]

    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def solve(capacity, k):
        if memo[k][capacity] is not None:
            return memo[k][capacity]

        if k >= len(profits):
            return 0

        profit_without = solve(capacity, k + 1)
        if weights[k] <= capacity:
            remaining = capacity - weights[k]
            profit_with = solve(remaining, k + 1) + profits[k]
        else:
            profit_with = -1

        best_value = max(profit_with, profit_without)
        memo[k][capacity] = best_value
        return best_value

    return solve(capacity=capacity, k=0)


N = [2600, 2600, 2600, 500, 4500]
V = [13, 13, 13, 10, 24]
C = 50

N = [2600, 2600, 2600, 4500]
V = [13, 13, 13, 24]
C = 50
value = knapsack(N, V, C)
print(f"valeur optimale: {value}")
# problem = Knapsack(V, N, C)
# value, X_optimal = problem.solve()

filename = "knapsack_memoized"
delay = 1
vs.make_animation(f"{filename}.gif", delay=delay)

# print(X_optimal)
# # Solution non faisable, qui prend tous les articles (il n'y a pas la place)
# print(
#     f"Contrainte respectée? (Volume total: {volume(X_optimal, V)}) : {constraint_max_volume(X_optimal, V, C)}"
# )
# print(f"Valeur nutritive emportée : {f(X_optimal, N)}")
