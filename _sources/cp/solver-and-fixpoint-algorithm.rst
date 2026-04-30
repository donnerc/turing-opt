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
    :interpreterargs: branch=branch

    ######################## Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/nqueens_turtle_visu.py'
    with open('nqueens_visu.py', 'w') as fd: fd.write(open_url(url).read())
    ############################################################

    from toycsp import Variable, Domain, Inconsistency, Constraint, NotEqual

    from collections.abc import Iterable
    from abc import ABC, abstractmethod
    from typing import Optional, Any, Callable, override, cast

    type PartialSolution = list[int | None]
    type Solution = list[int]



    class ToyCSP:
        """
        Class representing a Tiny Constraint Satisfaction Problem (TCSP).
        """

        def __init__(self, *args, **kwargs):

            self.constraints: list[Constraint] = []
            self.variables: list[Variable] = []
            self.n_recur: int = 0  # Number of recursive calls

            # collects all handlers (args beginning with `on_`)
            self.handlers = {
                arg.split('on_')[1]: [value] for arg, value in kwargs.items() if arg.startswith("on_")
            }

        def __repr__(self) -> str:
            # return f"ToyCSP(constraints={self.constraints}, variables={self.variables})"
            return f"ToyCSP : #vars = {len(self.variables)} / #constraints = {len(self.constraints)}"

        def add_variable(self, domain: Iterable[int], name: str | None = None) -> Variable:
            """
            Creates a variable with the given domain.

            Args:
                domain: An iterable of integers representing the domain values.

            Returns:
                A new Variable object.
            """
            var = Variable(domain, name)
            self.variables.append(var)
            return var

        def post(self, constraint: Constraint, schedule_fixpoint=True) -> Constraint:
            """
            Posts (adds) a constraint to the CSP and optionally schedules a fix point.

            Args:
                constraint: The constraint to add.
                schedule_fixpoint: If True, schedules a fix point after adding the constraint.

            Returns:
                The added constraint.
            """
            self.constraints.append(constraint)
            if schedule_fixpoint:
                self.fix_point()
            return constraint

        def backup_domains(self) -> list[Domain]:
            """
            Creates a backup copy of all variable domains.

            Returns:
                A list of Domain objects representing the backed-up domains.
            """
            backup = [var.dom.clone() for var in self.variables]
            return backup

        def restore_domains(self, backup: list[Domain]) -> None:
            """
            Restores the domains of all variables from the backup.

            Args:
                backup: A list of Domain objects representing the backed-up domains.
            """
            for i, var in enumerate(self.variables):
                var.dom = backup[i]

        def get_partial_solution(self) -> PartialSolution:
            """
            Returns the current partial solution as a list of variable values or None for unfixed variables.

            Returns:
                A list of integers or None representing the current partial solution.
            """
            return [cast(Optional[int], var.value()) for var in self.variables]

        def get_solution(self) -> Solution:
            """
            Returns the current solution as a list of variable values.

            Raises a ValueError if not all variables are fixed.

            Returns:
                A list of integers representing the solution.
            """
            if not all(var.dom.is_fixed() for var in self.variables):
                raise ValueError(
                    "Not all variables are fixed. No solution available.")
            return [cast(int, v.value()) for v in self.variables]

        def first_not_fixed(self) -> Variable | None:
            """
            Finds the first variable that has a non-fixed domain.

            Returns:
                An Optional containing the first unfixed variable, or None if all are fixed.
            """
            # https://www.programiz.com/python-programming/methods/built-in/next
            return next((var for var in self.variables if not var.dom.is_fixed()), None)

        def smallest_not_fixed(self) -> Variable | None:
            """
            Finds the variable with the smallest domain size that is not fixed.

            Returns:
                An Optional containing the variable with the smallest domain, or None if all are fixed.
            """
            min_size = float("inf")
            smallest_var = None
            for var in self.variables:
                if not var.dom.is_fixed() and var.dom.size() < min_size:
                    min_size = var.dom.size()
                    smallest_var = var
            # return smallest_var if smallest_var else None
            return smallest_var

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
                    self.call_handlers(
                        "inconsistent", {"event": "inconsistent", "current_var": variable})

                # Restaurer les domaines avant d'explorer la branche droite
                self.restore_domains(backup)

                # Branche droite : retirer la valeur du domaine de la variable
                try:
                    variable.dom.remove(value)
                    self.fix_point()
                    self.dfs()
                except Inconsistency:
                    self.call_handlers(
                        "inconsistent", {"event": "inconsistent", "current_var": variable})

        ##############################################################################
        # Event handler registration and management

        def register_handler(self, event, handler) -> None:
            """Registers a handler function for a specific event."""
            if event in self.handlers:
                self.handlers[event].append(handler)
            else:
                self.handlers[event] = [handler]

        def call_handlers(self, event: str, infos: dict[str, Any]) -> None:
            """Calls all registered handlers for a specific event."""
            if event in self.handlers:
                handlers = self.handlers[event]
                for h in handlers:
                    h(self, infos)

        def on(self, *events):
            """Decorator to register a function as a handler for one or more events."""
            def decorator(func):
                for event in events:
                    self.register_handler(event, func)
            return decorator

        def no_op(self, csp: "ToyCSP", infos: dict[str, Any]) -> None:
            """A no-op handler that does nothing."""
            pass





    ########################### Modèle du problème des n dames #################################
    from nqueens_visu import draw_chess_board
    from gturtle import *

    # paramètre
    n = int(input("Taille du problème: "))

    csp: ToyCSP = ToyCSP()

    # variables de décision
    q: list[Variable] = [csp.add_variable(range(n), name=f'Q[{i}]') for i in range(n)]

    # Formulation des contraintes
    for i in range(n):
        for j in range(i + 1, n):
            csp.post(NotEqual(q[i], q[j], 0))
            csp.post(NotEqual(q[i], q[j], i - j))
            csp.post(NotEqual(q[i], q[j], j - i))


    # useless when using the debugger
    wait = True

    @csp.on('solution')
    def handle_solution(csp: ToyCSP, infos) -> None:
        clean()
        solutions.append(csp.get_solution())
        draw_chess_board(csp)
        if wait: c = getKeyWait()

    @csp.on('beforefixpoint', 'afterfixpoint', 'inconsistent', 'propagate')
    def handle_everything(csp: ToyCSP, infos) -> None:
        clean()
        setPos(-400, 300)
        event = infos.get('event')
        usefull = infos.get('usefull', '')
        constraint = infos.get('constraint', '')
        text = f'''
        Event : {event}
        Usefull : {usefull}
        Constraint : {str(constraint)}
        Infos : {infos}
        '''
        label(text)
        draw_chess_board(csp)
        print(str(infos), str(csp.variables))
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

