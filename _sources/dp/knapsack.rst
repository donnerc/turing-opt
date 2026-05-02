.. _knapsack-dp.rst:

Le problème du sac à dos avec la programmation dynamique
########################################################

..  contents:: Contenu de la page
    :depth: 3

Nous avons déjà présenté le problème du sac à dos dans la section
:ref:`01-knapsack.rst`. Nous allons maintenant programmer une solution au
problème du sac à dos en utilisant la programmation dynamique. Nous allons
d'abord présenter le problème de manière intuitive, puis le formuler de manière
mathématique et enfin le résoudre par la force brute, par une approche gloutonne
et par la programmation dynamique.

..  note::

    Les explications détaillées et les solutions se trouvent dans
    https://gyminf-ads2-dp.surge.sh/knapsack-dp.html

Instance ``toy-instance``
=========================

Nous allons tester différentes approches sur l'instance suivante du problème du
sac à dos, ne contient que très peu d'articles. Nous allons ensuite appliquer
les différentes approches à des instances plus grandes du problème.

.. _table-knapsack-items-example-1:

..  csv-table:: Articles disponibles dans la réserve alimentaire
    :header-rows: 1
    :class: longtable

    No article, Description, Volume [L], Valeur nutritive [kcal]
    0, Paquet de pâtes, 13, 2600
    1, Paquet de pâtes, 13, 2600
    2, Paquet de pâtes, 13, 2600
    3, Pommes, 10, 500
    4, Paquet de riz, 24, 4500
    5, Yogourt, 11, 960

..  admonition:: Remarques

    Pour résoudre le problème, il faut prendre en compte les remarques suivantes:

    *   Pour pouvoir utiliser la programmation dynamique, on impose que tous les
        volumes et la capacité du sac soient des nombres entiers. Si, dans la
        vraie vie, les nombres ne sont pas entiers, on peut toujours transformer
        le problème en multipliant tous les volumes et la capacité par un
        facteur commun pour que les volumes et la capacité du sac à dos soient
        des nombres entiers.

    *   Chaque paquet de pâtes constitue un article à part entière et est donc
        noté dans une ligne à part entière dans le tableau.

    *   La colonne "Description" du tableau n'a aucune importance dans le
        problème. On ne prend en compte que le volume et la valeur nutritive des
        aliments.

    *   On ne peut pas "ouvrir" un paquet de pâtes pour prendre la moitié du
        paquet. Pour chaque article, soit on le prend complètement, soit on ne
        le prend pas du tout, d'où le nom du problème **0-1**-Knapsack Problem.

    *   On aurait pu remplacer les volumes en [l] par des poids en [kg] et
        mettre une contrainte de poids maximal de 50 kg au le sac à dos au lieu
        des 50 litres de contenance.

Formulation mathématique (Rappel)
---------------------------------

Mathématiquement, on formule le problème à l'aide de variables de décision, de
contraintes et d'une **fonction objectif** (= valeur à optimiser). On considère
que :math:`N` est le nombre d'objets emportés. Les données du problème sont les
suivantes:

..  admonition:: Données connues du problème

    On peut représenter le problème à l'aide de trois listes 

    - La liste ``V`` dont chaque élément ``V[i]`` indique le volume de l'objet
      numéro :math:`i`.

    - Liste ``N`` dont chaque élément ``N[i]`` indique la valeur nutritive de
      l'objet numéro :math:`i`.

