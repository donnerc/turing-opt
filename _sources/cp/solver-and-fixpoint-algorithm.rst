.. _solver-and-fixpoint-algorithm.rst:

Analyse du solveur sur le problème des :math:`n` dames
######################################################

..  contents:: Contenu de la page
    :depth: 3

Dans cette page, nous reprenons le problème des :math:`n` dames pour bien
comprendre le fonctionnement du solveur de contraintes


Visualisation
=============

La visualisation ci-dessous permet de comprendre le fonctionnement du solveur
``ToyCSP`` en visualisant la recherche de manière interactive.

..  activecode:: nqueens_cp_visu
    :language: webtp

    ######################## Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_turtle_visu.py'
    with open('nqueens_visu.py', 'w') as fd: fd.write(open_url(url).read())
    ############################################################

    from toycsp import Variable, Domain, Inconsistency, Constraint

    from collections.abc import Iterable
    from abc import ABC, abstractmethod
    from typing import List, Optional, Any, Callable

    class NotEqual(Constraint):
        """
        Constraint representing x != y + offset.
        """

        def __init__(self, x: Variable, y: Variable, offset: int = 0) -> None:
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


    class ToyCSP:
        """
        Class representing a Tiny Constraint Satisfaction Problem (TCSP).
        """

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
        
        ###############################################################

        def add_variable(self, domain: Iterable[int]) -> Variable:
            """
            Creates a variable with the given domain size.

            Args:
                dom_size: The number of values in the domain.

            Returns:
                A new Variable object.
            """
            var = Variable(domain)
            self.variables.append(var)
            return var

        def post(self, constraint: Constraint, schedule_fixpoint=True) -> Constraint:
            """
            Adds a not-equal constraint between two variables.

            Args:
                x: The first variable.
                y: The second variable.
                offset: The offset value. Defaults to 0.
            """
            self.constraints.append(constraint)
            if schedule_fixpoint:
                self.fix_point()

        def backup_domains(self) -> List[Domain]:
            """
            Creates a backup copy of all variable domains.

            Returns:
                A list of Domain objects representing the backed-up domains.
            """
            backup = [var.dom.clone() for var in self.variables]
            return backup

        def restore_domains(self, backup: List[Domain]) -> None:
            """
            Restores the domains of all variables from the backup.

            Args:
                backup: A list of Domain objects representing the backed-up domains.
            """
            for i, var in enumerate(self.variables):
                var.dom = backup[i]

        def get_solution(self) -> list[int]:
            return [v.value() for v in self.variables]

        def first_not_fixed(self) -> Optional[Variable]:
            """
            Finds the first variable that has a non-fixed domain.

            Returns:
                An Optional containing the first unfixed variable, or None if all are fixed.
            """
            # https://www.programiz.com/python-programming/methods/built-in/next
            return next((var for var in self.variables if not var.dom.is_fixed()), None)


        def fix_point(self) -> bool:
            """
            Performs constraint propagation until no further changes occur.

            Returns:
                True if a fix point is reached (no more changes), False otherwise.
            """
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

        def dfs(self, on_solution=None, on_fixpoint=None) -> None:
            """
            Performs Depth-First Search (DFS) to find all solutions to the CSP.

            Args:
                on_solution: A callback function that receives a solution (variable assignments).
            """
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

    ########################### Modèle du problème des n dames #################################
    from nqueens_visu import draw_chess_board
    from gturtle import *

    # paramètre
    n = int(input("Taille du problème: "))

    csp: ToyCSP = ToyCSP()

    # variables de décision
    q: list[Variable] = [csp.add_variable(range(n)) for _ in range(n)]

    # Formulation des contraintes
    for i in range(n):
        for j in range(i + 1, n):
            csp.post(NotEqual(q[i], q[j], 0))
            csp.post(NotEqual(q[i], q[j], i - j))
            csp.post(NotEqual(q[i], q[j], j - i))


    # useless when using the debugger
    wait = False

    @csp.on('solution')
    def handle_solution(csp: ToyCSP, infos) -> None:
        clean()
        solutions.append(csp.get_solution())
        draw_chess_board(csp)
        if wait: c = getKeyWait()

    @csp.on('beforefixpoint', 'afterfixpoint', 'inconsistency', 'propagate')
    def handle_everything(csp: ToyCSP, infos) -> None:
        clean()
        draw_chess_board(csp)
        print(infos, csp.variables)
        if wait: c = getKeyWait()


    solutions = []
    csp.dfs()

    print(f"{solutions = }")


Analyse du code
===============

Analysez le code de la classe ``ToyCSP`` à l'aide du débogueur intégré dans
WebTigerPython et répondez aux questions ci-dessous.

Utilisez le code ci-dessus pour analyser le fonctionnement de la classe
``ToyCSP``.