..  reveal:: comprehension-toycsp-add-variable-reponse
    :showtitle: Explication de la méthode ``add_variable``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de la méthode ``add_variable``
    

    La méthode ``add_variable`` permet de créer facilement une variable de
    décision entière pour le problème de satisfaction de contraintes. Elle prend
    en entrée un domaine (une liste de valeurs possibles pour la variable) et un
    nom optionnel pour la variable. Elle crée un objet ``Variable`` avec ce
    domaine et ce nom, l'ajoute à la liste des variables du CSP, et retourne cet
    objet. Cette méthode est essentielle pour définir les variables qui seront
    utilisées dans les contraintes du problème.


Méthode ``post``
----------------

..  shortanswer:: comprehension-toycsp-post

    Expliquez précisément l'utilité de la méthode ``post`` ?

..  reveal:: comprehension-toycsp-post-reponse
    :showtitle: Explication de la méthode ``post``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de la méthode ``post``

    La méthode ``post`` permet d'ajouter une contrainte au CSP. Elle prend en
    entrée un objet ``Constraint`` et l'ajoute à la liste des contraintes du
    CSP. De plus, elle peut automatiquement déclencher une propagation des
    contraintes (fix point) après l'ajout de la contrainte, ce qui permet de
    réduire les domaines des variables dès que possible. Cette méthode est
    essentielle pour construire le modèle du problème en ajoutant les
    contraintes qui définissent les relations entre les variables.

Méthode ``backup_domains``
--------------------------

..  shortanswer:: comprehension-toycsp-backup-domains

    Expliquez précisément l'utilité de la méthode ``backup_domains`` ?

