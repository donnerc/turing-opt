from _sources.db.scripts.dp import ArrayLRUCache

def fib_hash(n: int) -> int:
    memo = {}
    for k in range(n+1):
        if k <= 2: f = k
        else: f = memo[k-1] + memo[k-2]
        memo[k] = f
    return memo[n]

def fib_table(n: int) -> int:
    memo = [0] * (n + 1)
    for k in range(n + 1):
        if k <= 2: f = k
        else: f = memo[k - 1] + memo[k - 2]
        memo[k] = f
    return memo[n]

        

def fib_table_lru(n: int) -> int:
    memo = ArrayLRUCache(maxsize=3)
    for k in range(n + 1):
        if k <= 2: f = k
        else: f = memo[k - 1] + memo[k - 2]
        memo[k] = f
    return memo[n]


def fib_table_lru(n: int) -> int:
    memo = ArrayLRUCache(maxsize=3)
    # initialisation du tableau avec les cas de base
    for k in [0, 1]: memo[k] = k

    # remplir le tableau itérativement (dans le bon ordre) 
    # au lieu de faire des appels récursifs
    for k in range(2, n + 1):
        # remplacer les appels récursifs par des accès au tableau
        result = memo[k - 1] + memo[k - 2]
        memo[k] = result
    # La réponse au problème se trouve dans la dernière case
    # remplie du tableau
    return memo[n]

def test(f):
    for n in list(range(10)) + [50, 200, 1000]:
        print(f"F({n}) = {f(n)}")

test(fib_hash)
test(fib_table)
test(fib_table_lru)