.. _challenge-recursion.rst:

Challenge : algorithmes récursifs
#################################

..  contents:: Contenu de la page
    :depth: 3

..  note::

    Ce challenge consiste à résoudre quelques problèmes de manière récursive. Comme
    les autres challenges, il vaut 5 points.

Problème 1 (Fusion de deux listes triées)
=========================================

..  activecode:: challenge_recursion_merge_sorted_lists_rec.py

    Définissez une fonction récursive ``merge_sorted_lists(sorted_1: list,
    sorted_1: list) -> list`` qui prend en paramètre deux listes **triées**
    ``sorted_1`` et ``sorted_2`` et qui retourne la **fusion des listes**, à
    savoir une nouvelle liste triée qui contient tous les éléments de la
    première liste et tous ceux de la deuxième liste.

    ..  admonition:: Indications

        Il faut considérer plusieurs cas de base pour ce problème. De même, il y
        a plusieurs appels récursifs différents.

        Commencez par déterminer les cas de base. La question à poser est pour
        quelles valeurs de ``list1`` et ``list2`` le résultat est-il trivial?

    ..  admonition:: Exemples d'utilisation

        ::

            >>> merge_sorted_lists([], [1, 3, 6])
            [1, 3, 6]
            >>> merge_sorted_lists([1, 3, 6], [])
            [1, 3, 6]
            >>> merge_sorted_lists([1, 3, 6], [1, 3, 6])
            [1, 1, 3, 3, 6, 6]
            >>> merge_sorted_lists([1], [1, 3, 6])
            [1, 1, 3, 6]
            >>> merge_sorted_lists([3, 6, 9], [1, 4, 12])
            [1, 3, 4, 6, 9, 12]  

    ..  note:: 

        Pour que le challenge soit réussi, la fonction doit être récursive et ne
        contenir aucune boucle ``for`` ou ``while``.

    ~~~~

    def merge_sorted_lists(list1: list, list2: list) -> list:
        '''
        Recursively merges the sorted lists `list1` and `list2`
        and returns the result as a sorted list.
        
        >>> merge_sorted_lists([], [])
        []
        >>> merge_sorted_lists([], [1, 3, 6])
        [1, 3, 6]
        >>> merge_sorted_lists([1, 3, 6], [])
        [1, 3, 6]
        >>> merge_sorted_lists([1], [1, 3, 6])
        [1, 1, 3, 6]
        >>> merge_sorted_lists([3, 6, 9], [1, 4, 12])
        [1, 3, 4, 6, 9, 12]
        >>> merge_sorted_lists([1, 3, 6], [1, 3, 6])
        [1, 1, 3, 3, 6, 6]
        
        '''
        ...

    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez futurecoder.io ou basthon.fr pour bénéficier des doctests")
            
    ====
    
    from unittest.gui import TestCaseGui


    class myTests(TestCaseGui):

        def test_1(self):

            tests = (
                ([], [], []),
                ([], [1, 3, 6], [1, 3, 6]),
                ([1, 3, 6], [], [1, 3, 6]),
                ([1], [1, 3, 6], [1, 1, 3, 6]),
                ([3, 6, 9], [1, 4, 12], [1, 3, 4, 6, 9, 12]),
                ([1, 3, 6], [1, 3, 6], [1, 1, 3, 3, 6, 6]),
            )


            for list1, list2, expected in tests:
                result = merge_sorted_lists(list1, list2)
                
                #feedback = f"La liste fusionnée contient le bon nombre d'éléments"
                #self.assertEqual(len(result), len(expected), feedback)

                feedback = f"Fusion OK pour list1={list1} et list2={list2}"
                self.assertEqual(result, expected, feedback)



    myTests().main()


..  reveal:: 3571e188-7745-4719-8344-8f45cb696e07
    :showtitle: Solution

    La version la plus basique de l'algorithme est la suivante

    ..  code-block:: python

        def merge_sorted_lists(list1: list, list2: list) -> list:
            '''
            Recursively merges the sorted lists `list1` and `list2`
            and returns the result as a sorted list.
            
            >>> merge_sorted_lists([], [])
            []
            >>> merge_sorted_lists([], [1, 3, 6])
            [1, 3, 6]
            >>> merge_sorted_lists([1, 3, 6], [])
            [1, 3, 6]
            >>> merge_sorted_lists([1], [1, 3, 6])
            [1, 1, 3, 6]
            >>> merge_sorted_lists([3, 6, 9], [1, 4, 12])
            [1, 3, 4, 6, 9, 12]
            >>> merge_sorted_lists([1, 3, 6], [1, 3, 6])
            [1, 1, 3, 3, 6, 6]
            
            '''
            if list1 == []:
                return list2
            elif list2 == []:
                return list1
            elif list1[0] > list2[0]:
                return [list2[0]] + merge_sorted_lists(list1, list2[1:])
            else:
                return [list1[0]] + merge_sorted_lists(list1[1:], list2)

