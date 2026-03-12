##########################
Exercices sur la récursion
##########################

..  contents::  Contenu de la page
    :depth: 3

.. _exo_recursive_product:

Exercice 1.A (produit récursif)
===============================

Développer une fonction récursive ``recursive_product(numbers: list[float])
-> float`` qui prend en argument une liste de nombres ``float`` et retourne
la somme de cette liste. La fonction ne doit pas utiliser de boucle ``for``
ou ``while``.

..  admonition:: Conseil
    
    Résolvez l'exercice dans https://webtigerpython.ethz.ch

..  admonition:: Exemple d'utilisation
    :class: note

    ::

        >>> recursive_product([])
        1.0
        >>> recursive_product([6])
        6.0
        >>> recursive_product([6.0, 2])
        12.0
        >>> recursive_product([6, 2, 3])
        36.0

..  activecode:: recursive_product_py
    :language: webtp
    :interpreterargs: branch=branch

    def recursive_product(numbers: list[float]) -> float:
        '''
        >>> recursive_product([])
        1.0
        >>> recursive_product([6])
        6.0
        >>> recursive_product([6.0, 2])
        12.0
        >>> recursive_product([6, 2, 3])
        36.0

        >>> # pas de boucle for ou while
        >>> import inspect
        >>> source = inspect.getsource(recursive_product)
        >>> any(word in source for word in ["for ", "while "])
        False
        '''
        
        ...

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

..  reveal:: 03bbc41c-afca-483a-83d0-1563683e6f07
    :showtitle: Solution

    ..  admonition:: Solution

        ::

            def recursive_product(numbers: list[float]) -> float:
                if len(numbers) == 0:
                    return 1
                else:
                    return numbers[0] * recursive_product(numbers[1:])


Exercice 1.B
============

..  shortanswer:: time-complexity-recursive-product

    Déterminez la complexité temporelle de la fonction récursive
    ``recursive_product(numbers)`` développée à l'exercice précédent.


..  reveal:: 784eac7f-ff61-4976-b129-13261cc1c750
    :showtitle: Solution

    ..  admonition:: Solution

        La complexité temporelle est quadratique dans le nombre :math:`n`
        d'éléments à multiplier. En effet, chaque appel récursif est en
        :math:`\Theta(n)` en raison de la création de la liste ``tail`` avec le
        slicing. Comme il y a :math:`n` appels récursifs, la complexité
        temporelle totale est 

        ..  math::

            n \cdot \Theta(n) = \Theta(n^2)


Exercice 1.C
============

..  shortanswer:: space-complexity-recursive-product

    Déterminez la complexité spatiale de la fonction récursive
    ``recursive_product(numbers)`` développée à l'exercice précédent.

    ..  admonition:: Indication

        N'oubliez pas que, lors de chaque appel récursif, il faut stocker les
        variables locales (dont les paramètres) dans un nouvel espace
        d'exécution sur la pile d'appels et qu'ils vont s'empiler jusqu'à ce
        qu'on atteigne un cas de base et que la fonction se termine.


..  reveal:: 788eedff-7b24-4e7f-b870-87de6e6dee2e
    :showtitle: Solution

    ..  admonition:: Solution

        La complexité spatiale est quadratique. En effet, si :math:`n` est la
        taille de la liste, il faut :math:`n` appels récursifs. Le problème est
        que pour chaque appel récursif, l'opération de slicing ``numbers[1:]``
        qui construit le reste crée une **nouvelle liste**.

        En tout, en plus de la liste de base, il faut donc

        ..  math::

            S(n) = (n-1) + (n-2) + \ldots + 3 + 2 + 1 =
            \frac{(n-1) \cdot n}{2} =
            \frac{n^2 - n}{2} = 
            \frac{1}{2} \cdot n^2 + \frac{1}{2} n

        nombres à stocker en mémoire, fonction qui est en :math:`\Theta(n^2)`.
    

Exercice 2 (optimisation du produit récursif)
=============================================

