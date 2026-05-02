from _sources.db.scripts.dp import timeit
memo = {}   # dictionnaire global servant à stocker les valeurs déjà calculées
def fib(n):
    if n <= 1: 
        memo[n] = n
        return n

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
    
for n in [5, 10, 20, 200]:
    result, ms = timeit(fib, n)
    print(f"fib({n}) -> {result}, exécuté en {round(ms, 3)} ms")

