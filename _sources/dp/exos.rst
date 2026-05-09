.. _dp-exos:

Exercices
#########

..  contents:: Exercices
    :depth: 2

Exercice 1
==========

..  activecode:: dp-exo-01
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    Résolvez par programmation dynamique le problème suivant : étant donné une
    liste de n entiers positifs, déterminez la somme maximale de ces entiers
    sans jamais prendre deux éléments consécutifs.

    ..  admonition:: Exemples

        ::

            # en prenant 3 et 10
            >>> max_non_consecutive_sum([3, 2, 7, 10])
            13
            
            # en prenant 3, 5 et 7
            >>> max_non_consecutive_sum([3, 2, 5, 10, 7])
            15
            
            # en prenant 5, 100 et 5
            >>> max_non_consecutive_sum([5, 5, 10, 100, 10, 5])
            110

    ~~~~

..  reveal:: dp-exo-01-solution
    :showtitle: Solution
    :hidetitle: Cacher la solution
    :instructoronly:

    On commence par une solution récursive naïve, puis on introduit la
    mémoïsation pour éviter les calculs redondants, et enfin on peut passer à
    une solution itérative en utilisant une table de programmation dynamique.

    ..  admonition:: Solution récursive naïve

        La solution récursive naïve consiste à définir une fonction qui prend en
        entrée la liste d'entiers et l'indice courant, et qui retourne la somme
        maximale en considérant les éléments jusqu'à cet indice.

        Voici une implémentation possible en Python :

        ..  code-block:: python

            def max_sum(nums, index):
                if index < 0:
                    return 0
                elif index == 0:
                    return nums[0]

                # On a deux choix : prendre l'élément courant ou ne pas le prendre
                take = nums[index] + max_sum(nums, index - 2)
                skip = max_sum(nums, index - 1)

                return max(take, skip)


    Voici une solution possible en Python :

    ..  code-block:: python

        def max_non_consecutive_sum(nums):
            if not nums:
                return 0
            elif len(nums) == 1:
                return nums[0]

            # dp[i] représente la somme maximale en considérant les éléments jusqu'à l'indice i
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

            return dp[-1]


    ..  activecode:: max-non-consecutive-sum-solution-01
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        Première approche : solution récursive naïve

        ~~~~

        def max_non_consecutive_sum(numbers: list[float]) -> float:
            '''
            # en prenant 3 et 10
            >>> max_non_consecutive_sum([3, 2, 7, 10])
            13
            
            # en prenant 3, 5 et 7
            >>> max_non_consecutive_sum([3, 2, 5, 10, 7])
            15
            
            # en prenant 5, 100 et 5
            >>> max_non_consecutive_sum([5, 5, 10, 100, 10, 5])
            110
            '''
            if len(numbers) == 0:
                return 0
            elif len(numbers) == 1:
                return numbers[0]

            sum1 = numbers[0] + max_non_consecutive_sum(numbers[2:])
            sum2 = max_non_consecutive_sum(numbers[1:])
            return max(sum1, sum2)

        import doctest
        doctest.testmod()

    ..  activecode:: max-non-consecutive-sum-solution-02
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        Seconde approche : solution récursive avec indice pour permettre la mémoïsation

        ~~~~

        def max_non_consecutive_sum(numbers: list[float], i: int = 0) -> float:
            '''
            # en prenant 3 et 10
            >>> max_non_consecutive_sum([3, 2, 7, 10])
            13
            
            # en prenant 3, 5 et 7
            >>> max_non_consecutive_sum([3, 2, 5, 10, 7])
            15
            
            # en prenant 5, 100 et 5
            >>> max_non_consecutive_sum([5, 5, 10, 100, 10, 5])
            110
            '''
            if i == len(numbers):
                return 0
            elif i == len(numbers) - 1:
                return numbers[i]

            sum1 = numbers[i] + max_non_consecutive_sum(numbers, i + 2)
            sum2 = max_non_consecutive_sum(numbers, i + 1)
            return max(sum1, sum2)

        import doctest
        doctest.testmod()


    ..  activecode:: max-non-consecutive-sum-solution-03
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        Troisième approche : solution récursive avec mémoïsation

        ~~~~

        def max_non_consecutive_sum(numbers: list[float]) -> float:
            '''
            # en prenant 3 et 10
            >>> max_non_consecutive_sum([3, 2, 7, 10])
            13
            
            # en prenant 3, 5 et 7
            >>> max_non_consecutive_sum([3, 2, 5, 10, 7])
            15
            
            # en prenant 5, 100 et 5
            >>> max_non_consecutive_sum([5, 5, 10, 100, 10, 5])
            110
            '''

            memo = {}

            def helper(i: int) -> float:
                if i in memo:
                    return memo[i]
                if i == len(numbers):
                    return 0
                elif i == len(numbers) - 1:
                    return numbers[i]

                sum1 = numbers[i] + helper(i + 2)
                sum2 = helper(i + 1)
                memo[i] = max(sum1, sum2)
                return memo[i]

            return helper(0)

        import doctest
        doctest.testmod()

    ..  activecode:: max-non-consecutive-sum-solution-04
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        Quatrième approche : solution itérative avec table de programmation dynamique

        ~~~~

        def max_non_consecutive_sum(numbers: list[float]) -> float:
            '''
            # en prenant 3 et 10
            >>> max_non_consecutive_sum([3, 2, 7, 10])
            13

            # en prenant 3, 5 et 7
            >>> max_non_consecutive_sum([3, 2, 5, 10, 7])
            15

            # en prenant 5, 100 et 5
            >>> max_non_consecutive_sum([5, 5, 10, 100, 10, 5])
            110
            >>> max_non_consecutive_sum([5, 3, 7, 11, 6])
            18
            '''

            N = len(numbers)
            memo = [None] * (N + 1)
            memo[-1] = 0
            memo[-2] = numbers[-1]

            for i in range(N - 2, -1, -1):
                sum1 = numbers[i] + memo[i + 2]
                sum2 = memo[i + 1]
                memo[i] = max(sum1, sum2)

            return memo[0]

        import doctest
        doctest.testmod()


