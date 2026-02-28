.. _exos.rst:

Exercices
#########

..  contents:: Exercices
    :depth: 3

..  note:: 

    Les solutions aux exercices ne sont pas disponibles pour le moment. Les
    exercices difficiles sont marqués d'une étoile. Plus il y a d'étoiles, plus
    vous allez transpirer ...

Exercice 1
==========

Améliorez la fonction ``check_constraints`` utilisée pour résoudre le problèmes
des :math:`n` dames pour qu'il n'y ait plus que deux conditions à tester, sans
utiliser d'opérateur logique (``or``). Tester ensuite votre code à l'aide de
``doctest``.

..  reveal:: 1fce8cad-da1c-43bb-95fa-716fde2c68c6
    :showtitle: Indice 1

    Il faut utiliser une fonction mathématique très simple et familière pour
    gérer les deux contraintes de diagonales avec une seule condition.

..  activecode:: session1-exos-simplify-check-constraints
    :language: webtp

        def check_constraints(q: list[int | None], n: int) -> bool:
            '''
            Vérifie que toutes les contraintes du problème soient satisfaites dans la
            solution partielle ``q`` représentant la ligne sur laquelle est placée chaque dames
            q[i]. On ne considère que les j premiers éléments de la liste q.

            >>> check_constraints([0], 1)
            True
            >>> check_constraints([1, 3, None, None], 2)
            True
            >>> check_constraints([1, None, None, None], 1)
            True
            >>> check_constraints([3, None, None, None], 1)
            True
            >>> check_constraints([1, 3, 5, 0, 2, 4], 6)
            True
            >>> check_constraints([1, 3, None, None], 2)
            True

            >>> check_constraints([0, 1, 2, 3], 4)
            False
            >>> check_constraints([3, 2, None, None], 2)
            False
            >>> check_constraints([2, 3, None, None], 2)
            False
            >>> check_constraints([1, 1, None, None, None], 2)
            False

            '''

            for i in range(n):
                for j in range(i + 1, n):
                    if q[i] == q[j]: return False
                    if q[i] - q[j] == i - j: return False
                    if q[j] - q[i] == i - j: return False

            return True 

        if __name__ == '__main__':
            import doctest
            doctest.testmod


..  reveal:: 1fce8cad-da1c-43bb-95fa-716fde2c68c6-solution
    :showtitle: Solution
    :instructoronly:

    ..  admonition:: Solution

        Il faut utiliser la valeur absolue ``abs(x)`` pour résumer en une seule
        condition les deux conditions de diagonales:

        ..  code-block:: python

            def check_constraints(q: list[int | None], n: int) -> bool:
                '''
                Vérifie que toutes les contraintes du problème soient satisfaites dans la
                solution partielle ``q`` représentant la ligne sur laquelle est placée chaque dames
                q[i]. On ne considère que les j premiers éléments de la liste q.

                >>> check_constraints([0], 1)
                True
                >>> check_constraints([1, 3, None, None], 2)
                True
                >>> check_constraints([1, None, None, None], 1)
                True
                >>> check_constraints([3, None, None, None], 1)
                True
                >>> check_constraints([1, 3, 5, 0, 2, 4], 6)
                True
                >>> check_constraints([1, 3, None, None], 2)
                True

                >>> check_constraints([0, 1, 2, 3], 4)
                False
                >>> check_constraints([3, 2, None, None], 2)
                False
                >>> check_constraints([2, 3, None, None], 2)
                False
                >>> check_constraints([1, 1, None, None, None], 2)
                False

                '''

                for i in range(n):
                    for j in range(i + 1, n):
                        if q[i] == q[j]: return False
                        if abs(q[i] - q[j]) == i - j: return False

                return True 

        if __name__ == '__main__':
            import doctest
            doctest.testmod

Exercice 2
==========

Exercice 2a
-----------

Développez une fonction ``hsymmetry(q: list[int | None]) -> list[int | None]``
qui effectue une symétrie axiale d'axe horizontal. Si :math:`n` est impair, la
ligne centrale ne change pas. 

..  note:: 

    -   Développez vous-mêmes vos propres tests à l'aide du module ``doctest`` pour
        valider votre fonction.

    -   Il est possible de résoudre le problème en une seule ligne à l'aide
        d'une liste en compréhension et d'une expression conditionnelle.

..  activecode:: session1-exos-horiz-symmetry
    :language: webtp

    type PartialChessboard =ist[int | None]

    def vsymmetry(q: PartialChessboard) -> PartialChessboard:
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()
    
