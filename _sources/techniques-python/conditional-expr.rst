.. _expressions-conditionnelles.rst:

Expressions conditionnelles
###########################

..  contents:: Contenu de la page
    :depth: 3

Syntaxe
=======

Une expression conditionnelle est composée de l'opérateur **ternaire** ``... if
... else ...``. On a donc la structure

::

    expr_si_vrai if expression else expr_si_faux

La sémantique est la suivante

- On évalue d'abord l'expression ``expression`` entre le ``if`` et le ``else``.
- Si l'expression en question est truthy (``bool(expression) == True``), on
  évalue l'expression ``expr_si_vrai``, dont la valeur devient la valeur de
  l'ensemble de l'expression conditionnelle.
- Si, au contraire, l'expression ``expression`` est falsy (``bool(expression) ==
  True``), on évalue l'expression ``expr_si_faux``, dont la valeur devient la
  valeur de l'ensemble de l'expression conditionnelle.

Exemple
=======

On veut créer une fonction ``welcome(name: str, sexe: str) -> str`` qui retourne
un message de bienvenue à la personne nommée ``name``, de sexe ``sexe``, en
faisant les accords corrects. On peut utiliser des **instructions
conditionnelles**, comme dans le programme ci-dessous:

..  activecode:: ce05a12d-9d62-4fc0-b0f6-123643c3089b

    def welcome(nom, sexe):
        if sexe == 'f':
            accord = 'se'
            cher = 'Chère'
        else:
            accord = 'x'
            cher = 'Cher'
        
        return f"{cher} {nom}, es-tu heureu{accord}?"
        
    print(welcome('Maxime', 'm'))
    print(welcome('Marie', 'f'))

ou raccourcir significativement le programme avec des **expressions
conditionnelles**, comme suit:

..  activecode:: 6b23d7e8-083f-4471-84d0-2760ff696d1c

    def welcome(nom, sexe):
        accord = 'se' if sexe == 'f' else 'x'
        cher = 'Chère' if sexe == 'f' else 'Cher'
        return f"{cher} {nom}, es-tu heureu{accord}?"
        
    print(welcome('Maxime', 'm'))
    print(welcome('Marie', 'f'))

.. note::

    La deuxième variante avec les expressions conditionnelles est plus concise
    et plus lisible. Si l'on veut rajouter un nouveau mot / accord dans le
    texte, il suffit de ne modifier qu'une seule ligne

Questions de compréhension
==========================

Question 1
----------

..  shortanswer:: prog-conditionnal-expression-comprehension-01

    Sans utiliser Python, déterminez ce qu'affiche le programme ci-dessous, puis
    vérifiez votre réponse dans Python. **Justifiez votre réponse**.

    ::

        y = 5
        x = "A" if y < 4 else "B" if y < 6 else "C"

..  shortanswer:: prog-conditionnal-expression-comprehension-02

    Sans utiliser Python, déterminez ce qu'affiche le programme ci-dessous, puis
    vérifiez votre réponse dans Python. **Justifiez votre réponse**.

    ::

        y = 2
        x = "A" if y < 4 else "B" if y < 6 else "C"

..  shortanswer:: prog-conditionnal-expression-comprehension-03

    Sans utiliser Python, déterminez ce qu'affiche le programme ci-dessous, puis
    vérifiez votre réponse dans Python. **Justifiez votre réponse**.

    ::

        y = 8
        x = "A" if y < 4 else "B" if y < 6 else "C"

Exercices
=========

Exercice 1
----------

..  activecode:: prog-conditionnal-expression-abs
    :language: webtp

    Complétez le code de la fonction ``abs(x)`` ci-dessous pour qu'elle retourne la
    valeur absolue de ``x``. 

    ..  note:: 

        Limitez le corps de la fonction ``abs`` à une seule ligne de code en
        utilisant une expression conditionnelle.

    ~~~~

    def abs(x: float) -> float:
        '''
        Returns the absolute value of `x` using a conditional expression.

        >>> abs(10)
        10
        >>> abs(-10)
        10
        >>> abs(0)
        0
        >>> abs("salut")
        '''
        ...

    try:    
        import doctest
        doctest.testmod()
    except:
        print("Impossible de lancer les doctests")


..  reveal:: e6028bdd-d324-4402-8668-177e01fa414d
    :showtitle: Solution
    :modal:
    :modaltitle: Solution
    :instructoronly:

    ..  code-block:: python

        def abs(x: float) -> float:
            '''
            Returns the absolute value of `x` using a conditional expression.

            >>> abs(10)
            10
            >>> abs(-10)
            10
            >>> abs(0)
            0
            '''
            return x if x >= 0 else -x

    ..
        def abs(x: float) -> float:
            '''
            Returns the absolute value of `x` using a conditional expression.

            >>> abs(10)
            10
            >>> abs(-10)
            10
            >>> abs(0)
            0
            >>> abs("salut")
            Traceback (most recent call last):
            ...
            TypeError: x must be a number
            '''
            try:
                return x if x >= 0 else -x
            except TypeError:
                raise TypeError("x must be a number")

Exercice 2
----------

..  activecode:: prog-conditionnal-expression-plural
    :language: webtp

    Complétez le code de la fonction ``plural(word: str, n: int) -> str``
    ci-dessous. Elle doit retourner le mot ``word`` au singuler si ``n`` indique
    un nombre singulier et retourner le mot ``word`` accordé au pluriel si ``n``
    indique un nombre pluriel.

    ..  note:: 

        Limitez le corps de la fonction ``plural`` à une seule ligne de code en
        utilisant une expression conditionnelle.

    ~~~~

    def plural(word: str, n: int) -> str
        ''' 
        
        Returns the plural or singular of ``word`` (depending on the value of
        ``n``) assuming ``word`` is an english word that has a plural in ...s
        (for instance apple => apples).

        >>> plural("apple", 0)
        "apple"
        >>> plural("apple", 1)
        "apple"
        >>> plural("apple", 2)
        "apples"
        >>> plural("apple", 1000)
        "apples"
        >>> plural("cat", 0)
        "cat"
        >>> plural("cat", 1)
        "cat"
        >>> plural("cat", 100)
        "cats"
        '''
        ...

    try:    
        import doctest
        doctest.testmod()
    except:
        print("Impossible de lancer les doctests")


..  reveal:: d0a77709-4c8d-49a9-9dc9-d1aee6700574
    :showtitle: Solution
    :modal:
    :modaltitle: Solution
    :instructoronly:

    ..  code-block:: python

        def plural(word: str, n: int) -> str:
            '''

            Returns the plural or singular of ``word`` (depending on the value
            of ``n``) assuming ``word`` is an english word that has a plural in
            ...s (for instance apple => apples).

            >>> plural("apple", 0)
            'apple'
            >>> plural('apple', 1)
            'apple'
            >>> plural('apple', 2)
            'apples'
            >>> plural('apple', 1000)
            'apples'
            >>> plural('cat', 0)
            'cat'
            >>> plural('cat', 1)
            'cat'
            >>> plural('cat', 100)
            'cats'
            '''
            return f"{word}{'' if n <= 1 else 's'}"