Dans l'exercice précédent, nous sommes arrivés à la conclusion que la complexité
temporelle est spatiale étaient toutes deux quadratiques, ce qui est bien moins
bon que la version itérative qui est en :math:`\Theta(n)` pour la complexité
temporelle et en :math:`\Theta(1)` pour l'espace mémoire additionnel nécessaire
pour effectuer l'opération.

..  admonition:: Version itérative

    Pour rappel, la version itérative classique est la suivante:

    ..  activecode:: 018f8937-0612-4760-ac5b-dbc83bb74638

        def product_iter(numbers: list[float]) -> list[float]:
            result = 1
            for n in numbers:
                result *= n
            return result

    Cette version n'utilise en effet que la variable ``result`` (accumulateur)
    comme espace mémoire additionnel, ce qui est :math:`\Theta(1)`. De plus,
    chaque opération dans la boucle est :math:`\Theta(1)`, ce qui donne une
    complexité pour toute la boucle de :math:`n\cdot \Theta(1) = \Theta(n)`.

Il est possible de modifier légèrement la manière de faire la récursion pour
travailler lors de chaque appel sur la liste originale au lieu de travailler sur
une copie. Cela permet de régler les deux problèmes de complexités observés dans
le premier exercice. Complétez le code ci-dessous pour terminer la solution
suggérée par les arguments de la fonction récursive. 

..  activecode:: recursive_product__optim_py

    Modifiez la fonction ``recursive_product`` définie à l'exercice
    :ref:`exo_recursive_product` pour que les complexités temporelle et spatiale
    soient linéaires. Pour cela, utilisez un indice ``start: int`` pour indiquer
    à partir de quel élément on doit considérer le début de la liste.

    ..  admonition:: Indication

        Il s'agit de ne pas utiliser le slicing et de travailler sur la liste
        originale en délimitant la partie considérée par des indices passés en
        paramètre lors de l'appel récursif.

    ..  admonition:: Exemples d'utilisation

        Malgré l'indice ``head`` pour indiquer à partir de quelle position il
        faut considérer la liste, faites en sorte que la fonction puisse être
        appelée comme avant, sans avoir à indiquer d'indice de départ.

        ::

            >>> recursive_product([])
            1
            >>> recursive_product([], head=0)
            1
            >>> recursive_product([6, 2, 3], head=0)
            36
            >>> recursive_product([6, 2, 3], head=1)
            6
            >>> recursive_product([6, 2, 3], head=2)
            3
            >>> recursive_product([6, 2, 3], head=3)
            1

    ~~~~

    def recursive_product(numbers: list[float], head: int) -> float:
        '''
        Recursively computes the product of all the elements of `numbers`

        >>> recursive_product([])
        1
        >>> recursive_product([], head=0)
        1
        >>> recursive_product([6, 2, 3], head=0)
        36
        >>> recursive_product([6, 2, 3], head=1)
        6
        >>> recursive_product([6, 2, 3], head=2)
        3
        >>> recursive_product([6, 2, 3], head=3)
        1

        >>> import inspect
        >>> source = inspect.getsource(recursive_product)
        >>> # pas de boucle for ou while
        >>> any(word in source for word in ["for ", "while "])
        False

        >>> # pas de slicing
        >>> any(word in source for word in ["[1:]", "[1 :]", "[ 1:", "[1: ", "[:]", "[: ", "[ :", " [", " ]"])
        False
        '''
        ...

    if __name__ == "__main__":
        import doctest
        doctest.testmod()



..  reveal:: e3010534-73e9-4ad0-9ef1-27428a1ce461
    :showtitle: Solution

    ..  admonition:: Solution

        La fonction ci-dessous calcule en temps linéaire le produit des éléments
        de la liste ``numbers``. La complexité de la mémoire additionnelle est
        aussi linéaire, car chaque appel récursif ne nécessite que de stocker
        l'indice ``head`` et n'a pas à copier le reste de la liste ``numbers``
        avec le slicing.

        La complexité spatiale reste moins bonne que la version itérative, dont
        l'espace additionnel nécessaire était constant. Cela est une règle
        générale avec les algorithmes récursifs : ils sont gourmands en mémoire,
        car il faut sauvegarder les variables locales de chaque appel récursif
        dans la pile d'appels.

        ..  code-block:: python
            :linenos:

            def recursive_product(numbers: list[float], head: int = 0) -> float:
                '''
                Recursively computes the product of all the elements of `numbers`

                >>> recursive_product([])
                1
                >>> recursive_product([], head=0)
                1
                >>> recursive_product([6, 2, 3], head=0)
                36
                >>> recursive_product([6, 2, 3], head=1)
                6
                >>> recursive_product([6, 2, 3], head=2)
                3
                >>> recursive_product([6, 2, 3], head=3)
                1

                '''
                if head == len(numbers):
                    return 1
                else:
                    return numbers[head] * recursive_product(numbers, head=head + 1)    



