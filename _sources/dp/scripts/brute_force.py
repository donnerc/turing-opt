from itertools import combinations, product

# Données de l'instance
N = [2600, 2600, 2600, 4500]
V = [13, 13, 13, 24]
C = 50

# Domaine de valeurs des variables de décision
domain = [0, 1]

# Volume de la solution X
def volume(X, V):
    return sum(X[i] * V[i] for i in range(len(X)))

# Valeur de la solution X
def f(X, N):
    return sum(X[i] * N[i] for i in range(len(X)))

# Force brute
all_guesses = product([0,1], repeat=4)
all_solutions = [(X, f(X, N), volume(X, V)) for X in all_guesses]

# Classement des solutions => meilleures solutions en haut
for no, solution in enumerate(sorted(all_solutions, key=lambda sol: sol[1], reverse=True)):
    X, value, volume = solution
    feasible = volume <= C
    print(f"Solution no {no}: X={X}, f(X)={value}, V(X)={volume}, Feasible={feasible}")