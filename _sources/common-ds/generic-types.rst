.. _generic-types.rst:

Types génériques
################

..  contents:: Contenu de la page
    :depth: 3

Avant de passer à la définition de types abstraits, il est nécessaire de
considérer la notion de **type générique**. 

Présentation en vidéo
=====================

..  youtube:: TkDg3EHwC1g
    :divid: arjancodes-generic-types
    :width: 640
    :height: 360

Le problème
===========

Supposons qu'on veuille définir une fonction pour retourner tous les éléments
d'une liste situés aux positions impaires. On pourrait utiliser la fonction

..  code-block:: python
    :linenos:

    def get_odd_items(items):
        return [item for i, item in enumerate(items) if i % 2 == 1]

Si on veut rajouter des annotations de type pour consolider le code et pour
bénéficier de l'aide intégré d'IDE tels que VSCode, on ne pourrait pas utiliser
simplement la syntaxe suivante:

..  code-block:: python
    :linenos:

    def get_odd_items(items: list) -> list:
        return [item for i, item in enumerate(items) if i % 2 == 1]

    list1 = [1, 2, 3, 4, 5]
    list2 = ["a", "b", "c", "d"]

    print(get_odd_items(list1))
    print(get_odd_items(list2))

Le problème est qu'on ne sait pas le type des éléments contenus dans la liste.
On pourrait évidemment écrire par exemple 

..  code-block:: python
    :linenos:

    def get_odd_items(items: list[float]) -> list[float]:
        return [item for i, item in enumerate(items) if i % 2 == 1]

    list1 = [1, 2, 3, 4, 5]
    list2 = ["a", "b", "c", "d"]
    
    print(get_odd_items(list1))
    print(get_odd_items(list2))  # => pose problème pour le typechecking

mais la fonction ne pourrait ensuite plus être utilisée correctement pour des
listes contenant autre chose que des nombres.

Typage générique des fonctions
==============================

Pour résoudre ce problème, on utilise des **types génériques**, qui est une
sorte de "paramétrisation des types". On voudrait pouvoir écrire quelque chose
comme 

..  code-block:: python
    :linenos:

    def get_odd_items(items: list[T]) -> list[T]:
        return [item for i, item in enumerate(items) if i % 2 == 1]

où ``T`` est une sorte de "variable de type". Ce concept s'appelle **type
générique**. L'avantage est qu'on encode l'information que le type des éléments
de la liste retournée par la fonction est le même que les types des éléments de
la liste reçue en paramètre, ce qui permet de renforcer la vérification des
types.


Il y a deux syntaxes en Python pour exprimer cela.

Ancienne syntaxe
----------------

..  activecode:: a1697719-44f5-4e56-93c4-95cf878d43cd
    :language: webtp

    from typing import TypeVar

    T = TypeVar("T")

    def get_odd_items(items: list[T]) -> list[T]:
        return [item for i, item in enumerate(items) if i % 2 == 1]

    list1: list[int] = [1, 2, 3, 4, 5]
    list2: list[str] = ["a", "b", "c", "d"]
    
    print(get_odd_items(list1))  # => OK, car T peut être n'importe quel type
    print(get_odd_items(list2))  # => OK, car T peut être n'importe quel type


Nouvelle syntaxe (Python :math:`\geq` 3.12)
-------------------------------------------

La nouvelle syntaxe disponble dès Python 3.12 est bien plus concise et pratique.

..  activecode:: 44dd3f44-cd1e-4f4e-9255-e304f379ff47
    :language: webtp

    def get_odd_items[T](items: list[T]) -> list[T]:
        return [item for i, item in enumerate(items) if i % 2 == 1]

    list1: list[int] = [1, 2, 3, 4, 5]
    list2: list[str] = ["a", "b", "c", "d"]
    
    print(get_odd_items(list1))  # => OK, car T peut être n'importe quel type
    print(get_odd_items(list2))  # => OK, car T peut être n'importe quel type

Typage générique des classes
============================

Ancienne syntaxe
----------------

..  activecode:: 10103900-f9bf-47d7-96c6-1b5a1ce65b17
    :language: webtp

    from typing import TypeVar, Generic

    T = TypeVar("T")

    class Container(Generic[T]):

        def __init__(self, items: list[T]):
            self._items: list[T] = items

        def get_items(self) -> list[T]:
            return self._items

    # c1 contient ne contient que des entiers
    c1 = Container([1, 2, 3, 4])
    print(c1.get_items())

    c2 = Container(["Nina", "Jonathan"])
    print(c2.get_items())

Nouvelle syntaxe (Python :math:`\geq` 3.12)
-------------------------------------------

La nouvelle syntaxe disponble dès Python 3.12 est bien plus concise et pratique.

..  activecode:: 8f1db48c-0bf4-4360-9d0e-e89092407abb
    :language: webtp

    class Container[T]:

        def __init__(self, items: list[T]) -> None:
            self._items: list[T] = items

        def get_items(self) -> list[T]:
            return self._items

    # c1 contient ne contient que des entiers
    c1 = Container([1, 2, 3, 4])
    print(c1.get_items())

    c2 = Container(["Nina", "Jonathan"])
    print(c2.get_items())


Références
==========

- Types génériques dans la documentation du vérificateur de types MyPy :
  https://mypy.readthedocs.io/en/stable/generics.html, consulté le 12 novembre
  2024

- Billet de blog de "Arjan Codes" :
  https://www.arjancodes.com/blog/python-generics-syntax/, consulté le 12
  novembre 2024