..
    ..  activecode:: recursive_product_exception_py

        Modifier la fonction ``recursive_product`` pour qu'elle lève une exception
        de type ``ValueError`` avec un message approprié si l'un des éléments de la
        liste n'est pas un nombre.

        ..  admonition:: Consigne supplémentaire

            ``for`` ni ``while``. Comme dans le précédent exercice, résolvez le
            problème sans boucle

        ..  admonition:: Indication
            :class: tip

            Vous pouvez utiliser la fonction ``isinstance(object, classname)`` pour
            déterminer si ``object`` est une instance de la classe ``classname``. Il
            suffit donc de déterminer si l'élément est une instance de ``int`` ou de
            ``float`` et de lever l'exception si nécessaire.

            Documentation : https://docs.python.org/2/library/functions.html#isinstance

            ::

                >>> isinstance(1, int)
                True
                >>> isinstance(1.0, int)
                False
                >>> isinstance(1.0, float)
                True
                >>> isinstance("1", int)
                False

        ~~~~

        ====

        from unittest.gui import TestCaseGui


        class myTests(TestCaseGui):

            def test_1(self):

                tests = (
                    ([], 1.0),
                    ([6], 6.0),
                    ([6, 2], 12.0),
                    ([6, 2, 3], 36.0),
                )


                for numbers, expected in tests:
                    result = recursive_product(numbers)

                    feedback = f"Produit OK pour numbers={numbers}"
                    self.assertEqual(result, expected, feedback)
                    
            def test_raises_value_exception(self):
                self.assertRaises(ValueError, recursive_product, ["salut", 2, 3])


        myTests().main()

    ..  reveal:: 6172f041-a784-40ff-89f8-a69e8212a73b
        :showtitle: Solution

        ..  admonition:: Solution

            Il faut contrôler, avant de faire l'appel récursif, que le premier
            élément de la liste soit bien un nombre avec la fonction ``isinstance``.

            ::
                
                def recursive_product(numbers):
                    if len(numbers) == 0:
                        return 1
                    else:
                        head = numbers[0]
                        tail = numbers[1:]
                        
                        if isinstance(head, int) or isinstance(head, float):
                            return numbers[0] * recursive_product(numbers[1:])
                        else:
                            print(repr(head), type(head))
                            raise ValueError("All elements need to be numbers")
                            