Problème 2 (``any`` récursif)
=============================

..  activecode:: challenge_recursion_any_rec.py

    Développez une fonction ``any(items: list[bool]) -> bool`` qui prend en
    paramètre une liste ``items``. Elle doit retourner ``False`` si et seulement
    si tous les éléments de ``items`` sont "falsy" et ``True`` dans tous les
    autres cas. Si la liste ``items`` est vide, la fonction doit retourner
    ``False``.

    ..  note:: 

        En Python, un objet ``obj`` est "truthy" si et seulement si ``bool(obj)
        == True`` et "falsy" dans le cas contraire.
    
    ..  note:: 

        En Python, il existe une telle fonction ``any(iterable) -> bool`` .

        ::

            >>> any([False, False, True])
            True
            >>> any([False, True, False])
            True
            >>> any([0, 0, 1])
            True
            >>> any([False, False, False])
            False
            >>> any([0, 0, 0])
            False
            >>> any([])
            False

    ~~~~

    def any(items: list[bool]) -> bool:
        '''
        
        >>> any([False, False, True])
        True
        >>> any([False, True, False])
        True
        >>> any([0, 0, 1])
        True
        >>> any([False, False, False])
        False
        >>> any([0, 0, 0])
        False
        >>> any([])
        False

        '''
        ...
                    
    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez futurecoder.io ou basthon.fr pour bénéficier des doctests")

    ====
    
    from unittest.gui import TestCaseGui


    class myTests(TestCaseGui):

        def test_1(self):

            tests = (
                ([False, False, True], True),
                ([False, True, False], True),
                ([0, 0, 1], True),
                ([False, False, False], False),
                ([0, 0, 0], False),
                ([], False),
            )


            for items, expected in tests:
                result = any(items)
                
                feedback = f"OK pour items={items}"
                self.assertEqual(result, expected, feedback)


    myTests().main()

..  reveal:: 242ed5fc-eb94-4421-89a3-6524d9cb8680
    :showtitle: Solution

    La version la plus basique de l'algorithme est la suivante

    ..  code-block:: python

        def any(items: list[bool]) -> bool:
            '''
            
            >>> any([False, False, True])
            True
            >>> any([False, True, False])
            True
            >>> any([0, 0, 1])
            True
            >>> any([False, False, False])
            False
            >>> any([0, 0, 0])
            False
            >>> any([])
            False

            '''
            if items ==  []:
                return False
            else:
                head = items[0]
                tail = items[1:]
                return bool(head) or any(tail)

Problème 3 (``any`` itératif)
=============================

..  activecode:: challenge_recursion_any_iter.py

    Développez une variante itérative (donc non récursive) de la fonction
    ``any`` du problème précédent. Votre fonction doit avoir une complexité
    temporelle :math:`O(n)` dans le pire des cas et une complexité spatiale (en
    ne comptant pas la liste ``items``) :math:`O(1)`.

    ~~~~

    def any(items: list[bool]) -> bool:
        '''
        
        >>> any([False, False, True])
        True
        >>> any([False, True, False])
        True
        >>> any([0, 0, 1])
        True
        >>> any([False, False, False])
        False
        >>> any([0, 0, 0])
        False
        >>> any([])
        False

        '''
        ...

    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez futurecoder.io ou basthon.fr pour bénéficier des doctests")

    ====
    
    from unittest.gui import TestCaseGui


    class myTests(TestCaseGui):

        def test_1(self):

            tests = (
                ([False, False, True], True),
                ([False, True, False], True),
                ([0, 0, 1], True),
                ([False, False, False], False),
                ([0, 0, 0], False),
                ([], False),
            )


            for items, expected in tests:
                result = any(items)
                
                feedback = f"OK pour items={items}"
                self.assertEqual(result, expected, feedback)


    myTests().main()

..  reveal:: a5b85499-1d06-4a2e-92c8-02205f752074
    :showtitle: Solution

    La version la plus basique de l'algorithme est la suivante

    ..  code-block:: python

        def any(items: list[bool]) -> bool:
            for item in items:
                if item:
                    return True
            else:
                return False