..  note::

    Mettez la variable ``wait`` à ``True`` si vous n'utilisez pas la débogueur,
    pour contrôler la résolution et à ``False`` si vous utilisez le débogueur.

Essayez d'expliquer le fonctionnement des méthodes importantes de la classe
``ToyCSP``


Méthode ``add_variable``
------------------------

..  shortanswer:: comprehension-toycsp-add-variable

    Expliquez précisément l'utilité de la méthode ``add_variable`` ?


Méthode ``post``
----------------

..  shortanswer:: comprehension-toycsp-post

    Expliquez précisément l'utilité de la méthode ``post`` ?

Méthode ``backup_domains``
--------------------------

..  shortanswer:: comprehension-toycsp-backup-domains

    Expliquez précisément l'utilité de la méthode ``backup_domains`` ?


Méthode ``restore_domains``
---------------------------

..  shortanswer:: comprehension-toycsp-restore-domains

    Expliquez précisément l'utilité de la méthode ``restore_domains`` ? Faites
    une recherche sur le fonction ``enumerate`` si vous ne savez pas ce qu'elle
    fait.

Méthode ``first_not_fixed``
---------------------------

..  shortanswer:: comprehension-toycsp-firstnotfixed

    Expliquez précisément l'utilité de la méthode ``first_not_fixed`` ? Son
    fonctionnement utilise une fonctionnalité très avancée de Python : une
    expression générateur. Cela fonctionne un peu comme une liste en
    compréhension, mais de manière plus efficace. 

    Utilisez une IA générative pour comprendre la ligne ::

        return next((var for var in self.variables if not var.dom.is_fixed()), None)

Méthode ``fixpoint``
--------------------

La méthode ``ToyCSP.fixpoint`` est cruciale pour la résolution du problème. Elle
permet essentiellement d'implémenter la **vérification avant** (*forward
checking*) consistant à supprimer de toutes les variables encore non assignées
(dont le domaine contient encore plusieurs valeurs) toutes les valeurs
incompatibles avec le placement de la dame qui vient d'être effectué.

Elle implémente un algorithme du "point fixe", car elle tourne jusqu'à ce
qu'elle ne produise plus aucun effet (qu'il n'y ait plus de valeurs à supprimer
dans les domaines des variables non assignées).

..  note::

    Dans un premier temps, n'essayez pas de comprendre les méthodes suivantes
    qui permettent d'implémenter le mécanisme de notification des événements de
    résolution (solution trouvée, inconsistence, propagation, application du
    point fixe, ...). Ces méthodes permettent notamment d'implémenter le
    mécanisme d'enregistrement de fonction de gestion des événements avec le
    décorateur ``@on(<event>)`` et utilisent des aspects de Python que vous ne
    connaissez probablement pas. La compréhension détaillée de ces méthodes
    n'est pas importante pour comprendre le fonctionnement général de la classe
    ``ToyCSP``.

    -   ``register_handler(self, event, handler) -> None``
    -   ``call_handlers(self, event: str, infos: dict[str, Any]) -> None``
    -   ``on(self, *events)``
    -   ``no_op(self, csp: "ToyCSP", infos: dict[str, Any]) -> None``

..  shortanswer:: comprehension-toycsp-bitwise-and

    Que fait l'opérateur ``&=``. Testez cet opérateur dans un REPL Python séparé
    (Thonny ou le terminal).

..  shortanswer:: comprehension-toycsp-fixpoint

    Essayez d'expliquer son fonctionnement en rajoutant des commentaires dans le
    code si nécessaire et en décrivant précisément son fonctionnement.


Méthode ``dfs``
---------------

La méthode ``dfs`` joue le même rôle que dans les autres approches vues jusqu'à
présent pour résoudre un problème par recherche exhaustive : explorer
systématiquement toutes les possibilités de l'espace de recherche.

Comparez-la aux fonctions ``dfs`` utilisées jusqu'à présent et expliquez les
différences suivantes:

..  shortanswer:: comprehension-toycsp-whynoindex

    Pourquoi la méthode ``dfs`` n'utilise-t-elle pas de paramètre ``index`` qui
    était essentiel dans les fonctions ``dfs`` utilisées dans les approches
    précédentes?


..  shortanswer:: comprehension-toycsp-backup-restore

    Pourquoi effectue-t-on les instructions suivantes et à quel moment de la
    recherche (parcours de l'arbre de recherche) ces opérations sont-elles
    exécutées.

    - ``backup = self.backup_domains()``

    - ``self.restore_domains(backup)``


..  shortanswer:: comprehension-toycsp-complete-search

    Comment peut-on être certain que la méthode ``dfs`` explore bien tout
    l'espace de recherche?

