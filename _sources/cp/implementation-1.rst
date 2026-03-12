.. _implementation-1.rst:

Implémentation (étape 1)
########################

..  contents:: Contenu de la page
    :depth: 3

Dans cette première étape, nous allons implémenter une version très basique des
domaines, des variables et de la contrainte ``NotEqual``. Ces contraintes seront
suffisantes pour résoudre des problème simples tels que les :math:`n` dames ou
des Sudokus.

Implémentation des domaines
===========================

..  activecode:: toycsp_impl_domain
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    Définissez une classe ``Domain`` qui permet de représenter le domaine de
    variables entières.

    ..  admonition:: Consignes
        :class: note

        On doit pouvoir instantier un domaine de deux manières : 
        
        -   En fournissant un nombre entier ``n``. Dans ce cas, le domaine
            contiendra les valeurs ``{0, 1, 2, ..., n-1}``

        -   En fournissant un ensemble (``set``). Dans ce cas, le domaine
            contiendra les mêmes valeurs que l'ensemble en question.

        La classe doit posséder les méthodes suivantes

        -   ``is_fixed(self) -> bool`` : retourne ``True`` si le domaine est
            fixé, à savoir s'il se réduit à une seule valeur et ``False`` sinon.
        -   ``size(self) -> int`` : retourne le nombre d'éléments présents dans
            le domaine.
        -   ``__len__(self) -> int``: idem que ``size``
        -   ``__repr__(self) -> str`` : retourne la représentation du domaine
            sous la forme ``Domain({v1, v2, ..., vn})``.

        -   ``min(self) -> int`` : retourne la valeur minimale du domaine
        -   ``remove(self, v: int) -> bool`` : supprime la valeur ``v`` du
            domaine. Retourne ``True`` si la valeur se trouvait dans le domaine
            avant d'être supprimée et ``False`` si la valeur n'était pas
            présente dans le domaine. Lève l'exception ``Inconsistency`` si le
            domaine est vide après la suppression de la valeur ``v``.
        -   ``fix(self, v: int)`` : réduit le domaine à a seule valeur ``v``.
        -   ``clone(self) -> "Domain"`` : crée une copie du domaine en
            retournant **une nouvelle instance** de ``Domain`` avec les mêmes
            valeurs.

    ~~~~

    class Domain:
        """ 
        
        Implementation of a very basic domain using a set to store the values

        >>> d = Domain(5)
        >>> d.values
        {0, 1, 2, 3, 4}
        >>> d.min()
        0
        >>> d.size()
        5
        >>> len(d)
        5
        >>> d.is_fixed()
        False
        >>> d.fix(v=6)
        Traceback (most recent call last):
        ...
        Inconsistency
        >>> d.fix(v=4)
        >>> d.values
        {4}
        >>> d.is_fixed()
        True
        >>> d1 = d.clone()
        >>> d1 is d
        False

        >>> d = Domain({1, 3})
        >>> d.values
        {1, 3}
        >>> d.remove(v=3)
        True
        >>> d
        Domain({1})
        >>> d.remove(v=3)
        False
        >>> d.remove(1)
        Traceback (most recent call last):
        ...
        Inconsistency

        """

        ...


..  reveal:: 3230694d-d66c-4dcc-bbf4-65b29790ab56
    :showtitle: Solution
    :hidetitle: Cacher
    :modal:
    :instructoronly:

    ..  activecode:: 5994b380-062a-4d64-9b63-90b8b5a5ce83
        :language: webtp
        :interpreterargs: branch=branch&layout=["Editor", "Console"]

        from typing import Any

        class Inconsistency(Exception): ...

        class Domain:
            """ 
            
            Implementation of a very basic domain using a set to store the values

            >>> d = Domain(5)
            >>> d.values
            {0, 1, 2, 3, 4}
            >>> d.min()
            0
            >>> d.size()
            5
            >>> len(d)
            5
            >>> d.is_fixed()
            False
            >>> d.fix(v=6)
            Traceback (most recent call last):
            ...
            Inconsistency
            >>> d.fix(v=4)
            >>> d.values
            {4}
            >>> d.is_fixed()
            True
            >>> d1 = d.clone()
            >>> d1 is d
            False

            >>> d = Domain({1, 3})
            >>> d.values
            {1, 3}
            >>> d.remove(v=3)
            True
            >>> d
            Domain({1})
            >>> d.remove(v=3)
            False
            >>> d.remove(1)
            Traceback (most recent call last):
            ...
            Inconsistency

            """

            def __init__(self, *args: tuple[Any, ...]) -> None:
                """
                Initializes a domain. Values are stored as a set.

                - Domain(n) Initializes the domain with {0, 1, 2, ... n-1}
                - Domain(set) Initializes the domaine with the given set

                """
                if len(args) != 1:
                    raise TypeError("Domain takes only one parameter")
                elif isinstance(args[0], int):
                    n = args[0]
                    self.values = set(range(n))
                elif isinstance(args[0], set):
                    dom = args[0]
                    self.values = dom.copy()
                else:
                    raise TypeError("Argument must be int or set[int]")

            def is_fixed(self) -> bool:
                """
                Verifies if only one value left

                Returns:
                    True if only one value left, False otherwise.
                """
                return len(self.values) == 1

            def size(self) -> int:
                """
                Gets the domain size

                Returns:
                    The number of values in the domain.
                """
                return len(self.values)
            
            def __len__(self) -> int:
                """
                Same as .size()
                """
                return self.size()

            def min(self) -> int:
                """
                Gets the minimum of the domain

                Returns:
                    The minimum value in the domain.
                """
                return min(self.values)

            def remove(self, v: int) -> bool:
                """
                Removes value v from the domain

                Args:
                    v: The value to remove.

                Returns:
                    True if the value was present in the domain, False otherwise.
                """
                if v in self.values:
                    self.values.remove(v)
                    if not self.values:
                        raise Inconsistency
                    return True
                return False

            def fix(self, v: int):
                """
                Fixes the domain to value v

                Args:
                    v: The value to fix the domain to.

                Raises:
                    Inconsistency: If the value is not in the domain.
                """
                if v not in self.values:
                    raise Inconsistency
                self.values = {v}

            def clone(self) -> "Domain":
                """
                Creates a copy of the domain.

                Returns:
                    A new Domain object with the same values.
                """
                return Domain(self.values)

            def __repr__(self) -> str:
                return f"Domain({self.values})"


        if __name__ == '__main__':
            import doctest
            doctest.testmod()