..  reveal:: ff9f6603-3aa4-4002-88c0-a38b9ae134e5
    :showtitle: Solution
    :instructoronly:

    On peut développer cette fonction en une seule ligne en utilisant
    judicieusement une liste en compréhension combinée avec une expression
    conditionnelle
    
    ::
        
        <expression_si_vrai> if <condition> else  <expression_si_faux>

    ..  note::

        Dans les tests, il est important de tester également des cas de figure
        où certains éléments de l'échiquier sont ``None``.

    ..  note:: 

        Attention à bien mettre la condition ``row_no is not None`` et pas
        seulement ``if row_no``, condition qui est fausse pour la valeur entière
        ``0``.
    
    ..  code-block:: python

        type PartialChessboard = list[int | None]
        def hsymmetry(q: PartialChessboard) -> PartialChessboard:
            '''
            >>> hsymmetry([0, 1, 2, 3])
            [3, 2, 1, 0]
            >>> hsymmetry([0, None, 2, 3])
            [3, None, 1, 0]
            >>> hsymmetry([0, 1, 1, 0])
            [3, 2, 2, 3]
            >>> hsymmetry([0, 1, 2, 3, 4])
            [4, 3, 2, 1, 0]
            >>> hsymmetry([0, 1, 2, 1, 0])
            [4, 3, 2, 3, 4]
            >>> hsymmetry([0])
            [0]
            '''
            n = len(q)
            return [((n - row_no - 1) if row_no is not None else None) for row_no in q]


        if __name__ == '__main__':
            import doctest
            doctest.testmod()



Exercice 2b
-----------

Développez une fonction ``vsymmetry(q: PartialChessboard) -> PartialChessboard``
qui effectue une symétrie axiale d'axe vertical. Si :math:`n` est impair, la
colonne centrale ne change pas. 

..  note:: 

    Développez vous-mêmes vos propres tests à l'aide du module ``doctest`` pour
    valider votre fonction.

    Le problème peut se résoudre en une seule ligne.

..  activecode:: session1-exos-vert-symmetry
    :language: webtp

    type PartialChessboard = list[int | None]

    def vsymmetry(q: PartialChessboard) -> PartialChessboard:
        ...


    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: d856a8ed-c858-46f9-8ac9-95b49c92261b
    :showtitle: Solution
    :instructoronly:

    ..  code-block:: python

        type PartialChessboard = list[int | None]

        def vsymmetry(q: PartialChessboard) -> PartialChessboard:
            '''
            >>> vsymmetry([0, 1, 2, 3])
            [3, 2, 1, 0]
            >>> vsymmetry([0, 1, 2, None])
            [None, 2, 1, 0]
            '''
            return list(reversed(q))


        if __name__ == '__main__':
            import doctest
            doctest.testmod()


Exercice 2c
-----------

Développez une fonction ``dsymmetry(q: PartialChessboard) -> PartialChessboard``
qui effectue une symétrie axiale d'axe correspondant à la grande diagonale
ascendante de l'échiquier. 

..  note:: 

    Développez vous-mêmes vos propres tests à l'aide du module ``doctest`` pour
    valider votre fonction.

..  activecode:: session1-exos-diag-symmetry
    :language: webtp

    type PartialChessboard = list[int | None]

    def dsymmetry(q: PartialChessboard) -> PartialChessboard:
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: 407762ba-33a0-4c49-8e64-0419a980ada7
    :showtitle: Solution
    :instructoronly:

    ..  code-block:: python

        type PartialChessboard = list[int | None]

        def dsymmetry(q: PartialChessboard) -> PartialChessboard:
            '''
            >>> dsymmetry([1, None, None, None])
            [None, 0, None, None]
            >>> dsymmetry([1, None, 3, None])
            [None, 0, None, 2]
            >>> dsymmetry([1, 3, 0, None])
            [2, 0, None, 1]
            >>> dsymmetry([1, 3, 0, 2])
            [2, 0, 3, 1]
            >>> dsymmetry(dsymmetry([1, 3, 0, 2]))
            [1, 3, 0, 2]
            >>> dsymmetry([0])
            [0]
            >>> 
            '''
            n = len(q)
            new_board: PartialChessboard = [None] * n
            for i in range(n):
                if q[i] is not None:
                    new_board[q[i]] = i

            return new_board

        if __name__ == '__main__':
            import doctest
            doctest.testmod()


Exercice 3
==========

Développez une fonction ``rotate(q: PartialChessboard) -> PartialChessboard``
qui prend une configuration ``q`` (solution complète ou partielle) des n dames
et effectue une rotation de 90° vers la droite de l'échiquier.

..  reveal:: 33c8c6ff-82b9-403d-aae9-9a08c2fbefa3
    :showtitle: Indice

    Une rotation de 90° vers la droite de l'échiquier peut se faire par
    composition de deux symétries déjà implémentées dans l'exercice 2.

..  note:: 

    Développez vous-mêmes vos propres tests à l'aide du module ``doctest`` pour
    valider votre fonction.

..  activecode:: session1-exos-rotate
    :language: webtp