..  reveal:: comprehension-toycsp-backup-domains-reponse
    :showtitle: Explication de la méthode ``backup_domains``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de la méthode ``backup_domains``

    La méthode ``backup_domains`` permet de créer une copie de sauvegarde des
    domaines actuels de toutes les variables du CSP. Cela est particulièrement
    utile lors de la recherche (DFS) pour pouvoir restaurer les domaines à un
    état précédent après avoir exploré une branche de l'arbre de recherche. En
    cas d'inconsistance ou après avoir exploré une branche, on peut utiliser
    cette sauvegarde pour revenir à l'état précédent des domaines et continuer à
    explorer d'autres branches sans être affecté par les modifications faites
    dans la branche précédente.


Méthode ``restore_domains``
---------------------------

..  shortanswer:: comprehension-toycsp-restore-domains

    Expliquez précisément l'utilité de la méthode ``restore_domains`` ? Faites
    une recherche sur le fonction ``enumerate`` si vous ne savez pas ce qu'elle
    fait.

..  reveal:: comprehension-toycsp-restore-domains-reponse
    :showtitle: Explication de la méthode ``restore_domains``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de la méthode ``restore_domains``

    La méthode ``restore_domains`` permet de restaurer les domaines de toutes
    les variables à partir d'une sauvegarde créée précédemment avec la méthode
    ``backup_domains``. Elle prend en entrée une liste de domaines (la
    sauvegarde) et met à jour les domaines de toutes les variables du CSP en les
    remplaçant par les domaines sauvegardés. Cela est essentiel pour revenir à
    un état précédent des domaines après avoir exploré une branche de l'arbre de
    recherche, surtout en cas d'inconsistance ou après avoir terminé
    l'exploration d'une branche.

Méthode ``first_not_fixed``
---------------------------

..  shortanswer:: comprehension-toycsp-firstnotfixed

    Expliquez précisément l'utilité de la méthode ``first_not_fixed`` ? Son
    fonctionnement utilise une fonctionnalité très avancée de Python : une
    expression générateur. Cela fonctionne un peu comme une liste en
    compréhension, mais de manière plus efficace. 

    Utilisez une IA générative pour comprendre la ligne ::

        return next((var for var in self.variables if not var.dom.is_fixed()), None)

..  reveal:: comprehension-toycsp-firstnotfixed-reponse
    :showtitle: Explication de la méthode ``first_not_fixed``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de la méthode ``first_not_fixed``

    La méthode ``first_not_fixed`` permet de trouver la première variable du CSP
    qui n'est pas encore fixée (c'est-à-dire dont le domaine contient encore
    plusieurs valeurs). Elle utilise une expression générateur pour parcourir la
    liste des variables et retourne la première variable qui n'est pas fixée. Si
    toutes les variables sont fixées, elle retourne ``None``. Cette méthode est
    utile pour choisir une variable à assigner lors de la recherche (DFS).

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
    décorateur ``@on(<event>)``. La compréhension détaillée de ces méthodes
    n'est pas importante pour comprendre le fonctionnement général de la classe
    ``ToyCSP``.

    -   ``register_handler(self, event, handler) -> None``
    -   ``call_handlers(self, event: str, infos: dict[str, Any]) -> None``
    -   ``on(self, *events)``
    -   ``no_op(self, csp: "ToyCSP", infos: dict[str, Any]) -> None``

..  shortanswer:: comprehension-toycsp-bitwise-and

    Que fait l'opérateur ``&=``. Testez cet opérateur dans un REPL Python séparé
    (Thonny ou le terminal).

