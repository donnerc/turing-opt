====================================================================
Turing2 : Optimisation combinatoire et programmation par contraintes
====================================================================

..  contents:: Parties du cours
    :depth: 3


Objectifs du module
:::::::::::::::::::

Dans ce module du cours, vous allez découvrir les éléments suivants

* Approfondir des notions déjà effleurées lors du cours Turing de base : 
    * Recherche en profondeur 
    * Récursion
    * Programmation orientée objets
    * Structures de données

* Les notions de base de la programmation par contraintes
* Des algorithmes de résolution de problèmes de satisfaction et d'optimisation
  de contraintes
* Renforcer vos compétences en programmation Python, notamment la programmation
  orientée objets
* Découvrir un des aspects phare du domaine de l'intelligence datant d'avant
  l'an 2000 traitant du raisonnement automatique.
* Développer votre propre solveur de contraintes en Python en utilisant la
  programmation orientée objets
* Appliquer les connaissances acquises à divers problèmes de satisfaction et optimisation
  de contraintes


Partie 0 : Introduction à l'optimisation combinatoire
:::::::::::::::::::::::::::::::::::::::::::::::::::::

..  toctree::
    :maxdepth: 2
    :numbered:
    
    introduction-opt.rst
    knapsack.rst


Partie 1 : Problèmes de satisfaction de contraintes
:::::::::::::::::::::::::::::::::::::::::::::::::::

..  note::

    Cette partie nécessite de comprendre de manière détaillée le fonctionnement
    de la récursion. Ces notions sont présentées dans la partie "Concepts de
    programmation".

..  toctree::
    :maxdepth: 2
    :numbered:
    
    psc/n-queens-csp.rst
    psc/generate-and-test.rst
    psc/generate-and-test-visu.rst
    psc/dfs-filter.rst
    psc/dfs-pruning.rst
    psc/exos.rst

..  
    session1/backtrack.rst
    session1/tinycsp.rst
    session1/exercices.rst

.. _part-toycsp:

Partie 2 : Programmation par contraintes
::::::::::::::::::::::::::::::::::::::::

    Constraint Programming represents one of the closest approaches computer
    science has yet made to the Holy Grail of programming: the user states the
    problem, the computer solves it. [E. Freuder]

..  note::

    Cette partie nécessite des connaissances de base en programmation orientée
    objets (POO). Ces notions sont présentées dans la partie "Concepts de
    programmation".

..  admonition:: Résumé

    Le but est de développer en Python un premier solveur de contraintes
    permettant de modéliser et résoudre des problèmes de satisfaction de
    contraintes (CSP) élémentaires tels que le problème des n reines, le Sudoku,
    ou encore les problèmes de coloriage de graphe.

..  toctree::
    :maxdepth: 2
    :numbered:
    
    cp/introduction.rst
    cp/cp-concepts.rst
    cp/implementation-1.rst
    cp/solver-and-fixpoint-algorithm.rst
    cp/benchmarking.rst
    cp/exos.rst

..
    cp/global-constraints.rst

Partie 3 : Programmation dynamique
::::::::::::::::::::::::::::::::::

..  admonition:: Résumé

    La programmation dynamique est une technique algorithmique de résolution de
    problèmes d'optimisation combinatoire. Elle repose sur le principe de
    "diviser pour régner" et permet de résoudre efficacement des problèmes qui
    peuvent être décomposés en sous-problèmes plus petits.

    On pourrait dire que la programmation dynamique est une forme de mémoïsation
    systématique, où les résultats des sous-problèmes sont stockés pour éviter
    les calculs redondants.

..  toctree::
    :maxdepth: 2
    :numbered:
    
    dp/introduction.rst
    dp/fibonacci.rst
    dp/memoization-top-down.rst
    dp/graphe-de-dependances.rst
    dp/tabulation-bottom-up.rst
    dp/knapsack.rst
    dp/exos.rst



BONUS : Un solveur plus puissant
::::::::::::::::::::::::::::::::

..  note::

    Cette partie est un résidu de l'édition 2025 du cours. Nous ne traiterons
    pas cette partie au cours. Elle montre comment développer un solveur plus
    professionnel, avec des structures de données plus efficaces. 

    Nous la laissons de côté par manque de temps.

..  toctree::
    :maxdepth: 2
    :numbered:
    
    better-cp-solver/introduction.rst
    better-cp-solver/prerequis.rst
    better-cp-solver/stack.rst
    better-cp-solver/turingcp.rst
    better-cp-solver/statemanager.rst
    better-cp-solver/state-stack.rst
    better-cp-solver/sparse-sets.rst




..
    Parties en préparation
    ::::::::::::::::::::::

    ..  toctree::
        :maxdepth: 2
        :numbered:

        part3/exos.rst
        playground.rst

..
    session2/

Concepts de programmation
:::::::::::::::::::::::::

..  note::

    Cette partie est indépendante de la programmation par contraintes et
    contient des explications sur certains concepts avancés du langage Python.

    Ce matériel est extrait du cours d'OC informatique du Collège du Sud

..  toctree::
    :maxdepth: 2
    :numbered:
    
    prog-recursion/main.rst
    prog-poo/main.rst
    techniques-python/main.rst
    common-ds/main.rst

..
    Astuces pratiques
    :::::::::::::::::

    ..  note:: 

        Cette rubrique donne des astuces et des outils pour être plus efficace en
        programmation, et donc lors de la résolution des problèmes.

    ..  toctree::
        :caption: Astuces
        :maxdepth: 2
        :numbered:
        
        git/main
        tricks/main




Ressources utiles
:::::::::::::::::

..  toctree::
    :maxdepth: 2
    :numbered:

    glossaire.rst


*   Cours de programmation par containtes de C. Solnon : https://perso.liris.cnrs.fr/christine.solnon/Site-PPC/