..  reveal:: 0903fe22-0e5f-4ad2-b76c-41f20d6197c6
    :showtitle: Solution
    :hidetitle: Cacher la solution
    :instructoronly:

    ..  code-block:: python

        type PartialChessboard = list[int | None]

        def hsymmetry(q: PartialChessboard) -> PartialChessboard:
            n = len(q)
            return [(n-row -1) if row is not None else None for row in q]


        def dsymmetry(q: PartialChessboard) -> PartialChessboard:
            n = len(q)
            new_board: PartialChessboard = [None] * n
            for i in range(n):
                if q[i] is not None:
                    new_board[q[i]] = i

            return new_board


        def rotate(q: PartialChessboard) -> PartialChessboard:
            '''
            >>> rotate([2, 0, 3, 1])
            [2, 0, 3, 1]
            >>> rotate([2, None, 3, 1])
            [None, 0, 3, 1]
            >>> rotate([1, 3, 5, 0, 2, 4])
            [2, 5, 1, 4, 0, 3]
            >>> rotate([1, None, None, 0, 2, 4])
            [2, 5, 1, None, 0, None]
            >>> 
            '''
            return hsymmetry(dsymmetry(q))

        if __name__ == '__main__':
            import doctest
            doctest.testmod()


Exercice 4
==========

Modifiez le programme DFS + élagage pour casser la symétrie axiale d'axe
horizontal, afin d'éliminer la moitié de l'arbre de recherche. 

..  reveal:: 931aeedd-7248-463d-bb0c-2057d1cd2f41
    :showtitle: Indice 1

    ..  admonition:: Indice 1

        Il faut rajouter une contrainte supplémentaire dans la fonction
        ``check_constraints``.

Cette astuce a l'avantage d'éliminer la moitié de l'arbre de recherche, mais
comporte le désavantage de supprimer la moitié des solutions retournées par la
fonction ``nqueens_solver``. Reconstruisez ces solutions manquantes à partir des
solutions obtenues et de la fonction ``hsymetry`` de l'exercice.

..  note:: 

    Développez vous-mêmes vos propres tests à l'aide du module ``doctest`` pour
    valider votre fonction.

..  activecode:: session1-exo-break-axial-symmetry
    :language: webtp




Exercice 5 (**)
===============

Dans la résolution d'un problème de satisfaction de contraintes, on peut souvent
essayer d'élaguer encore davantage l'arbre de recherche en utilisant des
heuristiques de placement des dames. Au fond cela est logique : une heuristique
parfaite consisterait à parcourir l'arbre de recherche en choisissant toujours
la meilleure ligne pour chaque reine. Cela permettrait de résoudre le problème
des :math:`n` dames en :math:`n` étapes. Évidemment, si l'on connaissait
l'heuristique parfaite, il n'y aurait plus d'intérêt d'utiliser l'ordinateur
pour résoudre le problème...

Mais on peut essayer de s'en approcher. Par exemple, on pourrait placer les
reines dans un autre ordre que forcément depuis le bas jusqu'en haut de
l'échiquer. On pourrait aussi essayer de placer les reines des colonnes du
milieu d'abord au lieu de commencer par les reines à gauche de l'échiquier. La
logique est qu'une reine du milieu rajoute plus de contraintes sur les reines
futures, ce qui élague automatiquement plus de branches de l'arbre lors du
placement des futures reines.

Cette heuristique correspond au fond au bon sens consistant à placer les reines
les plus difficiles à placer en premier.

Implémentez cette heuristique de placement en modifiant la fonction récursive
``dfs`` de la section :ref:`dfs-pruning.rst`.


..  note:: 

    Les modifications à apporter sont assez substantielles. Validez l'exactitude
    de votre fonction en générant d'abord les solutions correctes à partir d'un
    précédent programme que vous savez être correct.


..  activecode:: session1-exo-maxconflict-heuristic
    :language: webtp


Exercice 6 (**)
===============

Implémentez un algorithme *min-conflicts* pour trouver une solution au problème
des :math:`n` dames pour des grands :math:`n`. Cette approche est très
différente de celle abordée au cours. Au lieu de rechercher toutes les solutions
possibles en effectuant une recherche exhaustive, on part d'une solution
initiale possédant des conflits et on essaye de "réparer" progressivement la
solution en éliminant les conflits (échanges de reines par exemple) jusqu'à ce
qu'il n'y en ait plus du tout. On peut même combiner cette approche avec
l'approche exhaustive en faisant une bonne partie du travail avec l'heuristique
min-conflicts, puis en résolvant les derniers conflits (parfois difficile avec
min-conclicts) avec une recherche exhaustive utilisant du raisonnement.

Référence : https://en.wikipedia.org/wiki/Min-conflicts_algorithm

..  note::

    Les meilleurs solveurs de contraintes combinent plusieurs approches
    complémentaires pour résoudre un problème, parmi lesquelles on a par
    exemple:

    - Raisonnements logiques avec solveurs SAT
    - Programmation en nombres entiers (MIP solveurs)
    - Recherche locale et métaheuristiques
    - Recherche systématique (programmation par contraintes)

..  activecode:: session1-exo-minconflict-heuristic
    :language: webtp
