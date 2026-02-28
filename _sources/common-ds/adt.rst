.. _ds/adt.rst:

Notion de type abstrait
#######################

..  contents:: Contenu de la page
    :depth: 3

Définition
==========

Un type abstrait est une spécification abstraite (mathématique) de
fonctionnalités qu'un type de données doit mettre à disposition et de propriétés
qu'il doit avoir.

Lorsqu'on définit un type abstrait, on ne se préoccupe pas des détails
d'implémentation, mais on spécifie l'**interface** que doit avoir ce type de
données.

En Python, on peut définir un type abstrait à l'aide d'une **classe abstraite**
ou d'un **protocole**. Nous utiliserons les classes abstraites de base (*ABC* =
Abstract Base Class) pour définir les types abstraits utilisés dans notre
solveur.

Une classe abstraite est une classe qu'**on ne peut pas instancier
directement**, dont il faut **implémenter (surcharger) les fonctionnalités
(méthodes) dans une classe dérivée concrète**. À ce titre, **la classe abstraite
de base agit comme un contrat** puisque toutes les méthodes abstraites doivent
être surchargées dans les classes dérivées pour pouvoir être considérées comme
des classes concrètes qu'il est possible d'instancier.

Classe abstraite en Python
==========================

..  admonition:: Remarque

    La notion de classe abstraite aurait pu être présentée dans le cadre du
    chapitre de POO, tant cette notion est importante en POO.

En Python, une classe abstraite se définit en la dérivant de la classe ``ABC``
(=Abstract Base Class) et en utilisant le décorateur ``@abstractmethod`` pour
déclarer les méthodes abstraites (qui doivent être implémentées dans les classes
dérivées).

..  activecode:: c8bbf3ae-419c-4b44-b0c1-0663fdfdc1f6
    :language: webtp

    from abc import ABC, abstractmethod

    class MyAbstractClass(ABC):

        @abstractmethod
        def a_method_to_be_implemented_in_conrete_classes(self):
            pass

Les classes abstraites sont faites pour être dérivées, de sorte que les méthodes
soient concrétisées (implémentées) dans les classes dérivées, pour en faire des
types concrets instanciables.

Prococoles
==========

Nous utiliserons parfois aussi la notion de protocole pour définir l'interface
d'une classe. Dans le code ci-dessous, les classes ``State``, ``StateEntry``,
``Storage`` sont toutes des **protocoles**. En Python, un protocole correspond
en gros à la notion d'interface en Java : ils permettent de spécifier la
structure que doit posséder une classe (ses méthodes, attributs, ...). Toute
classe qui implémente un protocole doit fournir une implémentation pour les
méthodes non implémentées dans le protocole.

..  admonition:: Exemple : protocole ``Storage``

    Le protocole ``Storage`` spécifie que toute classe qui implémente le
    protocole ``Storage``  doit implémenter une méthode ``save`` ne prenant
    aucun paramètre (autre que ``self``) et retournant un ``StateEntry``.

..  activecode:: 21c53d62-d5a8-4a88-b3a9-d621e42aac7e
    :language: webtp

    class State[T](Protocol):

        def set_value(self, v: T) -> T: ...

        def value(self) -> T: ...

        def __str__(self) -> str: ...


    class StateEntry(Protocol):

        def restore(self) -> None: ...


    class Storage(Protocol):

        def save(self) -> StateEntry: ...


    class StateInt(State[int]):

        def increment(self) -> int:
            return self.set_value(self.value() + 1)

        def decrement(self) -> int:
            return self.set_value(self.value() - 1)


    class Copy[T](Storage, State[T]):

        class CopyStateEntry[T](StateEntry):
        
            def __init__(self, parent: "Copy") -> None:
                self._parent = parent
                self._v = parent._v
        
            def restore(self) -> None:
                self._parent._v = self._v
        
            def __repr__(self) -> str:
                return f"{self.__class__.__name__}({self._v})"

        def __init__(self, init_value: T) -> None:
            self._v = init_value

        def set_value(self, value: T) -> T:
            self._v = value
            return value

        def value(self):
            return self._v

        def save(self) -> StateEntry:
            return self.CopyStateEntry(self)

        def __repr__(self) -> str:
            return f"{self.__class


..  admonition:: Références

    - https://towardsdatascience.com/a-complete-guide-to-stacks-in-python-ee4e2045a704
    - https://medium.com/@tssovi/abstract-data-type-adt-in-python-33e6ce1f961e
    - https://object-oriented-python.github.io/5_abstract_data_types.html
    - https://info.blaisepascal.fr/nsi-pile-file#File