Problème 4.A (``map`` récursif)
===============================

..  activecode:: challenge_recursion_map.py

    Développez une fonction récursive ``map(items: list[any], f: Callable) ->
    list[any]`` qui retourne la liste ``[f(x) for x in items]``.

    ..  note:: 

        Votre fonction ne doit pas utiliser de boucle ``for`` ou ``while``.

    ..  note::

        Le module ``typing`` n'est pas disponible sur le site. Utilisez un
        environnement Python standard pour développer votre code. 

    ~~~~

    def map(items: list[any], f) -> list[any]:
        '''
        
        >>> map([1, 2, 3, 4], lambda x: x ** 2)
        [1, 4, 9, 16]
        >>> map([], lambda x: x ** 2)
        []
        >>> map([1, 2, 3, 4], lambda x: x % 2)
        [1, 0, 1, 0]

        '''
        ...

    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez futurecoder.io ou basthon.fr pour bénéficier des doctests")

    ====
    
    from unittest.gui import TestCaseGui


    class myTests(TestCaseGui):

        def test_1(self):

            tests = (
                (([1, 2, 3, 4], lambda x: x ** 2), [1, 4, 9, 16]),
                (([], lambda x: x ** 2), []),
                (([1, 2, 3, 4], lambda x: x % 2), [1, 0, 1, 0]),
            )


            for (items, f), expected in tests:
                result = map(items, f)
                
                feedback = f"OK pour items={items}"
                self.assertEqual(result, expected, feedback)


    myTests().main()



..  reveal:: 5196859c-4f8c-4bc0-98b3-7b69ec59f7fb
    :showtitle: Solution

    La version la plus basique de l'algorithme est la suivante

    ..  code-block:: python

        from typing import Callable

        def map(items: list[any], f: Callable) -> list[any]:
            '''
            
            >>> map([1, 2, 3, 4], lambda x: x ** 2)
            [1, 4, 9, 16]
            >>> map([], lambda x: x ** 2)
            []
            >>> map([1, 2, 3, 4], lambda x: x % 2)
            [1, 0, 1, 0]
            
            '''
            if items == []:
                return []
            else:
                head = items[0]
                tail = items[1:]
                return [f(head)] + map(tail, f)



Problème 5 : (``reduce``)
=========================

Consigne
--------

Le code ci-dessous implémente de manière itérative la fonction ``reduce(items:
list[T], init_value: T, f: Callable[[T, T], T]) -> T`` qui prend en paramètre
une liste d'éléments de type ``T``, une valeur initiale ``init_value`` de type
``T`` et une fonction ``f`` prenant deux paramètres ``a`` et ``b`` de type ``T``
et les combine pour retourner une seule valeur de type ``T``.

..  admonition:: Exemple

    Par exemple, si ``f`` est la fonction qui retourne la somme de ses deux
    paramètres, on peut utiliser la fonction ``reduce(items, f)`` pour effectuer
    la somme de tous les éléments de la liste ``items = [1, 2, 3, 4]``

    ..  activecode:: f91fed07-260b-4aab-87a1-91b4149b1803

        def add(a: float, b: float) -> float:
            return a + b

        def mult(a: float, b: float) -> float:
            return a * b

        def reduce_iter(items: list[any], init_value: any, f) -> any:
            result = init_value
            for item in items:
                result = f(result, item)
            return result

        items: list[float] = [1,2,3,4]
        print(f"Somme de la liste {items}: {reduce_iter(items, 0, add)}")
        print(f"Produit de la liste {items}: {reduce_iter(items, 1, mult)}")


