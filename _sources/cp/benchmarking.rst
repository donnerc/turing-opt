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
    :interpreterargs: branch=branch&filesystemSize=20


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

    Le programme suivant effectue les mesures et les affiche avec le module
    ``matplotlib``. Le DFS avec filtrage est si lent qu'on ne prend les mesures
    que pour :math:`n \leq 8` et on remplace le temps par des valeurs négatives
    pour :math:`n > 8`.

    ..  activecode:: e6b0e98f-f96c-41b9-8d5b-d85ed68885c9
        :language: webtp
        :interpreterargs: branch=branch&filesystemSize=20

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

    Faites des hypothèses sur les parties du code qui occupent la plupart du
    temps processeur et qu'il vaudrait la peine d'optimiser. Discutez de vos
    hypothèses les autres.

Profiling du programme
======================

Le programme ci-dessous permet de faire du **profiling** de notre solveur, pour
obtenir des statistiques très précieuses sur le nombre de fois que chaque
fonction / méthode est appelée et le temps passé dans chaque fonction.

..  activecode:: nqueens_toycsp_profiling
    :language: webtp
    :interpreterargs: branch=branch&filesystemSize=20

    ######################## Importation dans WebTigerPython ############
    from pyodide.http import open_url
    url = 'https://raw.githubusercontent.com/donnerc/pyminicp/refs/heads/main/build/toycsp_bundle.py'
    with open('toycsp.py', 'w') as fd: fd.write(open_url(url).read())
    #####################################################################

    from toycsp import ToyCSP, Variable, NotEqual

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

Éléments à optimiser
====================

..  shortanswer:: toycsp_profiling_optimisation

    En vous basant sur les résultats du profiling, proposez des pistes
    d'optimisation du code. Vous pouvez aussi faire des hypothèses sur les
    parties du code qui sont les plus coûteuses en temps processeur et qui
    mériteraient d'être optimisées, même si elles n'apparaissent pas dans les
    premières lignes du profiling.

..  reveal:: toycsp_profiling_optimisation_reponse
    :showtitle: Réponse
    :hidetitle: Cacher

    D'après le profiling, les fonctions les plus coûteuses sont :
    
    - ``ToyCSP.dfs`` : c'est la fonction qui effectue la recherche en
      profondeur. Elle est appelée une seule fois, mais elle est très coûteuse
      en temps d'exécution.
    
    - ``ToyCSP.propagate`` : c'est la fonction qui effectue la propagation des
      contraintes. Elle est appelée de nombreuses fois (plus de 100 000 fois
      pour n=9) et elle est également très coûteuse en temps d'exécution.
    
    - ``ToyCSP.post`` : c'est la fonction qui permet de poster une contrainte
      dans le solveur. Elle est appelée de nombreuses fois (plus de 200 000 fois
      pour n=9) et elle est également coûteuse en temps d'exécution.
    
    - ``ToyCSP.get_solution`` : c'est la fonction qui permet d'obtenir la
      solution courante du solveur. Elle est appelée de nombreuses fois (plus de
      100 000 fois pour n=9) et elle est également coûteuse en temps
      d'exécution.
    
Principaux goulots d'étranglement
=================================

En analysant attentivement le code, on constate que les éléments suivants ne
sont pas efficaces et pourraient être optimisés :

-   Les domaines des variables :

    - Le calcul du ``min`` est :math:`O(|D|)` et est effectué à chaque fois que
      l'on veut faire du forward-checking. On pourrait maintenir une variable
      qui stocke le minimum du domaine de chaque variable, et la mettre à jour à
      chaque fois que le domaine est modifié.

    - La sauvegarde et la restauration des domaines sont coûteuses, car la copie
      d'un domaine est :math:`O(|D|)`. On pourrait implémenter les domaines de
      manière plus efficace pour optimiser ces opérations, par exemple en
      utilisant des structures de données plus adaptées (``BitSet`` ou
      ``SparseSet``).

-   L'algorithme du point fixe propage de très nombreuses fois les contraintes
    de manière inutile, car il repropage à chaque fois toutes les contraintes,
    même celles qui n'ont pas été modifiées. On pourrait maintenir une file de
    contraintes à propager, et ne propager que les contraintes qui ont été
    modifiées.

-   On n'utilise que des contraintes binaires ``NotEqual(x, y, offset)``, mais
    on pourrait implémenter des contraintes globales plus efficaces pour ce type
    de problème, comme la contrainte ``AllDifferent`` qui est spécialement
    conçue pour les problèmes d'assignation de valeurs distinctes à un ensemble
    de variables.