Implémentation des variables de décision
========================================

..  activecode:: toycsp_impl_vars
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    Définissez une classe ``Variable`` qui permet de représenter les variables
    de décision entière.

    ..  admonition:: Consignes
        :class: note

        On doit pouvoir instantier une variable en passant en paramètre les
        valeurs à insérer initialement dans son domaine sous la forme d'un
        itérable (liste, tuple, range, set, ...). On veut également pouvoir
        indiquer le nom de la variable avec le paramètre nommé ``name=``. Si le
        nom n'est pas donné, il sera créé automatiquement en se basant sur le
        compteur de création de variable (variables de classe) incrémenté lors
        de chaque instanciation.

    ::

        >>> q1 = Variable([3, 5, 7], name="Q1")
        >>> x = Variable(range(5, 8))

    La classe doit posséder les méthodes suivantes en plus du constructeur

    -   ``__repr__(self) -> str`` : 

    ..
        ############### Importation dans WebTigerPython ############
        from pyodide.http import open_url
        url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
        with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
        ############################################################

    ~~~~

    # Coller votre code de la classe Domain ici

    class Variable:
        '''
        >>> v = Variable({3, 4, 5})
        >>> v
        Variable(dom={3, 4, 5}, name='Var0')
        >>> v.dom
        Domain({3, 4, 5)
        >>> v2 = Variable(range(6, 9), name="Q2")
        Variable(dom={6, 7, 8}, name='Q2')
        
        '''

        ...


    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: 8a135924-181b-416f-910f-229b7f1bd98c
    :showtitle: Solution
    :hidetitle: Cacher
    :modal:
    :instructoronly:

    ..  code-block:: python

        from collections.abc import Iterable
        from domain import Domain

        class Variable:

            '''
            >>> v = Variable({3, 4, 5})
            >>> v
            Variable(dom={3, 4, 5}, name='Var0')
            >>> v.dom
            Domain({3, 4, 5)
            >>> v2 = Variable(range(6, 9), name="Q2")
            >>> v2
            Variable(dom={6, 7, 8}, name='Q2')
            
            '''

            var_counter = 0
            
            def __init__(self, dom: Iterable[int], name: str = None) -> None:
                self.dom = Domain(set(dom))
                self.name = name or 'Var' + str(Variable.var_counter)
                Variable.var_counter += 1
                
            def __repr__(self) -> str:
                return f"Variable(dom={self.dom.values}, name='{self.name}')"

        if __name__ == '__main__':
            import doctest
            doctest.testmod()

Implémentation de la contrainte ``NotEqual``
============================================

En PPC, l'intérêt des contraintes n'est pas seulement de formuler le problème
dans la phase de modélisation, mais également de constituer des outils de
raisonnement par le biais d'**algorithmes de filtrage** spécifique à chaque
contrainte. Un algorithme de filtrage permet de supprimer des domaines des
variables impliquées dans la contrainte les valeurs impossibles.

En d'autres termes, chaque contrainte :math:`c \in C` s'accompagne d'un
algorithme de filtrage :math:`\mathcal{F}_c` qui prend en entrée les domaines
des variables sur lesquelles porte la contrainte et qui élimine des domaines
certaines valeurs incohérentes, à savoir incompatibles avec les valeurs
présentes dans les autres domaines.