..  admonition:: Variables de décision

    Dans ce problème, les variables de décision sont des variables binaires
    :math:`x_i \in \{0, 1\}` définies de la manière suivante pour tout
    :math:`0 \leq i \leq N`,

    ..  math::

        x_i = \begin{cases}
        1 &\text{si on prend l'objet $i$} \\
        0 &\text{sinon} \\
        \end{cases}

    Pour l'instance considérée en exemple, il y a six variable de décision
    :math:`x_0, \ldots, x_5`, une pour chacun des articles que l'on peut
    potentiellement emporter.


..  admonition:: Contraintes

    Dans le cas du problème du sac à dos, il n'y a qu'une seule contrainte,
    formulée comme une inéquation linéaire:

    ..  math::

        \sum_{i=0}^{N-1}
        x_i \cdot V[i]
        \leq 
        C

    Pour l'instance considérée en exemple, pour un sac à dos de 50 litres, la
    contrainte s'écrit

    ..  math::
        
        x_0 \cdot 13 + x_1 \cdot 13 + x_2 \cdot 13 + x_3 \cdot 10 + x_4 \cdot 24 + x_5 \cdot 11 \leq 50

..  admonition:: Fonction objectif

    La fonction objectif indique la valeur qui doit être optimisée. Dans notre
    cas, il s'agit de la valeur nutritive totale emportée dans le sac à dos. En
    l'occurrence, la valeur objectif à optimiser est donnée par la fonction

    ..  math::

        f(X) = f(x_0, \ldots, x_{N-1}) = \sum_{i=0}^{N-1} x_i \cdot N[i]

    Pour l'instance considérée en exemple, la fonction objectif est donc

    ..  math::

        f(X) &= f(x_0, x_1, x_2, x_3, x_4, x_5) \\
        &= x_0 \cdot 2600 + x_1 \cdot 2600 + x_2
        \cdot 2600 + x_3 \cdot 500 + x_4 \cdot 4500 + x_5 \cdot 960

        
Résoudre le problème du sac à dos consiste à attribuer à chaque variable de
décision :math:`x_i` une valeur dans :math:`\{0, 1\}` de telle manière que
toutes les contraintes soient satisfaites. De plus, il faut trouver une solution
optimale, à savoir une solution qui maximise la fonction objectif :math:`f`. La
programmation dynamique se préoccupe avant tout de trouver le profit maximal et
détermine les objets à rajouter concrètement dans le sac une fois le problème de
la valeur optimale connue.

Résolution par la force brute
=============================

Commençons par une approche naïve de résolution du problème du sac à dos, à
savoir la force brute. L'idée est de générer toutes les combinaisons possibles
d'objets à emporter, de vérifier pour chacune d'entre elles si elle respecte la
contrainte de capacité du sac à dos et de calculer la valeur nutritive totale
emportée pour chacune d'entre elles. On peut ensuite sélectionner la combinaison
qui respecte la contrainte et qui maximise la valeur nutritive totale emportée.

..  activecode:: knapsack_brute_force_py
    :language: webtp
    :interpreterargs: debug_mode=true&layout=["Editor", "Console"]

    Développez une fonction ``knapsack_solver(profits: list[int], weights:
    list[int], capacity: int) -> list [int]`` qui retourne **une** solution
    optimale (il peut y en avoir plusieurs). Vous pouvez utiliser les données de
    l'instance ``toy-instance`` présentée ci-dessus pour tester votre fonction.

    Définissez également une fonction ``volume(solution: list[int], weights:
    list[int]) -> int`` qui calcule le volume total de la solution donnée en
    argument. De même, définissez une fonction ``profit(solution: list[int],
    profits: list[int]) -> int`` qui calcule le profit total de la solution
    donnée en argument.

    ~~~~

    # Données de l'instance
    N = [2600, 2600, 2600, 500, 4050, 960]
    V = [13, 13, 13, 10, 24, 11]
    C = 50

    # Domaine de valeurs des variables de décision
    domain = [0, 1]

    def volume(solution: list[int], weights: list[int]) -> int:
        '''
        >>> volume([1, 0, 1, 0, 1, 0], V)
        50
        '''
        ...

    def profit(solution: list[int], profits: list[int]) -> int:
        '''
        >>> profit([1, 0, 1, 0, 1, 0], N)
        9700
        '''
        ...

    def bf_knapsack_solver(profits: list[int], weights: list[int], capacity: int) -> int:
        '''
        >>> solution = bf_knapsack_solver(N, V, C)
        >>> solution in [(1, 1, 0, 0, 1, 0), (1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0)]
        True
        '''

        ...

    import doctest
    doctest.testmod()


Analyse de la complexité de l'approche par la force brute
---------------------------------------------------------

..  shortanswer:: knapsack-brute-force-complexity

    Faites une analyse de la complexité de l'approche par la force brute. En
    particulier, quelle est la complexité temporelle et spatiale de cette
    approche?

..  reveal:: knapsack-brute-force-complexity-solution
    :showtitle: Solution
    :hidetitle: Cacher la solution

    ..  admonition:: Solution

        La complexité temporelle de l'approche par la force brute est en
        :math:`O(2^N)`, où :math:`N` est le nombre d'objets disponibles. En
        effet, il y a :math:`2^N` combinaisons possibles d'objets à emporter
        (chaque objet peut être soit pris, soit laissé). La complexité spatiale
        de cette approche est en :math:`O(N)` si on considère que l'on stocke
        uniquement la meilleure combinaison trouvée jusqu'à présent, ou en
        :math:`O(2^N)` si on stocke toutes les combinaisons générées.

Approche récursive avec mémoïsation (Top-Down)
==============================================

..  activecode:: knapsack_top_down_py
    :language: webtp
    :interpreterargs: debug_mode=true&layout=["Editor", "Console"]

    Implémentez une fonction ``knapsack_rec(profits: list[int], weights:
    list[int], capacity: int) -> int`` qui résout le problème du sac à dos en
    utilisant une approche récursive avec mémoïsation (Top-Down). 

    ..  note::

        La fonction retourne uniquement la valeur optimale qu'il est possible de
        mettre dans le sac sans déterminer les objets à emporter (valeur des
        variables de décision). Nous allons voir comment faire cela plus tard
        une fois la valeur optimale connue.

    ~~~~

    # Données de l'instance
    N = [2600, 2600, 2600, 500, 4050, 960]
    V = [13, 13, 13, 10, 24, 11]
    C = 50

    def knapsack_rec(profits: list[int], weights: list[int], capacity: int) -> int:
        '''
        >>> knapsack_rec(N, V, C)
        9700
        '''
        ...

    import doctest
    doctest.testmod()



Approche itérative tabulaire (Bottom-Up)
========================================

Adaptez la version récursive avec mémoïsation du solveur du sac à dos pour
en faire une version itérative tabulaire (Bottom-Up).

Calcul de la valeur optimale du sac à dos
-----------------------------------------

..  activecode:: knapsack_bottom_up_py
    :language: webtp
    :interpreterargs: debug_mode=true&layout=["Editor", "Console"]

    Définissez une fonction ``knapsack_bottom_up(profits: list[int], weights:
    list[int], capacity: int) -> int`` qui résout le problème du sac à dos en
    utilisant une approche itérative tabulaire (Bottom-Up).

    ..  note:: 

        La fonction retourne uniquement la valeur optimale qu'il est possible de
        mettre dans le sac sans déterminer les objets à emporter (valeur des
        variables de décision). Nous allons voir comment faire cela plus tard
        une fois la valeur optimale connue.

    ~~~~

    # Données de l'instance
    N = [2600, 2600, 2600, 500, 4050, 960]
    V = [13, 13, 13, 10, 24, 11]
    C = 50

    def knapsack_bottom_up(profits: list[int], weights: list[int], capacity: int) -> int:
        '''
        >>> knapsack_bottom_up(N, V, C)
        9700
        '''
        ...

    import doctest
    doctest.testmod()


Reconstitution de la solution optimale
--------------------------------------

Une fois le tableau de programmation dynamique rempli, on peut reconstituer la
solution optimale en remontant le tableau à partir de la valeur optimale
trouvée. Cela nous permettra de déterminer quels objets doivent être emportés
dans le sac à dos pour atteindre la valeur optimale.

..  activecode:: knapsack_solution_reconstruction_py
    :language: webtp
    :interpreterargs: debug_mode=true&layout=["Editor", "Console"]

    Rajoutez à la solution de l'étape précédente une fonction
    ``reconstruct_solution(profits: list[int], weights: list[int], capacity:
    int, dp_table: list[list[int]]) -> list[int]`` qui prend en argument le
    tableau de programmation dynamique rempli et retourne une solution optimale
    (une liste de 0 et de 1 indiquant quels objets emporter).

    ~~~~


Complexité de l'approche par la programmation dynamique
=======================================================

..  shortanswer:: knapsack-dp-complexity

    Faites une analyse de la complexité de l'approche par la programmation
    dynamique. En particulier, quelle est la complexité temporelle et spatiale de
    cette approche?

..  reveal:: knapsack-dp-complexity-solution
    :showtitle: Solution
    :hidetitle: Cacher la solution
    :instructoronly:

    ..  admonition:: Solution

        La complexité temporelle de l'approche par la programmation dynamique
        est en :math:`O(N \cdot C)`, où :math:`N` est le nombre d'objets
        disponibles et :math:`C` est la capacité du sac à dos. En effet, il faut
        remplir un tableau de taille :math:`N \times C` et chaque cellule du
        tableau peut être calculée en temps constant. La complexité spatiale de
        cette approche est également en :math:`O(N \cdot C)` si on stocke le
        tableau complet, ou en :math:`O(C)` si on optimise l'espace en ne
        stockant que la dernière ligne du tableau à un moment donné.


Test sur des instances plus grandes
===================================

Testez les deux approches (Top-Down et Bottom-Up) sur des instances plus grandes
du problème du sac à dos. Vous trouverez des instances de test dans le dossier
``data/knapsack``.

