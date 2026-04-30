.. _cpsolver-stack.rst:

Pile optimisée pour le solveur
##############################

..  contents:: Contenu de page
    :depth: 3

Dans la section :ref:`stacks.rst`, nous avons développé une classe ``ListStack``
utilisant une liste Python pour stocker les éléments.

Nous utiliserons des piles dans le solveur de contraintres pour les objectifs
suivants:

- Sauvegarder l'état de la résolution (domaines des variables, ...) lors de
  chaque appel récursif (descente d'un niveau dans l'arbre de recherche)

- Stocker les variables de décision

En particulier dans le cas de la sauvegarde de l'état, la pile est souvent
amenée à diminuer et à réaugmenter. Le problème est que cela demande du temps
inutile à Python de redimensionner la liste sous-jacente. Nous allons donc
modifier le comportement de notre pile pour que même si les éléments sont
dépilés de la pile, la liste sous-jacente ne soit pas redimensionnée. 

Spécifications
==============

À partir du code ci-dessous, par dérivation de la classe ``ListStack``, créez
une nouvelle classe ``Stack`` dont la liste sous-jacente ne peut que croître en
cas de besoin, mais jamais décroître. Autrement dit, il faut rajouter un
attribut (privé) ``_size`` représentant le nombre d'éléments sur la pile mais
différent de la taille de la liste sous-jacente.

- Lorsqu'on fait un ``push``, si la liste sous-jacente encore de la place, on
  ajoute simplement le nouvel élément à la suite des autres dans la liste à
  l'emplacement ``self._items[self._size] = new_item``. Si, en revanche, il n'y a plus de
  place, on fait un ``self._items.append(new_item)``

- Adaptez la méthode ``pop`` de manière correspondante

- De plus, modifiez la classe pour qu'il soit possible d'itérer sur les éléments
  présents dans la pile avec une boucle ``for`` :

  ..  note:: Implémenter le protocole d'itérateur

      Pour pouvoir parcourir les éléments d'une pile avec une boucle ``for``, il
      est nécessaire de surcharger les méthodes ``__iter__`` et ``__next__``.
      Rajoutez une variable d'instance ``_iter_counter`` initialisé à 0 par
      ``__iter__`` et qui est incrémenté lors de chaque appel de ``__next__``.

  ::

      s = Stack()
      s.push(3)
      s.push(5)
      s.push(7)
      for item in s:
          print(item)

- Modifiez le constructeur de la classe pour qu'il soit possible d'initialiser
  la pile avec un itérable d'éléments

  ::

      >>> s = Stack([1, 3, 5])
      >>> s
      Stack([1, 3, 5])

..  activecode:: cpstack_py_student
    :language: webtp
    :interpreterargs: vanilla_python=true&debug_mode=true&layout=["Editor", "Console"]

    ############### Importation dans WebTigerPython ############
    from pyodide.http import open_url

    def load_external_files(files: list[str]) -> None:
        prefix = 'https://raw.githubusercontent.com/informatiquecsud/algo-ds/refs/heads/solutions/ds_single_files/'
        for file in files:
            module = file.split('/')[-1]
            with open(module, 'w') as fd: fd.write(open_url(prefix + file).read())

    load_external_files([
        'stack.py',
    ])
    ############################################################

    from typing import Generic, TypeVar
    from collections.abc import Iterable

    from stack import StackADT, EmptyStackError

    T = TypeVar('T')

    class ListStack(StackADT[T], Generic[T]):
        '''

        ``ListStack`` implements a stack by using a list as the container.

        >>> s: ListStack[int] = ListStack()
        >>> s.push(1)
        >>> s
        ListStack([1])
        >>> s.push(2)
        >>> s
        ListStack([1, 2])
        >>> s.push(3)
        >>> s
        ListStack([1, 2, 3])
        >>> s.peek()
        3
        >>> s.pop()
        3
        >>> s
        ListStack([1, 2])
        >>> s.pop()
        2
        >>> s.pop()
        1
        >>> s
        ListStack([])

        '''

        def __init__(self) -> None:
            self._items = []

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({repr(self._items)})'

        def __len__(self) -> int:
            return len(self._items)

        def push(self, item: T) -> None:
            self._items.append(item)

        def pop(self) -> T:
            try:
                return self._items.pop()
            except IndexError as e:
                raise EmptyStackError('Pop from an empty stack') from e

        def peek(self) -> T:
            try:
                return self._items[-1]
            except IndexError as e:
                raise EmptyStackError('Peek an empty stack') from e

        def is_empty(self) -> bool:
            return len(self) == 0


    if __name__ == '__main__':
        import doctest
        doctest.testmod()


