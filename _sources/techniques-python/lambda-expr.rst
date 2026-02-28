.. _expressions-lambda.rst:

Expressions lambda
##################

..  contents:: Contenu de la page
    :depth: 3

Les expressions lambda sont des expressions dont la valeur produite est une
fonction. Autrement dit, les expressions lambda sont une autre manière de
produire des fonctions que le ``def``. On utilise les expressions lambda en
programmation fonctionnelle, pour définir des fonctions simples, qu'il est
possible de définir seule une seule ligne.

..  note::

    On parle d'expression ``lambda`` en référence au :math:`\lambda`-calcul,
    formalisme développée dans les années 1930 Alonzo Church. Il constitue un
    des fondements de la théorie de la calculabilité et permet de répondre à des
    questions fondamentales en mathématiques et logique. 

    Pour plus d'information : https://fr.wikipedia.org/wiki/Lambda-calcul#:~:text=Le%20lambda%2Dcalcul%20(ou%20%CE%BB,une%20%CE%BB%2Dexpression%2C%20%CE%BBx.

Syntaxe
=======

..  admonition:: Syntaxe

    ::

        lambda <liste de paramètres>: <expression-utilisant-les-paramètres>

Exemple
=======

L'expression suivante définit la **fonction anonyme** :math:`x \mapsto x^2 + 1`

::

    lambda x: x ** 2 + 1

On peut ensuite utiliser cette expression dans une expression qui appelle la
fonction anonyme

..  activecode:: e324e6da-1467-400b-a628-1d2da265da34

    y = (lambda x: x ** 2 + 1)(4)
    print(y)


Exemple d'utilisation expressions lambda
========================================

Supposons que l'on veuille filtrer les éléments d'une liste de nombres, en ne
gardant par exemple que les éléments qui sont pairs.

On pourrait définir cela de la manière suivante

..  activecode:: 3a7230ba-3506-4a6d-aaef-c19cf136df12

    def filter_even(numbers: list[float]) -> list[float]:
        result = []

        for n in numbers:
            if n % 2 == 0:
                result.append(n)

        return result

    print(filter_even([5, 4, 7, 6, 9, 8]))

Maintenant, si on veut ensuite définir une fonction analogue qui prend en
paramètre une liste de chaînes de caractères et qui retourne une liste ne
comprenant que ceux dont la longueur est inférieure à 5, on définirait cette
fonction comme suit:

..  activecode:: e8a6d366-2ca9-436a-bc06-002a6781e495

    def filter_short_words(words: list[str]) -> list[str]:
        result = []

        for w in words:
            if len(w) < 5:
                result.append(w)

        return result

    print(filter_short_words(["maison", "omelette", "pain", "bananes"]))

On peut constater que les fonctions ``filter_even`` et ``filter_short_words``
font pratiquement la même chose : elles prennent une liste d'éléments et créent
une nouvelle liste ne contenant que les éléments de la liste originale
satisfaisant à une certaine condition. Au lieu de redéfinir une fonction presque
identique à chaque fois, il suffirait de définir une fonction générique
``filter(items: list, condition) -> list`` qui prend une liste ``items`` et une
condition ``condition`` à appliquer aux éléments. Cela est réalisable comme
suit, en considérant le paramètre ``condition`` comme **une fonction** qui prend
un élément de la liste en paramètre et retourne ``True`` s'il faut le conserver
et ``False`` sinon:

..  activecode:: 364a1604-746d-49e0-86d4-8de95297dbf9
    :language: webtp

    from collections.abc import Callable

    def filter[T](items: list[T], condition: Callable[[T], bool]) -> list[T]:
        result: list[T] = []

        for item in items:
            if condition(item):
                result.append(item)

        return result

    print(filter([5, 4, 7, 6, 9, 8], lambda x: x % 2 == 0))
    print(filter(["maison", "omelette", "pain", "bananes"], lambda x: len(x) < 5))

..  admonition:: Remarques sur les annotations de type

    Les annotations de type de la fonction filter présentent quelques nouveautés

    - ``filter[T]`` indiquent qu'on utilise le type générique ``T``. Les types
      génériques permettent par exemple de traiter les cas suivants de manière
      générique:

      - La fonction ``filter`` prend en paramètre une liste de ``int`` (noté
        ``list[int]``), auquel cas le type ``T`` devient ``int``

      - La fonction ``filter`` prend en paramètre une liste de ``str`` (noté
        ``list[str]``), auquel cas, le type ``T`` devient ``str``

      - etc.

    - ``Callable[[T], bool]`` signifie que le paramètre ``condition`` doit être
      un appelable (*callable* en anglais), donc par exemple une fonction, qui
      prend un seul paramètre de type ``T`` et qui retourne un booléen.

    - Le module ``collections`` contient de nombreuses collections utiles en
      Python et le module ``collections.abc`` contient les classes abstraites de
      base pour ces collections (**ABC = Abstract Base Class**).

Exercices
=========

Exercice 1
----------

Complétez les lignes avec une élipse ``...`` avec un appel à la fonction
``filter`` et une expression lambda appropriée.

..  activecode:: filter_exercise_lambda
    :language: webtp

    from collections.abc import Callable

    def filter[T](items: list[T], condition: Callable[[T], bool]) -> list[T]:
        result: list[T] = []

        for item in items:
            if condition(item):
                result.append(item)

        return result

    nicknames = ['einstein284', 'fido', 'compteharbour', 'superman12', 'pic$ou23', 'pic$sou']

    # pseudos dont le nombre de lettre est pair
    # => ['fido', 'superman12', 'pic$ou23']
    nicknames_even_chars = ...    

    # pseudos ne contenant pas de chiffre
    # => ['fido', 'compteharbour', 'pic$sou']
    nicknames_without_digit = ...

..  reveal:: de0dc283-e260-4fd2-899e-a0514206c58c
    :showtitle: Solution

    ::

        # pseudos dont le nombre de lettre est pair
        nicknames_even_chars = filter(nicknames, lambda nn: len(nn) % 2 == 0)
        print(nicknames_even_chars) # devrait afficher ['fido', 'superman12']

        # pseudos ne contenant pas de chiffre
        nicknames_without_digit = filter(nicknames, lambda nn: not any(c.isdigit() for c in nn))
        print(nicknames_without_digit) # devrait afficher ['fido', 'compteharbour']
