.. _benchmarking.rst:

Comparatif d'efficacité du solveur ``ToyCSP`` pour les :math:`n` dames
######################################################################

..  contents:: Contenu de la page
    :depth: 3

Comparatif entre les différentes approches
==========================================

Comparez les différentes approches de résolution du problème des n dames. Vous
pouvez trouver les codes dans le dépôt du cours
https://github.com/donnerc/pyminicp

- approche par DFS + filtrage : https://github.com/donnerc/pyminicp/blob/main/nqueens_dfs_filter.py
- approche par DFS + élagage : https://github.com/donnerc/pyminicp/blob/main/nqueens_dfs_prune.py
- approche avec le solveur de contraintes avec vérification avant :
  https://github.com/donnerc/pyminicp/blob/main/nqueens_short.py

#.  Pour chaque méthode, notez le temps d'exécution. Affichez le résultat au format
    CSV ou dans un autre format que vous jugerez approprié.

..  activecode:: benchmarking-compare
    :language: webtp

    ######################## Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_dfs_filter.py'
    with open('nqueens_filter.py', 'w') as fd: fd.write(open_url(url).read())
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_dfs_prune.py'
    with open('nqueens_prune.py', 'w') as fd: fd.write(open_url(url).read())
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_short.py'
    with open('nqueens_cp.py', 'w') as fd: fd.write(open_url(url).read())
    ############################################################

    from nqueens_filter import nqueens_solver as filter_solver
    from nqueens_prune import nqueens_solver as prune_solver
    from nqueens_cp import nqueens_solver as cp_solver

    from time import time

    t0 = time()
    solutions = cp_solver(n=8)
    print(f"Nombre de solutions {len(solutions) = }")
    t1 = time()

    print(f"temps = {(t1 - t0) * 1000} ms")


Conclusions
===========

..  shortanswer:: 06708064-e11a-4b11-8055-715eae9334ad

    Quelles conclusions tirez-vous de la comparaison entre les trois approches?

    - Le solveur ``ToyCSP`` avec la vérification avant est-il plus efficace que
      les deux autres méthodes plus basiques?

    - Citez les avantages de l'approche par programmation par contraintes par
      rapport aux autres approches


..  reveal:: 3de8e451-4899-4002-83c5-237ae6bc64ea
    :showtitle: Réponse

    On constate que le solveur ToyCSP est plus lent que l'approche DFS + élagage
    et que le DFS avec filtrage est horriblement lent.
    
    
    ..  note::
        
        Ceci mérite réflexion, car l'arbre de recherche est le plus optimisé avec l'approche utilisée par
        ToyCSP (utilisant le forward-checking).

    ..  admonition:: Avantages de la programmation par contraintes

        - Approche générale permettant de séparer formulation du problème et
          recherche de solutions

        - Pas besoin de coder des algorithmes spécifiques (ces derniers sont
          cachés dans les algorithmes de propagation / filtrage des contraintes)

        - Permet de tester facilement différentes stratégies de résolution
          indépendamment du problème

        - Permet de modifier facilement le problème (modélisation)

    Voici un tableau comparatif des temps d'exécution pour :math:`n` allant de 4
    à 12. Les mesures n'ont pas été effectuées pour le DFS + filtrage pour
    :math:`n > 8`, car il est clair que cette approche est trop lente.

    ..  csv-table:: Comparatif des différents solveurs
        :header-rows: 1

        n,temps DFS + filtrage[ms],temps DFS + élagage [ms],temps ToyCSP [ms]
        4,0.0,0.0,2.0
        5,6.0,1.0,5.0
        6,44.0,1.0,9.0
        7,712.0,4.0,37.0
        8,22574.0,22.0,409.0
        9,,123.0,1828.0
        10,,583.0,9077.0
        11,,3634.0,14109.0
        12,,6649.0,84866.0

    Représentation graphique des résultats:

    ..  raw:: html

        <iframe 
            src="https://www.desmos.com/calculator/9op0y4poip?embed" 
            width="100%" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

    Le programme suivant effectue les mesures et les affiche avec le module
    ``matplotlib``. Le DFS avec filtrage est si lent qu'on ne prend les mesures
    que pour :math:`n \leq 8` et on remplace le temps par des valeurs négatives
    pour :math:`n > 8`.

    ..  activecode:: e6b0e98f-f96c-41b9-8d5b-d85ed68885c9
        :language: webtp

        ######################## Importation dans WebTigerPython ############
        from pyodide.http import open_url
        url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
        with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
        url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_dfs_filter.py'
        with open('nqueens_filter.py', 'w') as fd: fd.write(open_url(url).read())
        url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_dfs_prune.py'
        with open('nqueens_prune.py', 'w') as fd: fd.write(open_url(url).read())
        url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_short.py'
        with open('nqueens_cp.py', 'w') as fd: fd.write(open_url(url).read())
        ############################################################
        import matplotlib.pyplot as plt
        from time import time, sleep

        # importation de la résolution avec filtrage
        from nqueens_filter import nqueens_solver as filter_solver
        # importation de la résolution avec élagage
        from nqueens_prune import nqueens_solver as prune_solver
        # importation de la résolution par contraintes avec forward-checking
        from nqueens_cp import nqueens_solver as toycsp_solver


        def timit(solver, n):
            t0 = time()
            solutions = solver(n=n)
            t1 = time()
            time_ms = round((t1 - t0) * 1000, 2)

            return time_ms


        sizes = []
        dfs_filter_times = []
        dfs_prune_times = []
        toycsp_times = []

        print(f"{'n':10s}{'DFS+filtrage [ms]':>23s}{'DFS+élagage [ms]':>23s}{'ToyCSP [ms]':>23s}")
        for n in range(4, 12):
            sizes.append(n)

            if n < 9:
                dfs_filter_ms = timit(filter_solver, n)
                dfs_filter_times.append(dfs_filter_ms)
                dfs_filter_ms = f'{dfs_filter_ms:>23.2f}'
            else:
                dfs_filter_ms = f'{'-':>23s}'

            dfs_prune_ms = timit(prune_solver, n)
            dfs_prune_times.append(dfs_prune_ms)

            toycsp_ms = timit(toycsp_solver, n)
            toycsp_times.append(toycsp_ms)

            print(f"{n:<10d}{dfs_filter_ms}{dfs_prune_ms:>23.2f}{toycsp_ms:>23.2f}")
            sleep(0.1)


        fig, ax = plt.subplots()
        ax.scatter(sizes[:5], dfs_filter_times[:5], label="DFS+filter")
        ax.scatter(sizes, dfs_prune_times, label="DFS+prune")
        ax.scatter(sizes, toycsp_times, label="ToyCSP")
        ax.set_xlabel("Board size n")
        ax.set_ylabel("Time [ms]")
        ax.set_title("Comparison between the three approaches")
        ax.legend()
        ax.grid(True)
        plt.show()

..  shortanswer:: toycsp_profiling_question

    Déterminez les parties du code qui occupent la plupart du temps processeur
    et qu'il vaudrait la peine d'optimiser.

Profiling du programme
======================

Le programme ci-dessous permet de faire du **profiling** de notre solveur, pour
obtenir des statistiques très précieuses sur le nombre de fois que chaque
fonction / méthode est appelée et le temps passé dans chaque fonction.

..  activecode:: nqueens_toycsp_profiling
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

    def nqueens(n: int) -> list[list[int]]:
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

        return solutions

    ########### Profiling ##############

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