Exercice 2
==========

Définissez une fonction ``max_grid_sum(grid: list[list[int]]) -> int`` qui prend
en entrée une grille de nombres et retourne la somme maximale que l'on peut
obtenir en partant du coin supérieur gauche et en se déplaçant uniquement vers
la droite ou vers le bas jusqu'au coin inférieur droit.

..  admonition:: Exemples

    ::

        >>> max_grid_sum([[5, 3, 2], [1, 4, 1], [1, 5, 3]])
        16
        >>> max_grid_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        29
        >>> max_grid_sum([[10, 10, 2], [1, 1, 1], [1, 1, 1]])
        22

..  activecode:: dp-exo-02
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    
Exercice 3 (Longest Common Subsequence)
=======================================

Définissez une fonction ``longest_common_subsequence(s1: str, s2: str) -> int``
qui prend en entrée deux chaînes de caractères et retourne la longueur de la
plus longue sous-séquence commune entre les deux chaînes. Une sous-séquence est
une séquence de caractères qui apparaît dans le même ordre dans les deux
chaînes, mais pas nécessairement de manière contiguë.

..  admonition:: Exemples

    ::

        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        4
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        3
        >>> longest_common_subsequence("AAAA", "AA")
        2

..  activecode:: dp-exo-03
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]


Exercice 4 (Distance de Levenshtein)
====================================

Définissez une fonction ``edit_distance(s1: str, s2: str) -> int`` qui prend en
entrée deux chaînes de caractères et retourne la distance d'édition entre les
deux chaînes. La distance d'édition est définie comme le nombre minimum
d'opérations nécessaires pour transformer la chaîne ``s1`` en ``s2``, où les
opérations autorisées sont l'insertion, la suppression ou la substitution d'un
caractère.

