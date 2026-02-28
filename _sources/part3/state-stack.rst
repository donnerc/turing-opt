..  _state-stack.rst:

Une pile restaurable
####################

..  contents:: Contenu de la page
    :depth: 3

Notre solveur aura besoin d'une pile restaurable par le gestionnaire d'états.


Classe ``StateStack``
=====================

Reprenez le code de la pile optimisée développée dans la section
:ref:`cpsolver-stack.rst` pour qu'elle soit restaurable par le gestionnaire
d'états. 

..  note:: 

    Étant donné la manière dont nous avons développé la classe ``Stack``, la
    seule chose qu'il faut restaurer pour restaurer la pile est l'attribut
    indiquant sa taille

Code de base
------------

..  activecode:: state_stack
    :language: webtp
    :interpreterargs: vanilla_python=true&debug_mode=true&layout=["Editor", "Console"]

    ############### Importation dans WebTigerPython ############
    from pyodide.http import open_url

    def load_external_files(files: list[str]) -> None:
        prefix = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/turingcp/'
        for file in files:
            module = file.split('/')[-1]
            with open(module, 'w') as fd: fd.write(open_url(prefix + file).read())

    load_external_files([
        'stack.py',
        'state_types.py',
        'state.py',
    ])
    ############################################################

    from typing import Generic, TypeVar
    from collections.abc import Iterable

    from stack import StackADT, StackException, EmptyStackError
    from state_types import StateManager, StateInt
    from state import CopyStateManager

    T = TypeVar('T')

    class StateStack(StackADT[T], Generic[T]):
        '''

        ``StateStack`` is a restorable stack that can be restored in O(1) time.

        >>> sm = CopyStateManager()
        >>> s: StateStack[int] = StateStack(sm)
        >>> s.push(1)
        >>> s
        StateStack([1])
        >>> s.push(2)
        >>> s
        StateStack([1, 2])
        >>> s.push(3)
        >>> s
        StateStack([1, 2, 3])
        >>> len(s)
        3
        >>> s.peek()
        3
        >>> s.pop()
        3
        >>> s
        StateStack([1, 2])
        >>> s.pop()
        2
        >>> s.pop()
        1
        >>> s
        StateStack([])
        >>> s.pop()
        Traceback (most recent call last):
            ...
        stack.EmptyStackError: Pop from an empty stack
        >>> s.peek()
        Traceback (most recent call last):
            ...
        stack.EmptyStackError: Peek an empty stack

        
        # Iterator protocol and stack initialization
        >>> sm = CopyStateManager()
        >>> s: StateStack[int] = StateStack(sm, [1,2,3])
        >>> [item for item in s]
        [1, 2, 3]

        '''

        def __init__(self, sm: StateManager, items: Iterable[T] | None = None) -> None:
            self._items: list[T] = list(items) if items is not None else []
            self._iter_position = 0

            # initially _item size is the real size
            self._real_size: StateInt = ...

        ...        
        
    def test_restore():
        '''
        >>> sm = CopyStateManager()
        >>> s = StateStack(sm, [4, 6, 8])
        >>> sm.save_state()
        >>> s.pop()
        8
        >>> s
        StateStack([4, 6])
        >>> sm.save_state()
        >>> s.pop()
        6
        >>> sm.save_state()
        >>> s.pop()
        4
        >>> s
        StateStack([])
        >>> sm.restore_state()
        >>> s
        StateStack([4])
        >>> sm.restore_state()
        >>> s
        StateStack([4, 6])
        >>> sm.restore_state()
        >>> s
        StateStack([4, 6, 8])
        '''


    if __name__ == '__main__':
        import doctest
        doctest.testmod()
        