..  activecode:: challenge_recursion_reduce.py

    Implémentez la fonction ``reduce`` de manière récursive pour qu'elle
    fonctionne comme la fonction ``reduce`` itérative développée ci-dessus. Le
    paramètre ``init_value`` est facultatif. S'il n'est pas fourni, il faut
    prendre ``items[0]`` comme valeur initiale.

    ..  note::

        Si la liste ``items`` est vide, la fonction ``reduce`` doit retourner
        ``init_value``. Si ``init_value`` n'est pas spécifié et que la liste
        ``items`` est vide, la fonction doit lever une exception ``ValueError``
        avec un message approprié (voir doctests).

    L'exécution peut être effectuée de manière récursive de la manière suivante:

    ::

        reduce(items, f, init_value) -> 
            f(items[3],
                f(items[2],
                    f(items[1],
                        f(items[0], init_value))))
            

    Le calcul ``reduce([1, 2, 3, 4], add, 0)`` doit donc être effectué de la
    manière suivante:

    ::

        add(4, add(3, add(2, add(1, 0))))

    Si le paramètre ``init_value`` n'est pas fourni, le calcul doit se faire en
    prenant ``init_value = items[0]``. Ainsi, le calcul ``reduce([1, 3, 8, 6],
    max)`` doit se faire comme suit:

    ::

        max(6, max(8, max(1, 3)))

    Si la liste ``items`` est vide, la fonction doit retourner ``init_value``.
    Si ``init_value`` n'est pas fourni, la liste ne peut pas être vide et la
    fonction ``reduce`` doit retourner ``items[0]``.

    ~~~~

    def reduce(items: list[any], f, init_value: any = None) -> any:
        '''
        >>> add = lambda a, b: a + b
        >>> mult = lambda a, b: a * b
        >>> max = lambda a, b: a if a > b else b
        >>> min = lambda a, b: a if a < b else b
        >>> reduce([1, 4, 3, 6], add, 0)
        14
        >>> reduce([1], add, 0)
        1
        >>> reduce([], add, 0)
        0
        >>> reduce([1, 4, 3, 6], mult, 1)
        72
        >>> reduce([1, 4, 3, 8, 6], max, 1)
        8
        >>> reduce([1, 4, 3, 8, 6], max)
        8
        >>> reduce([3], max)
        3
        >>> reduce([], max)
        Traceback (most recent call last):
        ...
        ValueError: When init_value is None, items must contain at least 1 element
        >>> reduce([1, 4, 3, 8, 6], min)
        1
        
        '''
        ...

    
    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez futurecoder.io ou basthon.fr pour bénéficier des doctests")

    ====

    from unittest.gui import TestCaseGui

    add = lambda a, b: a + b
    mult = lambda a, b: a * b
    max = lambda a, b: a if a > b else b
    min = lambda a, b: a if a < b else b

    class myTests(TestCaseGui):

        def test_1(self):

            tests = (
                (([1, 4, 3, 6], add, 0), 14),
                (([1], add, 0), 1),
                (([], add, 0), 0),
                (([1, 4, 3, 6], mult, 1), 72),
                (([1, 4, 3, 8, 6], max, 1), 8),
                (([1, 4, 3, 8, 6], max, None), 8),
                (([3], max, None), 3),
            )


            for (items, fn, init_value), expected in tests:
                result = reduce(items, fn, init_value)

                feedback = f"OK pour items={items} et fn={fn}"
                self.assertEqual(result, expected, feedback)

        def test_raises_value_error(self):
            with self.assertRaises(ValueError) as context:
                reduce([], max)
            err_msg = 'When init_value is None, items must contain at least 1 element'
            feedback = f"Exception ValueError levée avec message correct"
            self.assertTrue(err_msg in context.exception.args, feedback=feedback)


    myTests().main()    

..  reveal:: 963f2423-f303-443b-8bb1-d5757650a8b4
    :showtitle: Solution

    ..  activecode:: 9841b093-253c-4b5f-bb90-26ac9d484b79

        def reduce(items: list[any], f, init_value: any = None) -> any:
            '''
            >>> add = lambda a, b: a + b
            >>> mult = lambda a, b: a * b
            >>> max = lambda a, b: a if a > b else b
            >>> min = lambda a, b: a if a < b else b
            >>> reduce([1, 4, 3, 6], add, 0)
            14
            >>> reduce([1], add, 0)
            1
            >>> reduce([], add, 0)
            0
            >>> reduce([1, 4, 3, 6], mult, 1)
            72
            >>> reduce([1, 4, 3, 8, 6], max, 1)
            8
            >>> reduce([1, 4, 3, 8, 6], max)
            8
            >>> reduce([3], max)
            3
            >>> reduce([], max)
            Traceback (most recent call last):
            ...
            ValueError: When init_value is None, items must contain at least 1 element
            >>> reduce([1, 4, 3, 8, 6], min)
            1
            
            '''
                
            if init_value is None:
                if len(items) > 0:
                    return reduce(items[1:], f, items[0])
                else:
                    raise ValueError("When init_value is None, items must contain at least 1 element")
                
            elif len(items) == 0:
                return init_value
            else: 
                return reduce(items[1:], f, f(items[0], init_value))
                
            


        try:
            import doctest
            doctest.testmod()
        except:
            print("Utilisez futurecoder.io ou basthon.fr pour bénéficier des doctests")
