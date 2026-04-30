.. _statemanager.rst:

State Manager
#############

..  contents:: Contenu de la page
    :depth: 3

Une partie très importante d'un solveur de programmation par contrainte réside
dans la manière de sauvegarder l'état de la recherche avant chaque branchement
dans l'arbre de recherche, afin de pouvoir le restaurer lorsqu'on effectue un
retour-arrière (*backtrack*) en cas d'inconsistence.

Le problème avec ``ToyCSP``
===========================

Dans le solveur ToyCSP, la sauvegarde / restauration s'effectue en effectuant
une copie de toutes les valeurs de tous les domaines. Ceci prend beaucoup de
temps et de mémoire. En réalité, il faudrait pouvoir sauvegarder et restaurer
les sauvegardes très efficacement (idéalement en :math:`\Theta(1)` pour chaque
domaine).

Le code de sauvegarde / restauration de ToyCSP
----------------------------------------------

Identifiez dans le code ci-dessous les parties du code qui s'occupent de
sauvegarder et restaurer le problème à chaque retour-arrière dans l'arbre de
recherche:

..  activecode:: d7826bb9-5864-4c5a-9628-1a233802b551
    :language: webtp
    :interpreterargs: debug_mode=true&layout=["Editor", "Console"]

    from collections.abc import Iterable
    from abc import ABC, abstractmethod
    from typing import override
    from typing import List, Optional, Any, Callable

    class Inconsistency(Exception):
        pass


    class Domain:
        def __init__(self, *args) -> None:
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
            return len(self.values) == 1

        def size(self) -> int:
            return len(self.values)

        def __len__(self) -> int:
            return self.size()

        def min(self) -> int:
            return min(self.values)

        def remove(self, v: int) -> bool:
            if v in self.values:
                self.values.remove(v)
                if not self.values:
                    raise Inconsistency
                return True
            return False

        def fix(self, v: int):
            if v not in self.values:
                raise Inconsistency
            self.values = {v}

        def clone(self) -> "Domain":
            return Domain(self.values)

        def __repr__(self) -> str:
            return f"Domain({self.values})"

    class Variable:

        var_counter = 0

        def __init__(self, dom: Iterable[int], name: str = None) -> None:
            self.dom = Domain(set(dom))
            self.name = name or 'Var' + str(Variable.var_counter)
            Variable.var_counter += 1

        def value(self) -> int:
            if self.dom.is_fixed():
                return self.dom.min()
            else:
                return None


        def __repr__(self) -> str:
            return f"Variable(dom={self.dom.values}, name='{self.name}')"

    class Constraint(ABC):
        @abstractmethod
        def propagate(self) -> bool:
            pass



    class NotEqual(Constraint):
        def __init__(self, x: Variable, y: Variable, offset: int = 0) -> None:
            self.x = x
            self.y = y
            self.offset = offset

        @override
        def propagate(self) -> bool:
            if self.x.dom.is_fixed():
                return self.y.dom.remove(self.x.dom.min() - self.offset)
            elif self.y.dom.is_fixed():
                return self.x.dom.remove(self.y.dom.min() + self.offset)
            return False

        def __repr__(self) -> str:
            return f'NotEqual(x={self.x}, y={self.y}, offset={self.offset})'


    class ToyCSP:
        def __init__(self, *args, **kwargs):

            self.constraints: List[Constraint] = []
            self.variables: List[Variable] = []
            self.n_recur = 0  # Number of recursive calls

            # collects all handlers (args beginning with `on_`)
            self.handlers = {
                arg.split('on_')[1]: [value] for arg, value in kwargs.items() if arg.startswith("on_")
            }

        def __repr__(self) -> str:
            #return f"ToyCSP(constraints={self.constraints}, variables={self.variables})"
            return f"ToyCSP : #vars = {len(self.variables)} / #constraints = {len(self.constraints)}"

        ############ Event handler registration and management
        def register_handler(self, event, handler) -> None:
            if event in self.handlers:
                self.handlers[event].append(handler)
            else:
                self.handlers[event] = [handler]

        def call_handlers(self, event: str, infos: dict[str, Any]) -> None:
            if event in self.handlers:
                handlers = self.handlers[event]
                for h in handlers: h(self, infos)

        def on(self, *events):
            def decorator(func):
                for event in events:
                    self.register_handler(event, func)
            return decorator

        def no_op(self, csp: "ToyCSP", infos: dict[str, Any]) -> None:
            pass

        ##############################################################3

        def add_variable(self, domain: Iterable[int]) -> Variable:
            var = Variable(domain)
            self.variables.append(var)
            return var

        def post(self, constraint: Constraint, schedule_fixpoint=True) -> Constraint:
            self.constraints.append(constraint)
            if schedule_fixpoint:
                self.fix_point()

        def fix_point(self) -> bool:
            self.call_handlers("beforefixpoint", {"event": "before fixpoint"})

            fix = False
            while not fix:
                fix = True
                for constraint in self.constraints:
                    was_usefull = constraint.propagate()
                    # if only one propagation is usefull amongst all constraints,
                    # fix will become false and the while
                    # loop will continue
                    fix &= not was_usefull
                    self.call_handlers("propagate", {
                            "event": f"propagating",
                            "usefull": was_usefull,
                            "constraint": constraint,
                        })

            self.call_handlers("afterfixpoint", {"event": "after fixpoint"})

            return fix

        def backup_domains(self) -> List[Domain]:
            backup = [var.dom.clone() for var in self.variables]
            return backup

        def restore_domains(self, backup: List[Domain]) -> None:
            for i, var in enumerate(self.variables):
                var.dom = backup[i]

        def first_not_fixed(self) -> Optional[Variable]:
            # https://www.programiz.com/python-programming/methods/built-in/next
            return next((var for var in self.variables if not var.dom.is_fixed()), None)

        def smallest_not_fixed(self) -> Optional[Variable]:
            '''to be modified '''
            return None

        def get_solution(self) -> list[int]:
            return [v.value() for v in self.variables]

        def dfs(self) -> None:
            self.n_recur += 1

            # Choisissez une variable non fixée (première rencontrée ou la plus petite)
            not_fixed = (
                self.first_not_fixed()
            )  # Essayer d'abord first_not_fixed (implémentation originale)

            if not not_fixed:
                # Toutes les variables sont fixées, une solution est trouvée
                self.call_handlers("solution", {})
            else:
                variable = not_fixed
                value = variable.dom.min()
                backup = self.backup_domains()

                # Branche gauche : affecter la valeur à la variable
                try:
                    variable.dom.fix(value)
                    self.fix_point()
                    self.dfs()
                except Inconsistency:
                    self.call_handlers("inconsistent", {"event": "inconsistent", "current_var": variable})

                # Restaurer les domaines avant d'explorer la branche droite
                self.restore_domains(backup)

                # Branche droite : retirer la valeur du domaine de la variable
                try:
                    variable.dom.remove(value)
                    self.fix_point()
                    self.dfs()
                except Inconsistency:
                    self.call_handlers("inconsistent", {"event": "inconsistent", "current_var": variable})

    # Problème des n dames
    n = int(input("Taille du problème: "))

    csp: ToyCSP = ToyCSP()
    q: list[Variable] = [csp.add_variable(range(n)) for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            csp.post(NotEqual(q[i], q[j], 0))
            csp.post(NotEqual(q[i], q[j], i - j))
            csp.post(NotEqual(q[i], q[j], j - i))

    @csp.on('solution')
    def handle_solution(csp, infos):
        solutions.append(csp.get_solution())

    solutions = []
    csp.dfs()

    print(f"{solutions = }")
    

..  reveal:: 00b951f2-00d5-4280-b679-84fbd1492047
    :showtitle: Réponse

    Les lignes suivantes de la méthode ``dfs`` effectuent ces opérations

    ..  code-block:: python
        :linenos:
        :emphasize-lines: 12, 21

        def dfs(self) -> None:
            self.n_recur += 1

            not_fixed = (
                self.first_not_fixed()
    
            if not not_fixed:
                self.call_handlers("solution", {})
            else:
                variable = not_fixed
                value = variable.dom.min()
                backup = self.backup_domains()

                try:
                    variable.dom.fix(value)
                    self.fix_point()
                    self.dfs()
                except Inconsistency:
                    ...

                self.restore_domains(backup)

                try:
                    variable.dom.remove(value)
                    self.fix_point()
                    self.dfs()
                except Inconsistency:
                    ...

Conclusion
----------

Le solveur ToyCSP présente deux problèmes majeurs au niveau de la gestion des
sauvegardes / restauration :

- Lenteur : la copie de tous les domaines est :math:`\Theta(m \cdot n)` où
  :math:`m` est le nombre de variables et :math:`n` la taille des domaines. De
  plus, la copie se fait intégralement à chaque branchement dans l'arbre de
  recherche.

- Uniquement les domaines des variables sont saugegardées, alors que d'autres
  informations sont nécessaires dans un solveur avancé dans lequel on rajoute
  des variables et des contraintes au fur et à mesure de la recherche. Il
  faudrait donc également sauvegarder la file de propagation, l'état
  d'activation des contraintes, ...


Un meilleur gestionnaire d'état
===============================

Nous avons besoin d'un gestionnaire d'état (*state manager*) capable de faire un
suivi de toutes les valeurs à sauvegarder / restaurer et de n'effectuer que les
opérations nécessaires.

Spécifications
--------------

Le gestionnaire d'état va effectuer le suivi des objets (nombres entiers ou
objets plus complexes) dont il faut sauvegarder et restaurer l'état.

..  admonition:: Exemple d'utilisation pour des nombres entiers

    Voici un exemple qui montre le fonctionnement du ``CopyStateManager`` pour
    faire le suivi de nombres entiers.

    ..  note:: 

        Remarquez l'on ne peut pas utiliser de simples nombres entiers Python
        avec l'opérateur d'affectation pour lire / écrire la valeur des
        variables. On utilise pour ce faire un type d'entier personnalisé, de la
        classe ``CopyInt`` dont on modifie la valeur avec la méthode
        ``.set_value(new_value)`` et dont on lit la valeur avec ``.value()``.

    ::

        >>> sm = CopyStateManager()
        >>> sm.get_level()
        -1
        >>> x = sm.make_state_int(1)
        >>> x
        CopyInt(1)
        >>> x.value()
        1
        >>> sm.save_state()
        >>> sm.get_level()
        0
        >>> x.set_value(2)
        2
        >>> y = sm.make_state_int(10)
        >>> sm.save_state()
        >>> sm.get_level()
        1
        >>> x.set_value(3)
        3
        >>> x.value()
        3
        >>> y.set_value(20)
        20
        >>> sm.prior
        Stack([Backup([CopyStateEntry(1)]), Backup([CopyStateEntry(2), CopyStateEntry(10)])])
        >>> sm.store
        Stack([CopyInt(3), CopyInt(20)])
        >>> sm.restore_state()
        >>> x
        CopyInt(2)
        >>> y
        CopyInt(10)
        >>> sm.get_level()
        0
        >>> sm.restore_state()
        >>> x
        CopyInt(1)
        >>> y
        CopyInt(10)
        >>> sm.get_level()
        -1

        >>> sm = CopyStateManager()
        >>> z = [sm.make_state_int(2 * i) for i in range(3)]
        >>> sm.save_state()
        >>> for x in z: x.increment()
        1
        3
        5
        >>> z
        [CopyInt(1), CopyInt(3), CopyInt(5)]
        >>> sm.restore_state()
        >>> z
        [CopyInt(0), CopyInt(2), CopyInt(4)]


..  admonition:: Exemple avec des objets plus complexes

    ::

        >>> sm = CopyStateManager()
        >>> obj = sm.make_state_obj(True)
        >>> obj
        Copy(True)
        >>> sm.save_state()
        >>> obj.set_value(False)
        False
        >>> obj
        Copy(False)

        >>> sm = CopyStateManager()
        >>> obj = sm.make_state_obj([1, 2, 3])
        >>> obj
        Copy([1, 2, 3])
        >>> sm.save_state()
        >>> obj.set_value("this is a bad example")
        'this is a bad example'
        >>> obj
        Copy('this is a bad example')
        >>> sm.restore_state()
        >>> obj
        Copy([1, 2, 3])


Interface ``StateManager``
--------------------------

..  code-block:: python
    :linenos:

    from typing import Protocol
    from collections.abc import Callable

    type Procedure = Callable[[], None]


    class StateManager(Protocol):
        '''
        The StateManager exposes all the mechanisms and data-structures needed to
        implement a depth-first-search with reversible states.
        '''

        def save_state(self) -> None:
            '''
            Stores the current state such that it can be recovered using
            restore_state(). Increase the level by 1
            '''
            ...

        def restore_state(self) -> None:
            '''
            Restores state as it was at `get_level()-1`
            Decrease the level by 1
            '''
            ...

        def restore_state_until(self, level: int) -> None:
            '''
            Restores the state up the the given level.

            param: level the level, a non negative number between 0 and get_level
            '''
            ...

        def on_restore(self, listener: Procedure) -> None:
            '''
            Add a listener that is notified each time the `restore_state()` is
            called.
            '''
            ...

        def get_level(self) -> int:
            '''
            Returns the current level. It is increased at each `save_state()` and
            decreased at each `restore_state()`. It is initially equal to -1.
            
            returns current the level
            '''
            ...

        def make_state_int(self, init_value: int) -> StateInt:
            """
            Creates an Integer that can be restored in place on `restore_state()`
            """
            ...

        def make_state_obj[T](self, obj: T) -> State[T]:
            """
            Creates an object of type `T` that can be restored in place on
            `restore_state()`
            """
            ...

Étude du code de ``CopyStateManager``
=====================================

..  activecode:: study_copy_state_manager
    :language: webtp
    :interpreterargs: branch=branch&debug_mode=true&layout=["Editor", "Console"]

    ############### Importation dans WebTigerPython ############
    from pyodide.http import open_url

    def load_external_files(files: list[str]) -> None:
        prefix = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/turingcp/'
        for file in files:
            module = file.split('/')[-1]
            with open(module, 'w') as fd: fd.write(open_url(prefix + file).read())

    load_external_files([
        'stack.py',
    ])
    ############################################################

    from typing import Protocol
    from collections.abc import Callable

    from stack import Stack

    type Procedure = Callable[[], None]
    
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

    class StateManager(Protocol):
        '''
        The StateManager exposes all the mechanisms and data-structures needed to
        implement a depth-first-search with reversible states.
        '''

        def save_state(self) -> None:
            '''
            Stores the current state such that it can be recovered using
            restore_state(). Increase the level by 1
            '''
            ...

        def restore_state(self) -> None:
            '''
            Restores state as it was at `get_level()-1`
            Decrease the level by 1
            '''
            ...

        def restore_state_until(self, level: int) -> None:
            '''
            Restores the state up the the given level.

            param: level the level, a non negative number between 0 and get_level
            '''
            ...

        def on_restore(self, listener: Procedure) -> None:
            '''
            Add a listener that is notified each time the `restore_state()` is
            called.
            '''
            ...

        def get_level(self) -> int:
            '''
            Returns the current level. It is increased at each `save_state()` and
            decreased at each `restore_state()`. It is initially equal to -1.
            
            returns current the level
            '''
            ...

        def make_state_int(self, init_value: int) -> StateInt:
            """
            Creates an Integer that can be restored in place on `restore_state()`
            """
            ...

        def make_state_obj[T](self, obj: T) -> State[T]:
            """
            Creates an object of type `T` that can be restored in place on
            `restore_state()`
            """
            ...

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
            return f"{self.__class__.__name__}({repr(self._v)})"


    class CopyInt(Copy[int], StateInt):

        def __init__(self, init_value: int) -> None:
            super().__init__(init_value)


    class CopyStateManager(StateManager):
        """
        >>> sm = CopyStateManager()
        >>> sm.get_level()
        -1
        >>> x = sm.make_state_int(1)
        >>> x
        CopyInt(1)
        >>> x.value()
        1
        >>> sm.save_state()
        >>> sm.get_level()
        0
        >>> x.set_value(2)
        2
        >>> y = sm.make_state_int(10)
        >>> sm.save_state()
        >>> sm.get_level()
        1
        >>> x.set_value(3)
        3
        >>> x.value()
        3
        >>> y.set_value(20)
        20
        >>> sm.prior
        Stack([Backup([CopyStateEntry(1)]), Backup([CopyStateEntry(2), CopyStateEntry(10)])])
        >>> sm.store
        Stack([CopyInt(3), CopyInt(20)])
        >>> sm.restore_state()
        >>> x
        CopyInt(2)
        >>> y
        CopyInt(10)
        >>> sm.get_level()
        0
        >>> sm.restore_state()
        >>> x
        CopyInt(1)
        >>> y
        CopyInt(10)
        >>> sm.get_level()
        -1

        >>> sm = CopyStateManager()
        >>> z = [sm.make_state_int(2 * i) for i in range(3)]
        >>> sm.save_state()
        >>> for x in z: x.increment()
        1
        3
        5
        >>> z
        [CopyInt(1), CopyInt(3), CopyInt(5)]
        >>> sm.restore_state()
        >>> z
        [CopyInt(0), CopyInt(2), CopyInt(4)]
        """

        class Backup(Stack[StateEntry]):

            def __init__(self, store):
                super().__init__()
                self._store = store
                self._sz = len(self._store)
                for s in self._store:
                    self.push(s.save())

            def restore(self) -> None:
                for state_entry in self:
                    state_entry.restore()

        def __init__(self) -> None:
            self.store: Stack[Storage] = Stack[Storage]()
            self.prior: Stack[self.Backup] = Stack[self.Backup]()
            # à voir si on veut une LinkedList ici ...
            self.on_restore_listeners: list[Procedure] = []

        def notify_restore(self) -> None:
            for listener in self.on_restore_listeners:
                listener()

        def on_restore(self, listener: Procedure) -> None:
            self.on_restore_listeners.append(listener)

        def get_level(self) -> int:
            return len(self.prior) - 1

        def store_size(self) -> int:
            return len(self.store)

        def save_state(self) -> None:
            self.prior.push(self.Backup(self.store))

        def restore_state(self) -> None:
            self.prior.pop().restore()
            self.notify_restore()

        def restore_state_until(self, level: int) -> None:
            while self.get_level() > level:
                self.restore_state()

        def with_new_state(self, proc: Procedure) -> None:
            level: int = self.get_level()
            self.save_state()
            proc()
            self.restore_state_until(level)

        def make_state_int(self, init_value: int) -> StateInt:
            """
            Creates an Integer that can be restored in place on `restore_state()`
            """
            s: CopyInt = CopyInt(init_value)
            self.store.push(s)
            return s

        def make_state_obj[T](self, obj: T) -> State[T]:
            """
            >>> sm = CopyStateManager()
            >>> obj = sm.make_state_obj(True)
            >>> obj
            Copy(True)
            >>> sm.save_state()
            >>> obj.set_value(False)
            False
            >>> obj
            Copy(False)

            >>> sm = CopyStateManager()
            >>> obj = sm.make_state_obj([1, 2, 3])
            >>> obj
            Copy([1, 2, 3])
            >>> sm.save_state()
            >>> obj.set_value("this is a bad example")
            'this is a bad example'
            >>> obj
            Copy('this is a bad example')
            >>> sm.restore_state()
            >>> obj
            Copy([1, 2, 3])
            """
            r: Copy = Copy(init_value=obj)
            self.store.push(r)
            return r

    def test():
        import doctest

        doctest.testmod()

    if __name__ == "__main__":
        test()