..  activecode:: toycsp_impl_notequal
    :language: webtp
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    Définissez une classe ``NotEqual(x, y)`` qui permet de représenter une
    contrainte de non égalité entre les variables :math:`x` et :math:`y`, à
    savoir :math:`x \neq y`. Le constructeur prend aussi un troisième paramètre
    ``offset`` qui permet de spécifier la contrainte :math:`x \neq y +
    \text{offset}`.

    ..  admonition:: Consignes
        :class: note

        La classe doit contenir encore les méthodes suivantes:

        -   ``propagate(self) -> bool`` : effectue la propagation (filtrage) sur
            les domaines des variables impliquées dans la contrainte. La
            contrainte peut effectuer une propagation dès que l'une des
            variables est fixée (n'a plus qu'une seule valeur dans son domaine).

        -   ``__repr__(self) -> str`` : retourne la représentation de la
            contrainte sous la forme ``NotEqual(x=Variable(...),
            y=Variable(...), offset=...)``.


    ~~~~

    ############### Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    ############################################################

    from toycsp import Domain, Variable

    class NotEqual:
        """
        Constraint representing x != y + offset.

        >>> x = Variable(range(5, 10))
        >>> y = Variable(range(3, 8))
        >>> x
        Variable(dom={5, 6, 7, 8, 9}, name='Var0')
        >>> y
        Variable(dom={3, 4, 5, 6, 7}, name='Var1')
        >>> c1 = NotEqual(x, y)     # x != y
        >>> c2 = NotEqual(x, y, 2)  # x != y + 2
        >>> c3 = NotEqual(x, y, -1) # x != y - 1
        >>> c1
        NotEqual(x=Variable(dom={5, 6, 7, 8, 9}, name='Var0'), y=Variable(dom={3, 4, 5, 6, 7}, name='Var1'), offset=0)
        >>> c1.propagate()
        False
        >>> x
        Variable(dom={5, 6, 7, 8, 9}, name='Var0')
        >>> y
        Variable(dom={3, 4, 5, 6, 7}, name='Var1')
        >>> x.dom.fix(6)
        >>> c1.propagate()
        True
        >>> x
        Variable(dom={6}, name='Var0')
        >>> y
        Variable(dom={3, 4, 5, 7}, name='Var1')
        >>> c2.propagate()
        True
        >>> x
        Variable(dom={6}, name='Var0')
        >>> y
        Variable(dom={3, 5, 7}, name='Var1')
        >>> c3.propagate()
        True
        >>> x
        Variable(dom={6}, name='Var0')
        >>> y
        Variable(dom={3, 5}, name='Var1')

        """

        ...


..  reveal:: 6f490d63-d9d5-4bb7-b844-bff400627d42
    :showtitle: Solution
    :hidetitle: Cacher
    :modal:
    :instructoronly:

    ..  code-block:: python
            
        class NotEqual():
            """
            Constraint representing x != y + offset.

            >>> x = Variable(range(5, 10))
            >>> y = Variable(range(3, 8))
            >>> x
            Variable(dom={5, 6, 7, 8, 9}, name='Var0')
            >>> y
            Variable(dom={3, 4, 5, 6, 7}, name='Var1')
            >>> c1 = NotEqual(x, y)     # x != y
            >>> c2 = NotEqual(x, y, 2)  # x != y + 2
            >>> c3 = NotEqual(x, y, -1) # x != y - 1
            >>> c1
            NotEqual(x=Variable(dom={5, 6, 7, 8, 9}, name='Var0'), y=Variable(dom={3, 4, 5, 6, 7}, name='Var1'), offset=0)
            >>> c1.propagate()
            False
            >>> x
            Variable(dom={5, 6, 7, 8, 9}, name='Var0')
            >>> y
            Variable(dom={3, 4, 5, 6, 7}, name='Var1')
            >>> x.dom.fix(6)
            >>> c1.propagate()
            True
            >>> x
            Variable(dom={6}, name='Var0')
            >>> y
            Variable(dom={3, 4, 5, 7}, name='Var1')
            >>> c2.propagate()
            True
            >>> x
            Variable(dom={6}, name='Var0')
            >>> y
            Variable(dom={3, 5, 7}, name='Var1')
            >>> c3.propagate()
            True
            >>> x
            Variable(dom={6}, name='Var0')
            >>> y
            Variable(dom={3, 5}, name='Var1')

            """

            def __init__(self, x: Variable, y: Variable, offset: int = 0) -> None:
                """
                Initializes the NotEqual constraint.

                Args:
                    x: The first variable.
                    y: The second variable.
                    offset: The offset value. Defaults to 0.
                """
                self.x = x
                self.y = y
                self.offset = offset

            def propagate(self) -> bool:
                """
                Propagates the NotEqual constraint.

                Returns:
                    True if any value was removed from a domain, False otherwise.
                """
                if self.x.dom.is_fixed():
                    return self.y.dom.remove(self.x.dom.min() - self.offset)
                elif self.y.dom.is_fixed():
                    return self.x.dom.remove(self.y.dom.min() + self.offset)
                return False

            def __repr__(self) -> str:
                return f'NotEqual(x={self.x}, y={self.y}, offset={self.offset})'