..  admonition:: Exemples

    ::

        >>> edit_distance("kitten", "sitting")
        3
        >>> edit_distance("flaw", "lawn")
        2
        >>> edit_distance("intention", "execution")
        5

..  activecode:: dp-exo-04
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]



..  reveal:: dp-exo-04-solution
    :showtitle: Solution
    :hidetitle: Cacher la solution
    :instructoronly:

    La distance d'édition peut être calculée à l'aide d'une table de programmation
    dynamique où l'entrée ``dp[i][j]`` représente la distance d'édition entre les
    sous-chaînes ``s1[:i]`` et ``s2[:j]``.

    Voici une approche récursive pour calculer la distance d'édition :

    ..  code-block:: python

        def edit_distance(s1, s2):
            if not s1:
                return len(s2)
            if not s2:
                return len(s1)

            if s1[-1] == s2[-1]:
                return edit_distance(s1[:-1], s2[:-1])
            else:
                return 1 + min(edit_distance(s1[:-1], s2),      # suppression
                               edit_distance(s1, s2[:-1]),      # insertion
                               edit_distance(s1[:-1], s2[:-1]) # substitution

    Voici une implémentation possible utilisant une approche itérative avec une
    table de programmation dynamique :

    ..  code-block:: python

        def edit_distance(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(m + 1):
                dp[i][0] = i
            for j in range(n + 1):
                dp[0][j] = j

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j] + 1,      # suppression
                                       dp[i][j - 1] + 1,      # insertion
                                       dp[i - 1][j - 1] + 1) # substitution

            return dp[m][n]

Exercice 5 (découpage de tige)
==============================

Définissez une fonction ``rod_cutting(prices: list[int], n: int) -> int`` qui
prend en entrée une liste de prix pour différentes longueurs de tiges et une
longueur totale ``n``, et retourne le profit maximal que l'on peut obtenir en
coupant la tige de longueur ``n`` en différentes longueurs et en vendant les
morceaux selon les prix donnés.

..  admonition:: Exemples

    ::

        >>> rod_cutting([1, 5, 8, 9], 4)
        10
        >>> rod_cutting([3, 5, 8, 9], 4)
        11
        >>> rod_cutting([2, 3, 7, 8], 4)
        9

..  activecode:: dp-exo-05
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]


..  reveal:: dp-exo-05-solution
    :showtitle: Solution
    :hidetitle: Cacher la solution
    :instructoronly:

    La solution au problème de découpage de tige peut être trouvée en utilisant une
    approche de programmation dynamique où l'on construit une table pour stocker
    les profits maximaux pour les différentes longueurs de tige.

    Voici une approche récursive pour résoudre le problème :

    ..  code-block:: python

        def rod_cutting(prices, n):
            if n == 0:
                return 0
            max_profit = 0
            for i in range(1, n + 1):
                max_profit = max(max_profit, prices[i - 1] + rod_cutting(prices, n - i))
            return max_profit

    Voici une approche récursive avec mémoïsation pour éviter les calculs
    redondants :

    ..  code-block:: python

        def rod_cutting_memo(prices, n, memo=None):
            if memo is None:
                memo = {}
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            max_profit = 0
            for i in range(1, n + 1):
                max_profit = max(max_profit, prices[i - 1] + rod_cutting_memo(prices, n - i, memo))
            memo[n] = max_profit
            return max_profit

    Voici une implémentation possible en Python avec table de programmation
    dynamique :

    ..  code-block:: python

        def rod_cutting(prices, n):
            dp = [0] * (n + 1)

            for i in range(1, n + 1):
                max_profit = 0
                for j in range(i):
                    max_profit = max(max_profit, prices[j] + dp[i - j - 1])
                dp[i] = max_profit

            return dp[n]