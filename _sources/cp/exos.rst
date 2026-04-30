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
    :interpreterargs: branch=branch&layout=["Editor", "Console"]

    ######################## Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    SUDOKUS_URL = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/sudokus.txt'
    with open('sudoku-instances.txt', 'w') as fd: fd.write(open_url(SUDOKUS_URL).read())
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

Benchmarking
------------

Testez l'efficacité du solveur de contraintes pour résoudre les Sudokus donnés
dans le fichier http://magictour.free.fr/top1465 en mesurant le temps
d'exécution de la fonction de résolution du Sudoku pour chacun de ces Sudokus.

Déterminez les 10 Sudokus les plus difficiles à résoudre pour le solveur de
contraintes en comparant les temps d'exécution pour chacun de ces Sudokus.

..  note::
    
    Vous pouvez utiliser la bibliothèque Python ``time`` pour mesurer le temps
    d'exécution de la fonction de résolution du Sudoku.


Optimisations du solveur de contraintes
=======================================

..  note::

    Il faut mieux travailler dans Visual Studio Code pour cet exercice, car il
    nécessite de faire des modifications dans le code du solveur de contraintes
    et d'avoir tous les fichiers à disposition.

    - Clonez le dépôt GitHub du projet : https://github.com/donnerc/pyminicp

    Vous trouvez le code de ``ToyCSP`` dans le dossier ``toycsp`` du projet.
    Vous pouvez aussi trouver une version bundle de ce code dans
    ``build/toycsp_bundle.py`` que vous pouvez utiliser dans WebTigerPython.

Optimisation 1 (Méthode ``fix_point``)
--------------------------------------

Modifiez la méthode ``ToyCSP.fix_point`` de la manière suivante

- Au lieu de faire une boucle sur toutes les contraintes et d'appeler la méthode
  ``propagate`` de chacune d'entre elles, faites une boucle sur les variables
  qui ont été fixées lors de l'appel de la méthode ``fix_point`` et appelez la
  méthode ``propagate`` uniquement pour les contraintes qui sont liées à ces
  variables. Testez l'effet de cette modification sur la recherche (temps,
  nombre d'appels récursifs de ``dfs``, ...) pour le problème des n dames pour
  :math:`n = 9`.

  ..  reveal:: 54f95427-6094-4375-bac6-887cd371cef0
      :showtitle: Indication

      Pour cela, vous pouvez ajouter un attribut ``constraints`` à la classe
      ``Variable`` qui contiendra la liste des contraintes liées à cette
      variable, et que vous mettrez à jour lors de l'ajout de contraintes dans
      le CSP.

- Au lieu de répéter la propagation jusqu'à ce que plus aucun domaine ne soit
  modifié, rajoutez un paramètre ``max_iterations`` à la méthode ``fix_point``
  qui limitera le nombre d'itérations de propagation. Testez l'effet de cette
  modification sur la recherche (temps, nombre d'appels récursifs de ``dfs``,
  ...) pour le problème des n dames pour :math:`n = 9`.

- La méthode ``fix_point`` appelle ``self.call_handlers("propagate", ...)`` à
  chaque propagation, même si aucun gestionnaire n'est enregistré pour cet
  événement. Modifiez la méthode pour n'appeler les gestionnaires de l'événement
  "propagate" que s'il y en a au moins un d'enregistré. Testez l'effet de cette
  modification sur la recherche (temps, nombre d'appels récursifs de ``dfs``,
  ...) pour le problème des n dames pour :math:`n = 9`.

Optimisation 2 (Choix de variable dans le ``dfs``)
--------------------------------------------------

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

..
    Optimisation 3 (Choix de valeur dans le ``dfs``)
    ------------------------------------------------

    Implémentez une manière alternative à ``min_value`` de choisir la prochaine
    valeur à fixer pour une variable dans le ``dfs`` en faisant un choix plus
    intelligent consistant à choisir à chaque fois la valeur médiane du domaine de
    la variable. Testez cette heuristique de choix de valeur à la place de
    ``min_value`` en comparant son effet sur la recherche (temps, nombre d'appels
    récursifs de ``dfs``, ...) pour le problème des n dames pour :math:`n = 9`.


Optimisation 3
--------------

Dans l'implémentation actuelle du solveur de contraintes, de nombreuses
propagations inutiles sont effectuées lors de la recherche, notamment lors de
l'exploration de la branche droite du ``dfs`` (après avoir retiré une valeur du
domaine d'une variable), d'autant plus que la contrainte ``NotEqual`` ne peut
avoir un effet que si une des variables est fixée. 

