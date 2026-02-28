.. _exos.rst:

Exercices
#########

..  contents:: Contenu de la page
    :depth: 3

Résolution de Sudoku
====================

Résolvez le Sudoku suivant (ou d'autres disponibles sur le Web) à l'aide du
solveur de contraintes ``ToyCSP``.

..  activecode:: session2_exos_sudoku1
    :language: webtp

    ######################## Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    ############################################################

    

    ############### Parameters #######################################
    grid = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]


    ############### Decision variables ###############################
            
    ############### Constraints ######################################
    # Row constraints
        
    # Column constraints

    # Subsquare constrains

    def show_solution(csp):
        ...
        
            
Choix des variables
===================

Implémentez une manière alternative à ``first_not_fixed`` de choisir la
prochaine variable à fixer dans le ``dfs`` en faisant un choix plus intelligent
consistant à choisir à chaque fois la variable dont le domaine est le plus
petit. Testez cette heuristique de choix de variable à la place de
``first_not_fixed`` en comparant son effet sur la recherche (temps, nombre
d'appels récursifs de ``dfs``, ...) pour le problème des n dames pour :math:`n =
9`.

Définissez une méthode ``smallest_not_fixed`` qui fonctionne comme
``first_not_fixed`` mais qui retourne la variable non assignée ayant le plus
petit domaine.

Rajoutez un paramètre à la méthode ``dfs`` permettant de choisir l'heuristique
de choix de variable lors de son appel.

..  activecode:: session2_exos_smallest_not_fixed
    :language: webtp

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


..  reveal:: 3ffc59a8-a34a-4b57-b13e-1237e8e22934
    :showtitle: Solution
    :instructoronly:

    ..  activecode:: 31994923-f446-476e-a6b3-5f65540b4d82
        :language: webtp

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
                
            def max(self) -> int:
                return max(self.values)

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

            def as_list(self) -> list[int]:
                return sorted(list(self.values))

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
                min_size = float("inf")
                smallest_var = None
                for var in self.variables:
                    if not var.dom.is_fixed() and var.dom.size() < min_size:
                        min_size = var.dom.size()
                        smallest_var = var
                return smallest_var if smallest_var else None

            def min_value(self, var):
                return var.dom.min()

            def max_value(self, var):
                return var.dom.max()

            def mid_value(self, var):
                n = len(var.dom)
                return var.dom.as_list()[n // 2]

            def get_solution(self) -> list[int]:
                return [v.value() for v in self.variables]

            def dfs(self, var_heuristic=None, val_heuristic=None) -> None:
                var_heuristic = var_heuristic or ToyCSP.first_not_fixed
                val_heuristic = val_heuristic or ToyCSP.min_value
                self.n_recur += 1

                # Choisissez une variable non fixée (première rencontrée ou la plus petite)
                not_fixed = (
                    var_heuristic(self)
                )  # Essayer d'abord first_not_fixed (implémentation originale) ensuite smallest_not_fixed

                if not not_fixed:
                    # Toutes les variables sont fixées, une solution est trouvée
                    self.call_handlers("solution", {})
                else:
                    variable = not_fixed
                    value = val_heuristic(self, variable)
                    backup = self.backup_domains()

                    # Branche gauche : affecter la valeur à la variable
                    try:
                        variable.dom.fix(value)
                        self.fix_point()
                        self.dfs(var_heuristic=var_heuristic, val_heuristic=val_heuristic)
                    except Inconsistency:
                        self.call_handlers("inconsistent", {"event": "inconsistent", "current_var": variable})

                    # Restaurer les domaines avant d'explorer la branche droite
                    self.restore_domains(backup)

                    # Branche droite : retirer la valeur du domaine de la variable
                    try:
                        variable.dom.remove(value)
                        self.fix_point()
                        self.dfs(var_heuristic=var_heuristic, val_heuristic=val_heuristic)
                    except Inconsistency:
                        self.call_handlers("inconsistent", {"event": "inconsistent", "current_var": variable})

        def nqueens(n: int):
            # problème
            csp: ToyCSP = ToyCSP()
            # variables de décision
            q: list[Variable] = [csp.add_variable(range(n)) for _ in range(n)]

            ## Déclaration des contraintes du problème
            for i in range(n):
                for j in range(i + 1, n):
                    # Pas deux reines sur la même ligne,
                    csp.post(NotEqual(q[i], q[j], 0))
                    # Pas deux reines sur une diagonale montante
                    csp.post(NotEqual(q[i], q[j], i - j))
                    # Pas deux reines sur une diagonale descendante
                    csp.post(NotEqual(q[i], q[j], j - i))

            @csp.on('solution')
            def handle_solution(csp, infos):
                solutions.append(csp.get_solution())
                #print(sol)

            solutions = []
            csp.dfs(var_heuristic=ToyCSP.smallest_not_fixed, val_heuristic=ToyCSP.min_value)

            return solutions

        # profiling : https://realpython.com/python-profiling/
        from cProfile import Profile
        from pstats import SortKey, Stats

        import sys

        try:
            n = int(sys.argv[1])
        except:
            n = 9

        with Profile() as profile:
            print(f"{nqueens(n) = }\n\nfor {n = }")
            (
                Stats(profile)
                .strip_dirs()
                .sort_stats(SortKey.CUMULATIVE)
                .print_stats()
            )