Exercice 3 (Maximum d'une liste)
================================

..  activecode:: max_rec_py

    Développer une fonction récursive ``max_rec(numbers: float) -> float`` qui retourne
    l'élément maximal d'une liste de nombres flottants. Si la liste est vide,
    lever une exception de type ``ValueError``. Il est interdit d'utiliser une
    boucle et la fonction prédéfinie ``max`` dans cet exercice.

    ..  admonition:: Indication
        :class: tip

        Commencer par définir une fonction ``max2(a: float, b: float) -> float`` qui
        retourne le maximum de deux éléments et utiliser cette fonction au sein de
        votre fonction récursive ``max_rec``.

        Prenez la peine de bien définir le cas de base (problème trivial) et la
        manière de réduire la taille du problème.

    ..  admonition:: Complexité spatiale 

        Tâchez de programmer la fonction récursive de manière à conserver une
        complexité spatiale linéaire et éviter qu'elle ne devienne quadratique. Pour
        cela, évitez la copie avec le slicing et privilégiez les indices. Vous
        pouvez commencer par utiliser le slicing pour une première version.

    ~~~~

    def max2(a: float, b: float) -> float:
        '''
        >>> max2(10, 2)
        10
        >>> max2(2, 10)
        10
        >>> max2(2, 2)
        2
        '''
        ...

    def max_rec(numbers: list[float]) -> float:
        '''

        Returns the max of the `numbers` list. Raises a ValueError if the list
        is empty

        >>> max_rec([1])
        1
        >>> max_rec([1, 2])
        2
        >>> max_rec([2, 1])
        2
        >>> max_rec([2, 1, 6, 2, 9])
        9
        >>> max_rec([2, 1, 12, 6, 2, 9])
        12

        >>> import inspect
        >>> source = inspect.getsource(recursive_product)
        >>> # pas de boucle for ou while
        >>> any(word in source for word in ["for ", "while "])
        False

        '''
        ...

    if __name__ == "__main__":
        import doctest
        doctest.testmod()


..  reveal:: f8a7726d-0472-4477-a78f-354dbdad756f
    :showtitle: Solution

    ..  admonition:: Solution
        :class: important

        ..  code-block:: python
            :linenos:

            def max2(a, b):
                if a > b:
                    return a
                else: 
                    return b

            def max_rec(numbers):
                if len(numbers) == 1:
                    return numbers[0]
                else:
                    return max2(numbers[0], max_rec(numbers[1:]))
                
            print(max_rec([1,4,8,3,10, 6]))

    Pour une solution qui n'utilise pas le slicing, on utilise un indice
    ``start: int`` qui indique le début de la liste à considérer:

    ..  code-block:: python
        :linenos:

        def max2(a: float, b: float) -> float:
            '''
            >>> max2(10, 2)
            10
            >>> max2(2, 10)
            10
            >>> max2(2, 2)
            2
            '''
            return a if a > b else b

        def max_rec(numbers: list[float], start: int = 0) -> float:
            '''

            Returns the max of the `numbers` list. 
            Raises a ValueError if the list is empty

            >>> max_rec([1])
            1
            >>> max_rec([1, 2])
            2
            >>> max_rec([2, 1])
            2
            >>> max_rec([2, 1, 6, 2, 9])
            9
            >>> max_rec([2, 1, 12, 6, 2, 9])
            12

            '''
            if len(numbers) == 0:
                raise ValueError("Unable to return the max of an empty list")
            
            if start == len(numbers) - 1:
                return numbers[start]
            else:
                return max2(numbers[start], max_rec(numbers, start=start + 1))



Exercice 4 (détection de palindrome)
====================================

..  activecode:: is_palindrome_rec_py

    Définir une fonction ``is_palindrom(text: str) -> bool`` pour vérifier si la
    chaine de caractères ``text`` est un palindrome. Une chaine de caractères est un
    palindrome si elle est symétrique, à savoir qu'elle est égale à elle-même
    lorsqu'on l'inverse. 

    **Indication** : Ne pas utiliser de boucle ``for`` ou ``while`` mais uniquement
    le principe de la récursion.

    Exemples de palindromes : ``"<><>"``, ``"abccba"``, ``"engagelejeuquejelegagne"``

    ..  admonition:: Exemple d'utilisation
        :class: note

        ::

            >>> is_palindrom("")
            True
            >>> is_palindrom("abab")
            False
            >>> is_palindrom("abccba")
            True
            >>> is_palindrom("engagelejeuquejelegagne")
            True
            >>> is_palindrom("Hello world!")
            False

    ~~~~

    def is_palindrom(text: str) -> bool:
        '''
        >>> is_palindrom("")
        True
        >>> is_palindrom("abab")
        False
        >>> is_palindrom("abccba")
        True
        >>> is_palindrom("engagelejeuquejelegagne")
        True
        >>> is_palindrom("Hello world!")
        False
        '''
        ...

    
    def test():
        import platform
        if platform.python_implementation() == 'CPython':
            import doctest
            doctest.testmod()

    test()


    ====

    from unittest.gui import TestCaseGui


    class myTests(TestCaseGui):

        def test_max_rec(self):

            tests = (
                ("", True),
                ("abab", False),
                ("abccba", True),
                ("engagelejeuquejelegagne", True),
                ("Hello world!", False),
            )

            for text, expected in tests:
                result = is_palindrom(text)
                
                feedback = f"is_palindrom(text={text}) OK"
                self.assertEqual(result, expected, feedback)


    myTests().main()



..  reveal:: 84d48edf-59c7-469a-aed9-052fdab929d5
    :showtitle: Solution

    ..  admonition:: Solution
        :class: important

        Voici une version avec le slicing de complexité quadratique

        ..  code-block:: python
            :linenos:

            def is_palindrom(text):
                if len(text) in [0, 1]:
                    return True
                elif len(text) == 2:
                    return text[0] == text[1]
                else:
                    return text[0] == text[-1] and is_palindrom(text[1:-1])
                    
            def test():
                assert is_palindrom("abba") == True
                assert is_palindrom("") == True
                assert is_palindrom("abcba") == True
                assert is_palindrom("abdcba") == False

            test()

        Pour une version linéaire, il faut éviter d'utiliser le slicing en
        utilisant plutôt des indices pour contrôler les bornes de la liste à
        considérer:

        ..  code-block:: python
            :linenos:

            def is_palindrom(text: str, i: int = 0) -> bool:
                '''
                >>> is_palindrom("")
                True
                >>> is_palindrom("abab")
                False
                >>> is_palindrom("abccba")
                True
                >>> is_palindrom("engagelejeuquejelegagne")
                True
                >>> is_palindrom("Hello world!")
                False
                '''
                if len(text) == 0:
                    return True

                start = i
                end = len(text) - 1 - i
                
                if end - start <= 1:
                    return text[start] == text[end]
                else:
                    return text[start] == text[end] and is_palindrom(text, i = i + 1)

            def test():
                import platform
                if platform.python_implementation() == 'CPython':
                    import doctest
                    doctest.testmod()

            test()


Exercice 5 (tête à toto)
========================

..  activecode:: tete_a_toto_rec.py

    ..  figure:: figures/exercice-tete-toto.png
        :align: center
        :width: 40%


    Comme vous le savez, 0 + 0 = 0. On pourrait aussi dire 0 = (0 + 0). Dans ce
    cas, on peut aussi aller un peu plus loin, et puisque 0 vaut (0 + 0),
    remplacer les 0 de (0 + 0) par leur valeur, et obtenir :

    ::

        0 = ((0 + 0) + (0 + 0)) 
    
    Rien n'empêche de continuer et d'écrire :

    ::

        0 = (((0 + 0) + (0 + 0)) + ((0 + 0) + (0 + 0))) 
    
    Développez une fonction ``toto(n: int) -> str`` qui retourne la chaîne de caractères demandée.

    ..  note:: 

        Vous n'avez pas le droit d'utiliser de boucle dans ce programme.
    

    ..  note::

        Cet exercice est emprunté à France IOI
        (https://www.france-ioi.org/algo/task.php?idChapter=513&idTask=509)

    
    ..  reveal:: 7f903bc7-6608-4768-bca5-81f4a0889bbc
        :showtitle: Indice

        Vous devrez utiliser une fonction récursive, mais ce n'est pas forcément
        la fonction ``toto`` qui doit être récursive.

    ~~~~


    def toto(n: int) -> str:
        '''
        >>> toto(0)
        '0 = 0'
        >>> toto(1)
        '0 = (0 + 0)'
        >>> toto(2)
        '0 = ((0 + 0) + (0 + 0))'
        >>> toto(3)
        '0 = (((0 + 0) + (0 + 0)) + ((0 + 0) + (0 + 0)))'
        >>> toto(4)
        '0 = ((((0 + 0) + (0 + 0)) + ((0 + 0) + (0 + 0))) + (((0 + 0) + (0 + 0)) + ((0 + 0) + (0 + 0))))'
        '''
    
        ...
        

    try:
        import doctest
        doctest.testmod()
    except:
        print("Impossible de lancer les doctests")
    

..  reveal:: b61342f8-c222-4c7a-a9c6-3cdee752af9f
    :showtitle: Solution

    ..  raw:: html

        <iframe 
            width="100%"
            height="500px"
            src="https://webtigerpython.ethz.ch/?code=NobwRAdghgtgpmAXGGUCWEB0AHAnmAGjABMoAXKJMAHQmLgDMACMgezYAoJEmMyBKJgFoAfEwDOZAE6JaTeUwDkyuQpHqW7VhwAM_VfMU6mAXiY7FBpurFtOARn0QFS42d1MA1Of6XnajTttACYnFyNTJg4Pbz0vKONY_l8rZT8XKTgyAFcpZwYIsxAACzgAG2w4KS5-AF90lwVaemZSiqquHj5BUQlpWX9DFUHrDTbK6r1UiysbJnGOx1SYnwb5OYXq0OWVuO9d5LXRsU2OAGYwhUVog_iDwX3b_cSfQ9mx8omOABZLwxungl4noHlFAfdQTcXnsgUlIeDock3iM0lY0MxnCYzDoBo0FJkcnlXEdyuI4Li8Zo2JIpJFTs4hEwliMMllcvlqGAOCAgjTavEeVo-foaBArLRpLgKfI0DBsKwpGQmMRWABjMhwSRWFXqzVkTAayQwVjEDhOOAAD1VcGwZGlTGwUj4HE5AEk5axxOI0AAjMpwZUBspQCDW2n-8TKtWGsjiTn8MC1AC6QA"
        ></iframe>


Exercice 6 (Exponentiation rapide)
==================================

..  activecode:: fast_exp_rec.py

    Développez une fonction récursive ``pow(a: float, b: int) -> float`` qui
    calcule :math:`a^b` de manière rapide. Notez que la puissance :math:`0^0`
    n'est pas bien définie et ne peut être calculée. Levez une exception de type
    ``ValueError`` dans ce cas.

    ..  note::

        Pour cet exercice, il est interdit d'utiliser l'opérateur ``**`` ou la
        fonction ``math.pow``.

    ..  note:: 

        Utilisez le fait que :math:`a^m = a^{2\cdot n} = (a^n)^2` pour :math:`m
        = 2n` pair.
    
    
    ~~~~

    def pow(a: float, n: int) -> float:
        '''
        >>> pow(0, 0)
        Traceback (most recent call last):
        ...
        ValueError: 0^0 is not mathematically well defined
        >>> pow(10, 1)
        10
        >>> pow(10, 0)
        1
        >>> pow(0, 9872943859287435982743857329845)
        0
        >>> pow(5, 2)
        25
        >>> pow(262, 22)
        159451426540433356807992796561830347140005150897209344
        '''
        ...

    try:
        import doctest
        doctest.testmod()
    except:
        print("Unable to run doctests")

    ====

    from unittest.gui import TestCaseGui

    tests = [
        ((10, 1), 10),
        ((10, 0), 1),
        ((0, 9872943859287435982743857329845), 0),
        ((5, 2), 25),
        ((262, 22), 159451426540433356807992796561830347140005150897209344),
    ]

    class myTests(TestCaseGui):

        def test_1(self):
            for args, expected in tests:
                result = pow(*args)
                feedback = f"Le résultat est OK pour args={args}"
                self.assertEqual(result, expected, feedback=feedback)

        # def test_raise_error(self):
        #     feedback = f"Exception levée correctement pour 0^0"
        #     self.assertRaises(ValueError, lambda: pow(0, 0), feedback)

    myTests().main()


..  reveal:: cf77760b-1432-4550-b29b-f535ce50c0dd
    :showtitle: Solution

    https://webtigerpython.ethz.ch/?code=NobwRAdghgtgpmAXGGUCWEB0AHAnmAGjABMoAXKJMAHQmLgDMACbAewHcAKKRJhgG1bkCTCLwxkAlEwC0APj6DyiWkzVMA5FtXq5elh04AGEUck61AFQBOUAMZwARvYDWTTjFYBnMk2twHCF87KH5-Jn4oH0kVCHV1TESLJgA1UIBXOABRa2tWa14jAD0jJjQvUVZfVDIACzgatBCw3CZ2ODCmegYMOGJkvQU2LgBGEyYR8zj1MYH9Yc4x0yn4kbmhw3GATgAOAHYAJi2AFgBmHYBWLYP9s6udg72zy73To53ji5X1I3WDLguIgO3zUBwufwWBwAbAcgcDkiMrp8RsdoRdjkYzqdThcoTsjHsttdCVDcSMdqcjKdjnsUUZ6RdEUYdltDkYttTjsktBpkmhmFAmABeIVMUpQOiiYWioyxeLxWzlOCpDLZXL5TjUMDFUrlSrVcj1RrNfitdqdbq9fpgEFlAXSsVy-VqfxkdLWOK_aZqflSkWO5IKuBuj0TZIdX1xACkTAODtlgfUAA9hf9uCI4gB6TOx21BkNxFMAKiYSfD_C8cCdztd7rigpLCygGdkEymtDI1lw1bKMDY1l8xFYdjIcB8ySHI7HZEwo58nmInCmcCTDmwZB7yWw1gkmrAAFVoI5-MqyKw_Ok4pO52QvFr2xBaGAAL4AXSAA
        

Exercice 7 (product)
====================

..  activecode:: list_product_rec.py

    Développez une fonction récursive ``product(items: list[T], n: int) -> list[list[T]]``
    qui retourne le produit (cartésien) de degré :math:`n` de la collection
    ``items`` avec elle-même.

    La fonction retourne une liste de listes. ``product(items=[1, 2], 3)``
    retourne par exemple la liste de toutes les listes de longueur 3 possibles
    contenant des éléments de la liste ``[1, 2]``.

    ..  note:: 

        Cette fonction pourrait être utilisée pour implémenter un algorithme de
        recherche exhaustive (force brute)

    ~~~~


    def product(items: list, n: int) -> list[list]:
        '''
        >>> product([1, 2,  3], 0)
        [[]]
        >>> product([1, 2, 3], 1)
        [[1], [2], [3]]
        >>> product([1, 2, 3], 2)
        [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
        >>> product([0, 1], 3)
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        '''
        if n == 1:        
            return [[i] for i in items]        
        else:
            res = product(items, n - 1)
            return [[i] + r for i in items for r in res]

            

    try:
        import doctest
        doctest.testmod()
    except:
        print("Unable to run doctests")

    ====

    from unittest.gui import TestCaseGui


    class myTests(TestCaseGui):

        def test_1(self):

            tests = (
                (([1, 2, 3], 0), [[]]),
                (([1, 2, 3], 1), [[1], [2], [3]]),
                (([1, 2, 3], 2), [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]),
                (([0, 1], 3), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]),
            )

            for args, expected in tests:
                items, n = args
                result = product(items, n)
                
                feedback = f"product(items={items}, n={n}) OK"
                self.assertEqual(result, expected, feedback)


    myTests().main()

        
..  reveal:: a855e53e-abf9-4b0b-9fc2-fa3d451d7b1f
    :showtitle: Solution

    ..  admonition:: Solution

        ..  code-block:: python

            def product(items: list, n: int):
                '''
                >>> product([1, 2,  3], 0)
                [[]]
                >>> product([1, 2, 3], 1)
                [[1], [2], [3]]
                >>> product([1, 2, 3], 2)
                [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
                >>> product([0, 1], 3)
                [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
                '''
                
                if n == 0:        
                    return [[]]        
                else:
                    res = product(items, n - 1)
                    return [[i] + r for i in items for r in res]

                    

            try:
                import doctest
                doctest.testmod()
            except:
                print("Unable to run doctests")

    => produit d'une liste avec elle-même plusieurs fois de suite

    https://webtigerpython.ethz.ch/?code=NobwRAdghgtgpmAXGGUCWEB0AHAnmAGjABMoAXKJMAHQmLgDMACbAJwHtiBXAYzIAo0ZODADOiJgBs0osgSYQJGMgEpEtJpqYByXRq0A-Iyw7c-_YAEZ5AJnkBmALryADCv2bgwR449MjBiacvAJWtg7OTJbuEFpMXpaRwDZJTr6xhsZsweZhTHZMTrYxcQnyifJ5KZXWhUkFFfEF1U0RlfblqbZddelxAUFmoS6dDiVaXiNMUy5JM6PxU7WzlUsLeTNJy-u1y1vlnX1autp-fmjMsQC8V9MScVp-caxwZFyssV4-D48ZmnCSURwdR_B4vURMW7ZIaCYRieSxAC0UXGPxebw-8WAaEcTAA1ExWEwGOwiWgmBgKXCISSiWTYuD0k9frQyKxcCC4mgYNhSWQmMR2Hw4LI_ILhbJMMJZDBOPwYnAAB48ODYMicrRsZT8ahgACq0AARpI4EwyOxCVxYuLpWRRLrUUwwABfRxAA

..
    idée : https://leetcode.com/problems/swap-nodes-in-pairs/description/
    idée 2 (hard) : https://leetcode.com/problems/number-of-digit-one/description/
    BST : https://leetcode.com/problems/all-possible-full-binary-trees/description/
    nombres : https://leetcode.com/problems/count-good-numbers/description/

..
    Exercice 9 (Structures récursives)
    ==================================

    Les structures récursives sont très courantes en informatique. Les structures
    récursives les plus fréquentes sont les **arbres**. Un arbre est un graphe
    dépourvu de cycle.

    ..  admonition:: Exemple 1

        L'arbre suivant représente une arborescence de dossiers dans un système
        Linux. Les noeuds de l'arbre représentent les dossiers et la racine ``/``
        représente le dossier racine du système

        ..  figure:: figures/exo-dot-filesystem.png
            :align: center
            :width: 100%

            Structure hiérarchique d'un système de fichiers Linux dont la racine
            (root) est représentée par le dossier ``/``.

        ..
            # http://www.graphviz.org/content/cluster

            digraph G {
            "/" -> "etc"
            "/" -> "home"
            "/" -> "lib"
            "/" -> "bin"
            "/" -> "usr"
            
            home -> guido
            home -> turing
            guido -> dev
            dev -> devpython
            dev -> dropbox
            
            lib -> python
            lib -> mysql
            
            turing -> machine
            turing -> test
            
            usr -> usr_bin
            usr -> usr_lib
            etc -> httpd
            etc -> "cron.d"
            etc -> "dconf"
            
            devpython -> src
            devpython -> tests
            
            usr_bin [label="bin"]
            usr_lib [label="lib"]
            devpython [label="python"]
            
            }

    ..  admonition:: Exemple 2

        On peut représenter l'expression arithmétique :math:`15 / ((3 + 5) \cdot 6)`
        par l'arbre syntaxique

        ..  figure:: figures/arithmetic-expr-tree.png
            :align: center
            :width: 50%

            Arbre syntaxique de l'expression :math:`15 / ((3 + 5) \cdot 6)`

        ..
            # http://www.graphviz.org/content/cluster

            digraph G {
                "/" -> 15
                "/" -> "*"
            "*" -> "+"
            "*" -> "6"
            "+" -> 3
            "+" -> 5
            }

    Un arbre peut être représenté par des **listes imbriquées**. Par exemple,
    l'arbre de l'exemple 2 peut être représenté par la structure imbriquée

    ..  activecode:: c116ea29-53c0-47fe-b5fa-5e479d5e5b24

        parse_tree = [
            "/",
            [15, [], []],
            [
                "*", 
                [
                    "+",
                    [3, [], []],
                    [5, [], []],
                ],
                [6, [], []]
            ]
        ]

    En effet, chaque noeud de l'arbre contient les informations suivantes

    - Une donnée (ici un opérateur ou un nombre)
    - Un sous-arbre gauche
    - Un sous-arbre droit

    ..  note::

        Le noeud au sommet de l'arbre s'appelle **racine** (l'arbre est retourné à
        l'envers par rapport à la nature) et les noeuds n'ayant pas de sous-arbre
        sont appelés **feuilles de l'arbre**. Les sous-arbres gauche et droit des
        feuilles sont représentés par des listes vides.

    Consigne
    --------

    Dans ce challenge, vous devez écrire une fonction ``to_prefix``