.. _variables.rst:

Variables de décision
#####################

..  contents:: Contenu de la page
    :depth: 3

En programmation par contraintes, les variables ont un statut différent de celui
en Python. Elles ne servent pas uniquement à stocker des données. En PPC, elles
sont beaucoup plus puissantes.

Domaine
=======

En PPC, chaque variable :math:`X_i` est caractérisée par un **domaine**
:math:`D_i` de valeurs possibles et est reliée à d'autres variables du problème
par des contraintes.

Exemple pour le problème des n dames
------------------------------------

Dans le problème des n dames, le domaine des variables est l'ensemble des
numéros de ligne possible pour une dame données. On a donc, dans le problème des
n dames, :math:`D_i = \left{0; 1; 2; \ldots; n-1 \right}` pour :math:`0 \leq  i
< n`

Implémentation
--------------

Définissez une classe ``Domain`` permettant de représenter le domaine d'une
variable entière.

..  note::
    
    Nous n'utiliserons que des variables entières dans ce cours

..  activecode:: toycsp_domain_v1
    :language: webtp

    from typing import Set

    class Domain:
        """
        Implementation of a very basic domain
        using a set to store the values

        >>> d = Domain(4)
        >>> type(d.values)
        
        >>> d.values
        {0, 1, 2, 3}

        """

        def __init__(self, *args) -> None:
            """
            Initializes a domain with {0, ... ,n-1} using Python sets
            as underlying datastructure (not efficient at all but simple
            as a first step)

            Args:
                n: The number of values in the domain.
            """
            ...

..              
            if len(args) != 1:
                raise TypeError("Domain takes only one parameter")
            elif isinstance(args[0], int):
                n = args[0]
                self.values = set(range(n))
            elif isinstance(args[0], set):
                dom = args[0]
                self.values = dom.copy()
            else:
                raise TypeError("Argument must be int or Domain")

    

Variables
=========

Définissez une classe ``Variable`` qui servira à représenter les variables de
décision d'un problème de satisfaction de contraintes.

..  activecode:: def_variables_py
    :language: webtp