..  reveal:: comprehension-toycsp-bitwise-and-reponse
    :showtitle: Explication de l'opérateur ``&=``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de l'opérateur ``&=``

    L'opérateur ``&=`` est un opérateur de bitwise AND (ET binaire) combiné avec
    une affectation. Il prend la valeur actuelle de la variable à gauche de
    l'opérateur, effectue une opération AND bit à bit avec la valeur à droite de
    l'opérateur, et stocke le résultat dans la variable à gauche. Par exemple,
    si vous avez ``x = 5`` (qui est 0101 en binaire) et que vous faites ``x &=
    3`` (qui est 0011 en binaire), le résultat sera ``x = 1`` (0001 en binaire),
    car 0101 AND 0011 donne 0001.

    Ici, on utilise une variable booléenne ``fix`` qui est initialisée à
    ``True``. Si une propagation de contrainte est utile (c'est-à-dire qu'elle a
    réduit le domaine d'une variable), on met ``fix`` à ``False``. Si aucune
    propagation n'est utile, ``fix`` reste ``True``, ce qui signifie que nous
    avons atteint un point fixe.

..  shortanswer:: comprehension-toycsp-fixpoint

    Essayez d'expliquer son fonctionnement en rajoutant des commentaires dans le
    code si nécessaire et en décrivant précisément son fonctionnement.

..  reveal:: comprehension-toycsp-fixpoint-reponse
    :showtitle: Explication de la méthode ``fix_point``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de la méthode ``fix_point``

    La méthode ``fix_point`` implémente un algorithme de propagation des
    contraintes jusqu'à ce qu'un point fixe soit atteint. Elle commence par
    appeler les gestionnaires d'événts pour signaler le début du processus de
    fix point. Ensuite, elle utilise une boucle ``while`` qui continue tant que
    des changements sont effectués dans les domaines des variables. À chaque
    itération, elle parcourt toutes les contraintes du CSP et appelle leur
    méthode ``propagate()``. Si la propagation d'une contrainte est utile
    (c'est-à-dire qu'elle a réduit le domaine d'une variable), la variable
    ``fix`` est mise à ``False``, ce qui signifie que nous n'avons pas encore
    atteint un point fixe. Si aucune propagation n'est utile, ``fix`` reste
    ``True``, et la boucle se termine, indiquant que nous avons atteint un point
    fixe où aucune contrainte ne peut plus réduire les domaines des variables.
    Enfin, elle appelle les gestionnaires d'événements pour signaler la fin du
    processus de fix point.


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

..  reveal:: comprehension-toycsp-whynoindex-reponse
    :showtitle: Explication de l'absence de paramètre ``index`` dans la méthode ``dfs``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de l'absence de paramètre ``index`` dans la méthode ``dfs``

    La méthode ``dfs`` n'utilise pas de paramètre ``index`` pour suivre la
    position dans la liste des variables, car elle utilise une approche
    différente pour choisir la variable à assigner. Au lieu de parcourir les
    variables dans un ordre fixe (comme avec un index), elle utilise la méthode
    ``first_not_fixed`` pour trouver la première variable qui n'est pas encore
    fixée. Cela permet une plus grande flexibilité dans le choix de la variable
    à assigner, et peut être combiné avec d'autres heuristiques de sélection de
    variable (comme ``smallest_not_fixed``) sans avoir à gérer manuellement un
    index.


..  shortanswer:: comprehension-toycsp-backup-restore

    Pourquoi effectue-t-on les instructions suivantes et à quel moment de la
    recherche (parcours de l'arbre de recherche) ces opérations sont-elles
    exécutées.

    - ``backup = self.backup_domains()``

    - ``self.restore_domains(backup)``

..  reveal:: comprehension-toycsp-backup-restore-reponse
    :showtitle: Explication de l'utilisation de ``backup_domains`` et ``restore_domains``
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de l'utilisation de ``backup_domains`` et ``restore_domains``

    Les instructions ``backup = self.backup_domains()`` et
    ``self.restore_domains(backup)`` sont utilisées pour gérer les modifications
    des domaines des variables lors de l'exploration de l'arbre de recherche.
    Avant d'explorer une branche (par exemple, en fixant une variable à une
    valeur), on crée une sauvegarde des domaines actuels des variables avec
    ``backup_domains()``. Après avoir exploré cette branche (que ce soit la
    branche gauche ou la branche droite), on utilise ``restore_domains(backup)``
    pour revenir à l'état précédent des domaines avant d'explorer la prochaine
    branche. Cela permet de s'assurer que les modifications apportées aux
    domaines dans une branche n'affectent pas les autres branches de l'arbre de
    recherche.


..  shortanswer:: comprehension-toycsp-complete-search

    Comment peut-on être certain que la méthode ``dfs`` explore bien tout
    l'espace de recherche?

..  reveal:: comprehension-toycsp-complete-search-reponse
    :showtitle: Explication de l'exploration complète de l'espace de recherche
    :hidetitle: Cacher
    :modal:
    :modaltitle: Explication de l'exploration complète de l'espace de recherche

    La méthode ``dfs`` explore tout l'espace de recherche en utilisant une
    approche récursive qui tente toutes les valeurs possibles pour chaque
    variable non fixée. Grâce à l'utilisation de ``backup_domains`` et
    ``restore_domains``, chaque branche de l'arbre de recherche est explorée
    indépendamment, garantissant que toutes les combinaisons possibles de
    valeurs sont considérées.
