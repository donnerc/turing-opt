.. _part3-turingcp.rst:

TuringCP
########

..  contents:: Contenu de la page
    :depth: 3

Nous allons développer un solveur plus complexe et flexible que nous appellerons
``TuringCP``, où CP = Constraint Programming. Ce solveur intègre les différentes
structures de données que nous avons développées spécialement, ainsi que
d'autres éléments qui augmentent sa flexibilité.

Exemple : n dames
=================

Voici un exemple d'utilisation du solveur ``TuringCP`` que nous allons étudier
pour terminer le cours. 

..  note::

    Pour le moment, le programme se plante avec une ``InconsistencyException``
    sur cette page, car le code n'a pas été testé sur Pyodide. Il s'exécute
    toutefois correctement dans un environnement Python standard...

..  activecode:: turingcp_nqueens
    :language: webtp

    ############### Importation dans WebTigerPython ############
    from pyodide.http import open_url

    def load_external_files(files: list[str]) -> None:
        prefix = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/turingcp/'
        for file in files:
            module = file.split('/')[-1]
            with open(module, 'w') as fd: fd.write(open_url(prefix + file).read())

    load_external_files([
        'stack.py',
        'constraint.py',
        'cp_types.py',
        'domain.py',
        'linked_queue.py',
        'modeling.py',
        'search.py',
        'solver.py',
        'stack.py',
        'state.py',
        'state_sparse_set.py',
        'state_stack.py',
        'state_types.py',
        'util_types.py',
        'utils.py',
        'variable.py',
    ])
    ############################################################

    from modeling import *

    from search import DFSearch
    from constraint import NotEqual, Equal

    type NQueensSolution = list[int]

    def nqueens(n: int = 8) -> list[NQueensSolution]:
        solutions: NQueensSolution = []

        # variables
        q = [int_var(range(0, n)) for _ in range(n)]

        # constraints
        for i in range(0, n):
            for j in range(i + 1, n):
                post(NotEqual(q[i], q[j], 0))
                post(NotEqual(q[i], q[j], i - j))
                post(NotEqual(q[i], q[j], j - i))

        # solving
        dfs: DFSearch = make_search()

        @dfs.on("solution")
        def handle_solution(dfs, infos):
            solutions.append(get_values(q))

        ''' remove this comment to define a custom branching strategy
        @dfs.branching_strategy
        def branching():
            def left():
                post(Equal(var, int_const(v)))

            def right():
                post(NotEqual(var, int_const(v)))

            # next variable choice
            for var in q:
                if not var.is_fixed():
                    break
            else:
                return []

            # next value choice
            v: int = var.min()

            return [left, right]
        '''

        dfs.solve()

        return solutions

Remarques
---------

La modéalisation n'est pas très différente de ce que nous avions dans
``ToyCSP``. Les principes restent les mêmes, mais avec plus de flexibilité dans
la spécification de la procédure de recherche (stratégie de branchement)
permettant de déterminer l'arbre de recherche.

..
    Solveur
    =======

    ..  activecode:: turingcp_solver
        :language: webtp

    Stack
    =====

    ..  activecode:: turingcp_stack
        :language: webtp


    Copier
    ------

    ..  activecode:: turingcp_copier
        :language: webtp

    Contraintes
    ===========


    StateManager
    ============

    ..  activecode:: turingcp_statemanager
        :language: webtp