Modifiez l'algorithme du point fixe pour n'effectuer la propagation que pour les
contraintes liées à la variable dont le domaine vient d'être modifié, et
uniquement si cette variable est fixée. Testez l'effet de cette modification sur
la recherche (temps, nombre d'appels récursifs de ``dfs``, ...) pour le problème
des n dames pour :math:`n = 12`.

Optimisation 4
--------------

Dans l'implémentation actuelle du solveur de contraintes, la sauvegarde et la
restauration des domaines sont de complexité :math:`O(n)` où :math:`n` est la
taille du domaine. Il est possible, en utilisant une représentation plus
efficace des domaines, de réduire la complexité de ces opérations à
:math:`O(1)`.

Deux alternatives sont possibles pour cela :

- Utiliser une représentation binaire des domaines, où chaque valeur du domaine
  est représentée par un bit dans un entier. La sauvegarde et la restauration
  des domaines peuvent alors être effectuées en copiant simplement l'entier
  représentant le domaine. Pour des petits domaines (par exemple, des domaines
  de taille inférieure à 32), cette approche peut être très efficace.

- Utiliser des SparseSets (cf. partie 3 du cours)


Optimisation 5
--------------

Dans l'implémentation actuelle du solveur de contraintes, le backup et la
restauration des domaines sont effectués pour toutes les variables du problème,
même si seules quelques-unes d'entre elles sont modifiées lors de l'exploration
d'une branche du ``dfs``.

Modifiez le solveur pour tenir une trace des variables dont les domaines ont été
modifiés lors de l'exploration d'une branche du ``dfs`` et ne faire le backup et
la restauration que pour ces variables. Testez l'effet de cette modification sur
la recherche (temps, nombre d'appels récursifs de ``dfs``, ...) pour le problème
des n dames pour :math:`n = 12`.

..  warning:: 

    Cette tâche peut se révéler beaucoup plus complexe qu'il n'y paraît au
    premier abord, notamment en raison de la nécessité de gérer correctement les
    modifications des domaines et les propagations associées. Il est recommandé
    de bien planifier l'implémentation avant de se lancer dans le code, et de
    tester soigneusement chaque étape pour s'assurer que le solveur fonctionne
    correctement après la modification.

Optimisation des domaines entiers par des nombres binaires
==========================================================

Il existe une manière très efficace de représenter des ensembles de nombres
entiers compris entre 0 et :math:`n-1` (inclus) à l'aide de nombres binaires de
:math:`n` bits. Par exemple, pour :math:`n=5`, on peut représenter l'ensemble
:math:`\{0, 2, 4\}` par le nombre binaire :math:`10101` (en base 10, c'est le
nombre 21).

Exercice 1
----------

..  shortanswer:: bitwise_set_representation_question_01

    Commencez par déterminer la représentation binaire des ensembles suivants:

    1. :math:`\{0, 2, 4\}`
    2. :math:`\{1, 3\}`
    3. :math:`\emptyset` (l'ensemble vide)
    4. :math:`\{0, 1, 2, 3, 4\}` (l'ensemble de tous les éléments)

..  reveal:: b5d75b65-b352-494d-9d51-35a8e7d26000
    :showtitle: Réponse

    1. :math:`\{0, 2, 4\}` est représenté par le nombre binaire :math:`10101` (en base 10, c'est le nombre 21).
    2. :math:`\{1, 3\}` est représenté par le nombre binaire :math:`01010` (en base 10, c'est le nombre 10).
    3. :math:`\emptyset` (l'ensemble vide) est représenté par le nombre binaire :math:`00000` (en base 10, c'est le nombre 0).
    4. :math:`\{0, 1, 2, 3, 4\}` (l'ensemble de tous les éléments) est
       représenté par le nombre binaire :math:`11111` (en base 10, c'est le
       nombre 31).

Exercice 2
----------

Développez une fonction ``add_element(s: int, element: int) -> int`` qui prend
en paramètre un nombre binaire ``s`` représentant un ensemble d'entiers et un
entier ``element`` à ajouter à cet ensemble. La fonction doit retourner un
nombre binaire représentant l'ensemble obtenu après l'ajout de l'élément.

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_add_element.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def add_element(s: BitSet, element: int) -> BitSet:
        ''' 
        
        Retourne un nombre binaire représentant l'ensemble obtenu après l'ajout
        de l'élément
        
        >>> add_element(0b10101, 1) == 0b10111
        True
        >>> add_element(0b10101, 2) == 0b10101
        True
        >>> add_element(0b10101, 3) == 0b11101
        True
        
        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_add_element_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise OR
    (``|``) pour ajouter l'élément à l'ensemble représenté par le nombre
    binaire. Voici une solution:

    ..  activecode:: a3328a41-5028-495d-9742-e3c1f50b84f3
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def add_element(s: BitSet, element: int) -> BitSet:
            ''' 
            
            Retourne un nombre binaire représentant l'ensemble obtenu après l'ajout
            de l'élément
            
            >>> add_element(0b10101, 1) == 0b10111
            True
            >>> add_element(0b10101, 2) == 0b10101
            True
            >>> add_element(0b10101, 3) == 0b11101
            True
            
            '''
            return s | (1 << element)

        if __name__ == '__main__':
            import doctest
            doctest.testmod()

Exercice 3
----------

Développez une fonction ``union(s1: BitSet, s2: BitSet) -> BitSet`` qui
prend en paramètre deux nombres binaires ``s1`` et ``s2`` représentant des
ensembles d entiers et qui retourne un nombre binaire représentant l'union de
ces deux ensembles.

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_union.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def union(s1: BitSet, s2: BitSet) -> BitSet:
        ''' 
        
        Retourne un nombre binaire représentant l'union de ces deux ensembles
        
        >>> union(0b10101, 0b01010) == 0b11111
        True
        >>> union(0b10101, 0b00100) == 0b10101
        True
        >>> union(0b10101, 0b00000) == 0b10101
        True

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_union_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise OR
    (``|``) pour calculer l'union des deux ensembles représentés par les nombres
    binaires. Voici la solution:

    ..  activecode:: 4bee3b74-714c-4109-8e29-5f280c9110ca
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def union(s1: BitSet, s2: BitSet) -> BitSet:
            ''' 
            
            Retourne un nombre binaire représentant l'union de ces deux ensembles
            
            >>> union(0b10101, 0b01010) == 0b11111
            True
            >>> union(0b10101, 0b00100) == 0b10101
            True
            >>> union(0b10101, 0b00000) == 0b10101
            True

            '''
            return s1 | s2

Exercice 4
----------

Développez une fonction ``intersection(s1: BitSet, s2: BitSet) -> BitSet``
qui prend en paramètre deux nombres binaires ``s1`` et ``s2`` représentant des
ensembles d entiers et qui retourne un nombre binaire représentant
l'intersection de ces deux ensembles.

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_intersection.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def intersection(s1: BitSet, s2: BitSet) -> BitSet:
        ''' 
        
        Retourne un nombre binaire représentant l'intersection de ces deux
        ensembles
        
        >>> intersection(0b10101, 0b01010) == 0b00000
        True
        >>> intersection(0b10101, 0b00100) == 0b00100
        True
        >>> intersection(0b10101, 0b00000) == 0b00000
        True

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_intersection_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise AND
    (``&``) pour calculer l'intersection des deux ensembles représentés par les
    nombres binaires. Voici la solution:

    ..  activecode:: fd23c785-7660-4af5-ae27-92dee287384c
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def intersection(s1: BitSet, s2: BitSet) -> BitSet:
            ''' 
            
            Retourne un nombre binaire représentant l'intersection de ces deux
            ensembles
            
            >>> intersection(0b10101, 0b01010) == 0b00000
            True
            >>> intersection(0b10101, 0b00100) == 0b00100
            True
            >>> intersection(0b10101, 0b00000) == 0b00000
            True

            '''
            return s1 & s2


Exercice 5
----------

Développez une fonction ``difference(s1: BitSet, s2: BitSet) -> BitSet`` qui
prend en paramètre deux nombres binaires ``s1`` et ``s2`` représentant des
ensembles d'entiers et qui retourne un nombre binaire représentant la différence
de ces deux ensembles (c'est à dire les éléments qui sont dans ``s1`` mais pas
dans ``s2``).

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_difference.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def difference(s1: BitSet, s2: BitSet) -> BitSet:
        ''' 
        
        Retourne un nombre binaire représentant la différence de ces deux
        ensembles
        
        >>> difference(0b10101, 0b01010) == 0b10101
        True
        >>> difference(0b10101, 0b00100) == 0b10001
        True
        >>> difference(0b10101, 0b10101) == 0b00000
        True
        >>> difference(0b11111, 0b10101) == 0b01010
        True
        >>> difference(0b10101, 0b00000) == 0b10101
        True

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_difference_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise AND
    (``&``) avec le complément de ``s2`` pour calculer la différence des deux
    ensembles représentés par les nombres binaires. Voici la solution:

    ..  activecode:: cdf359d6-eee9-4c1a-a889-2101fd1b1e1c
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def difference(s1: BitSet, s2: BitSet) -> BitSet:
            ''' 
            
            Retourne un nombre binaire représentant la différence de ces deux
            ensembles
            
            >>> difference(0b10101, 0b01010) == 0b10101
            True
            >>> difference(0b10101, 0b00100) == 0b10001
            True
            >>> difference(0b10101, 0b10101) == 0b00000
            True
            >>> difference(0b11111, 0b10101) == 0b01010
            True
            >>> difference(0b10101, 0b00000) == 0b10101
            True

            '''
            return s1 & ~s2

Exercice 6
----------

Développez une fonction ``remove_element(s: BitSet, element: int) -> BitSet``
qui prend en paramètre un nombre binaire ``s`` représentant un ensemble
d'entiers et un entier ``element`` à retirer de cet ensemble. La fonction doit
retourner un nombre binaire représentant l'ensemble obtenu après le retrait de
l'élément.

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

    Si l'élément à retirer n'est pas dans l'ensemble, la fonction doit lever une
    exception de type ``ValueError`` avec le message "Element {element} is not
    in the set represented by {s}".

..  activecode:: bitwise_set_remove_element.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def remove_element(s: BitSet, element: int) -> BitSet:
        ''' 
        
        Retourne un nombre binaire représentant l'ensemble obtenu après le
        retrait de l'élément
        
        >>> remove_element(0b10101, 0) == 0b10100
        True
        >>> remove_element(0b10101, 2) == 0b10001
        True
        >>> remove_element(0b10101, 3)
        Traceback (most recent call last):
        ...
        ValueError: Element 3 is not in the set represented by 0b10101

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_remove_element_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise AND
    (``&``) avec le complément de l'élément à retirer pour supprimer l'élément
    de l'ensemble représenté par le nombre binaire. Voici la solution:

    ..  activecode:: 1e81d1f9-0b6b-4980-bdfa-1e8418779a16
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def remove_element(s: BitSet, element: int) -> BitSet:
            ''' 
            
            Retourne un nombre binaire représentant l'ensemble obtenu après le
            retrait de l'élément
            
            >>> remove_element(0b10101, 0) == 0b10100
            True
            >>> remove_element(0b10101, 2) == 0b10001
            True
            >>> remove_element(0b10101, 3)
            Traceback (most recent call last):
            ...
            ValueError: Element 3 is not in the set represented by 0b10101

            '''
            if not (s & (1 << element)):
                raise ValueError(f"Element {element} is not in the set represented by {s:#b}")
            return s & ~(1 << element)

        if __name__ == '__main__':
            import doctest
            doctest.testmod()

Exercice 7
----------

Développez une fonction ``has_element(s: int, element: int) -> bool`` qui prend
en paramètre un nombre binaire ``s`` représentant un ensemble d'entiers et un
entier ``element`` à vérifier. La fonction doit retourner ``True`` si l'élément
est dans l'ensemble représenté par ``s``, et ``False`` sinon.

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_has_element.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def has_element(s: BitSet, element: int) -> bool:
        ''' 
        
        Retourne True si l'élément est dans l'ensemble représenté par s, et
        False sinon
        
        >>> has_element(0b10101, 0)
        True
        >>> has_element(0b10101, 1)
        False
        >>> has_element(0b10101, 2)
        True
        >>> has_element(0b10101, 3)
        False
        >>> has_element(0b10101, 4)
        True

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_has_element_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise AND
    (``&``) pour vérifier si l'élément est dans l'ensemble représenté par le
    nombre binaire. Voici la solution:

    ..  activecode:: 236fc0c3-cd47-4bed-9131-9dc49e799457
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def has_element(s: BitSet, element: int) -> bool:
            ''' 
            
            Retourne True si l'élément est dans l'ensemble représenté par s, et
            False sinon
            
            >>> has_element(0b10101, 0)
            True
            >>> has_element(0b10101, 1)
            False
            >>> has_element(0b10101, 2)
            True
            >>> has_element(0b10101, 3)
            False
            >>> has_element(0b10101, 4)
            True

            '''
            return (s & (1 << element)) != 0

        if __name__ == '__main__':
            import doctest
            doctest.testmod()        

Exercice 8
----------

Développez une fonction ``set_min(s: BitSet) -> int`` qui prend en paramètre un
nombre binaire ``s`` représentant un ensemble d'entiers et qui retourne le plus
petit élément de cet ensemble. Si l'ensemble est vide, la fonction doit lever
une exception de type ``ValueError`` avec le message "Cannot get the minimum of
an empty set".

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_min.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def set_min(s: BitSet) -> int:
        ''' 
        
        Retourne le plus petit élément de l'ensemble représenté par s
        
        >>> set_min(0b10101)
        0
        >>> set_min(0b01010)
        1
        >>> set_min(0b00000)
        Traceback (most recent call last):
        ...
        ValueError: Cannot get the minimum of an empty set

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_min_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise AND
    (``&``) avec le complément de ``s`` pour trouver le plus petit élément dans
    l'ensemble représenté par le nombre binaire. Voici la solution:

    ..  activecode:: 1f96778d-fa8f-4a87-9f74-a3a9a269bed1
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def set_min(s: BitSet) -> int:
            ''' 
            
            Retourne le plus petit élément de l'ensemble représenté par s
            
            >>> set_min(0b10101)
            0
            >>> set_min(0b01010)
            1
            >>> set_min(0b00000)
            Traceback (most recent call last):
            ...
            ValueError: Cannot get the minimum of an empty set

            '''
            if s == 0:
                raise ValueError(f"Cannot get the minimum of an empty set")
            return (s & -s).bit_length() - 1


Exercice 9
----------

Développez une fonction ``set_max(s: BitSet) -> int`` qui prend en paramètre un
nombre binaire ``s`` représentant un ensemble d'entiers et qui retourne le plus
grand élément de cet ensemble. Si l'ensemble est vide, la fonction doit lever
une exception de type ``ValueError`` avec le message "Cannot get the maximum of
an empty set".

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_max.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def set_max(s: BitSet) -> int:
        ''' 
        
        Retourne le plus grand élément de l'ensemble représenté par s
        
        >>> set_max(0b10101) # plus grand élément de {0, 2, 4}
        4
        >>> set_max(0b01010) # plus grand élément de {1, 3}
        3
        >>> set_max(0b00000) # plus grand élément de l'ensemble vide
        Traceback (most recent call last):
        ...
        ValueError: Cannot get the maximum of an empty set

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_max_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant l'opérateur de bitwise AND
    (``&``) avec le complément de ``s`` pour trouver le plus grand élément dans
    l'ensemble représenté par le nombre binaire. Voici la solution:

    ..  activecode:: bff98335-fbac-4f2d-a947-18588c841218
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def set_max(s: BitSet) -> int:
            ''' 
            
            Retourne le plus grand élément de l'ensemble représenté par s
            
            >>> set_max(0b10101) # plus grand élément de {0, 2, 4}
            4
            >>> set_max(0b01010) # plus grand élément de {1, 3}
            3
            >>> set_max(0b00000) # plus grand élément de l'ensemble vide
            Traceback (most recent call last):
            ...
            ValueError: Cannot get the maximum of an empty set

            '''
            if s == 0:
                raise ValueError(f"Cannot get the maximum of an empty set")
            return s.bit_length() - 1

Exercice 10
-----------

Développez une fonction ``set_size(s: BitSet) -> int`` qui prend en paramètre un
nombre binaire ``s`` représentant un ensemble d'entiers et qui retourne le
nombre d'éléments dans cet ensemble.

..  note:: 

    La fonction doit être très efficace et ne doit pas utiliser de boucle ni de
    conditionnelle. Elle doit faire le travail en une seule ligne de code, en
    utilisant les opérateurs sur les bits.

..  activecode:: bitwise_set_size.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def set_size(s: BitSet) -> int:
        ''' 
        
        Retourne le nombre d'éléments dans l'ensemble représenté par s
        
        >>> set_size(0b10101) # nombre d'éléments dans {0, 2, 4}
        3
        >>> set_size(0b01010) # nombre d'éléments dans {1, 3}
        2
        >>> set_size(0b00000) # nombre d'éléments dans l'ensemble vide
        0

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_size_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant la méthode ``bit_count()`` de
    Python pour compter le nombre de bits à 1 dans le nombre binaire. Voici la
    solution:

    ..  activecode:: 4734197a-ddfe-4ac6-9ec8-ec47b12acff2
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def set_size(s: BitSet) -> int:
            ''' 
            
            Retourne le nombre d'éléments dans l'ensemble représenté par s
            
            >>> set_size(0b10101) # nombre d'éléments dans {0, 2, 4}
            3
            >>> set_size(0b01010) # nombre d'éléments dans {1, 3}
            2
            >>> set_size(0b00000) # nombre d'éléments dans l'ensemble vide
            0

            '''
            return s.bit_count()

Exercice 11
-----------

Développez une fonction ``create_bitset(elements: Iterable[int]) -> BitSet`` qui
prend en paramètre un itérable d'entiers et qui retourne un nombre binaire
représentant l'ensemble de ces éléments.

..  note:: 

    La fonction doit être le plus efficace possible et doit utiliser les
    fonctions précédemment définies pour construire le nombre binaire
    représentant l'ensemble des éléments.

..  activecode:: bitwise_set_create_bitset.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    from typing import Iterable

    type BitSet = int

    def create_bitset(elements: Iterable[int]) -> BitSet:
        ''' 
        
        Retourne un nombre binaire représentant l'ensemble des éléments
        
        >>> create_bitset([0, 2, 2, 4]) == 0b10101
        True
        >>> create_bitset({1, 3}) == 0b01010
        True
        >>> create_bitset(set()) == 0b00000
        True
        >>> create_bitset({0, 1, 2, 3, 4}) == 0b11111
        True

        '''
        ...

    ..  reveal:: bitwise_set_create_bitset_solution
        :showtitle: Solution
        :hidetitle: Cacher
        :instructoronly:

        from typing import Iterable

        type BitSet = int

        def add_element(s: BitSet, element: int) -> BitSet:
            return s | (1 << element)

        def create_bitset(elements: Iterable[int]) -> BitSet:
            ''' 
            
            Retourne un nombre binaire représentant l'ensemble des éléments
            
            >>> create_bitset([0, 2, 2, 4]) == 0b10101
            True
            >>> create_bitset({1, 3}) == 0b01010
            True
            >>> create_bitset(set()) == 0b00000
            True
            >>> create_bitset({0, 1, 2, 3, 4}) == 0b11111
            True

            '''
            s: BitSet = 0
            for element in elements:
                s = add_element(s, element)
            return s

Exercice 12
-----------

Créez une fonction ``bitset_to_list(s: BitSet) -> list[int]`` qui prend en
paramètre un nombre binaire ``s`` représentant un ensemble d'entiers et qui
retourne une liste ordonnée des éléments de cet ensemble.

..  note:: 

    La fonction doit être le plus efficace possible et doit utiliser les
    fonctions précédemment définies pour construire la liste des éléments de
    l'ensemble représenté par le nombre binaire.

..  activecode:: bitwise_set_to_list.py
    :language: webtp
    :interpreterargs: layout=["Editor", "Console"]

    type BitSet = int

    def bitset_to_list(s: BitSet) -> list[int]:
        ''' 
        
        Retourne une liste ordonnée des éléments de l'ensemble représenté par s
        
        >>> bitset_to_list(0b10101)
        [0, 2, 4]
        >>> bitset_to_list(0b01010)
        [1, 3]
        >>> bitset_to_list(0b00000)
        []
        >>> bitset_to_list(0b11111)
        [0, 1, 2, 3, 4]

        '''
        ...

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

..  reveal:: bitwise_set_to_list_solution
    :showtitle: Solution
    :hidetitle: Cacher
    :instructoronly:

    La fonction peut être implémentée en utilisant une boucle pour parcourir les
    bits du nombre binaire et ajouter les éléments correspondants à la liste
    des éléments de l'ensemble. Voici la solution:

    ..  activecode:: 9ac06bab-3b4a-4342-b445-8650a9cec2a6
        :language: webtp
        :interpreterargs: layout=["Editor", "Console"]

        type BitSet = int

        def has_element(s: BitSet, element: int) -> bool:
            return (s & (1 << element)) != 0

        def bitset_to_list(s: BitSet) -> list[int]:
            ''' 
            
            Retourne une liste ordonnée des éléments de l'ensemble représenté par s
            
            >>> bitset_to_list(0b10101)
            [0, 2, 4]
            >>> bitset_to_list(0b01010)
            [1, 3]
            >>> bitset_to_list(0b00000)
            []
            >>> bitset_to_list(0b11111)
            [0, 1, 2, 3, 4]

            ''' 
            
            n = s.bit_length()
            return [i for i in range(n) if has_element(s, i)]