..  reveal:: 78ab4fab-b9dd-4f0a-aac0-ec0ad365dd9e
    :showtitle: Solution
    :instructoronly:

    ..  activecode:: 65e04199-2eab-4b76-9d45-7913896d3faa
        :language: webtp
        :interpreterargs: vanilla_python=true&debug_mode=true&layout=["Editor", "Console"]


        ############### Importation dans WebTigerPython ############
        from pyodide.http import open_url

        def load_external_files(files: list[str]) -> None:
            prefix = 'https://raw.githubusercontent.com/informatiquecsud/algo-ds/refs/heads/solutions/ds_single_files/'
            for file in files:
                module = file.split('/')[-1]
                with open(module, 'w') as fd: fd.write(open_url(prefix + file).read())

        load_external_files([
            'stack.py',
        ])
        ############################################################

        from typing import Generic, TypeVar
        from collections.abc import Iterable

        from stack import StackADT, EmptyStackError

        T = TypeVar('T')

        class Stack(StackADT[T], Generic[T]):
            '''

            ``Stack`` implements a stack by using a list as the container.

            >>> s: Stack[int] = Stack()
            >>> s.push(1)
            >>> s
            Stack([1])
            >>> s.push(2)
            >>> s
            Stack([1, 2])
            >>> s.push(3)
            >>> s
            Stack([1, 2, 3])
            >>> len(s)
            3
            >>> s.peek()
            3
            >>> s.pop()
            3
            >>> s
            Stack([1, 2])
            >>> s.pop()
            2
            >>> s.pop()
            1
            >>> s
            Stack([])
            >>> s.pop()
            Traceback (most recent call last):
                ...
            stack.EmptyStackError: Pop from an empty stack
            >>> s.peek()
            Traceback (most recent call last):
                ...
            stack.EmptyStackError: Peek an empty stack

            
            # Iterator protocol and stack initialization
            >>> s: Stack[int] = Stack([1,2,3])
            >>> [item for item in s]
            [1, 2, 3]

            '''

            def __init__(self, items: Iterable[T] | None = None) -> None:
                self._items = list(items) if items is not None else []
                self._iter_position = 0

                # initially _item size is the real size
                self._real_size = len(self._items)

            def __repr__(self) -> str:
                return f'{self.__class__.__name__}({self._items[:self._real_size]})'

            def __len__(self) -> int:
                return self._real_size

            def push(self, item: T) -> None:
                if self._real_size < len(self._items):
                    self._items[self._real_size] = item
                else:
                    self._items.append(item)
                self._real_size += 1

            def pop(self) -> T:
                if self._real_size == 0:
                    raise EmptyStackError('Pop from an empty stack')

                item = self._items[self._real_size - 1]
                self._real_size -= 1
                return item

            def peek(self) -> T:
                if self._real_size == 0:
                    raise EmptyStackError('Peek an empty stack')
                return self._items[self._real_size - 1]

            def is_empty(self) -> bool:
                return len(self) == 0
            
            def __iter__(self):
                self._iter_position = 0
                return self
            
            def __next__(self):
                if self._iter_position < self._real_size:
                    item: T = self._items[self._iter_position]
                    self._iter_position += 1
                    return item

                raise StopIteration
                    

        if __name__ == '__main__':
            import doctest
            doctest.testmod()