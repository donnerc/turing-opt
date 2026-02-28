..  _prog-lists-performances-creation:

Performance des opérations sur les listes
#########################################

..  contents:: Contenu de la page
    :depth: 3


Dans cette section, nous allons étudier la performance des opérations d'ajout et
de suppression d'éléments dans une liste. Comme vous allez le constater, ajouter
un élément en fin de liste ou en début de liste ne demande pas la même quantité
de travail pour Python. 

Nous allons adopter une approche expérimentale consistant à mesurer le temps
d'exécution de différents codes modifiant des listes. Nous allons travailler
avec de grosses listes pour avoir des résultats plus significatifs. En effet,
c'est lorsqu'on travaille avec de grosses quantités de données que les problèmes
de performance se manifestent.

Mesurer les performances d'un code
==================================

En Python, il y a plusieurs manières plus ou moins précises de mesurer le temps
d'exécution d'un programme. Nous utiliserons le template ci-dessous pour tester
le temps d'exécution des différentes fonctions ``test_n()``

..  activecode:: 8afb9478-e20f-4e74-bb61-3b46e0f48413
    :language: webtp

    from timeit import default_timer as timer

    def timeit(func, ntimes=10):
        start = timer()
        for _ in range(ntimes):
            func()       # function to measure
        end = timer()
        mean = round((end - start) * 1000 / ntimes, 4)

        print(f"Moyenne sur {ntimes} exécutions de {func.__name__}: {mean} ms")

    def test():
        the_list = []
        for n in range(100000):
            the_list += [n]

    timeit(test, ntimes=20)


..  admonition:: Remarque : fonction en guise de paramètre

    Remarquez qu'à la ligne 18, on appelle la fonction ``timeit`` définie à la
    ligne 4 en lui fournissant **le nom** de la fonction à chronométrer (sans
    les parenthèses). La fonction à chronométrer est ensuite appelée (avec les
    parenthèses) à l'intérieur de la fonction ``timeit()`` à la ligne 7.


Toutes les manières de créer une liste ne se valent pas
=======================================================

Il y a plusieurs manières de créer des listes en Python et toutes ne se valent
pas au niveau des performances. Il est important de toujours avoir à l'esprit
ces différences de performance lorsqu'on programme en Python, pour éviter de
gaspiller de l'énergie inutilement.

Activité 1
----------

Le programme ci-dessous utilise la technique exposée précédemment pour mesurer
le temps d'exécution de chacune des fonctions ``test_1`` à ``test_5``. Toutes
ces fonctions font exactement la même chose : elles construisent toutes une
liste de 10'000 nombres entiers de 0 à 9999, mais de manière différente.

..  activecode:: 1cf21411-e37f-4bf9-839b-1f9a4205a16e
    :language: webtp

    from timeit import default_timer as timer

    def timeit(func, ntimes=10):
        start = timer()
        for _ in range(ntimes):
            func()       # function to measure
        end = timer()
        mean = round((end - start) * 1000 / ntimes, 4)

        print(f"Moyenne sur {ntimes} exécutions de {func.__name__}: {mean} ms")

    N = 10_000

    def test_1():
        the_list = []
        for n in range(N):
            the_list += [n]
            
    def test_2():
        the_list = []
        for n in range(N):
            the_list.append(n)

    def test_3():
        the_list = [None] * N
        for i in range(N):
            the_list[i] = i
            
    def test_4():
        the_list = [n for n in range(N)]
        
    def test_5():
        the_list = list(range(N))
        

    # chronomètre les fonctions les unes après les autres
    for func in [test_1, test_2, test_3, test_4, test_5]:
        timeit(func)


..  shortanswer:: prog-lists-performance-activity-01-tests-timings

    Exécutez plusieurs fois ce programme et notez la sortie produite.

..  shortanswer:: prog-lists-performance-activity-01-test-q1

    Les temps mesurés sont-ils toujours les mêmes?

..  shortanswer:: prog-lists-performance-activity-01-test-q2

    Y a-t-il une certaine cohérence / régularité dans les temps d'exécution
    mesurés?
    
..
    ..  shortanswer:: prog-lists-performance-activity-01-test_1

        ..  code-block:: python

            def test_1():
                N = 10000
                the_list = []
                for n in range(N):
                    the_list += [n]

    ..  shortanswer:: prog-lists-performance-activity-01-test_2

        ..  code-block:: python

            def test_2():
                N = 10000
                the_list = []
                for n in range(N):
                    the_list.append(n)

    ..  shortanswer:: prog-lists-performance-activity-01-test_3

        ..  code-block:: python

            def test_3():
                N = 10000
                the_list = [None] * N
                for i in range(N):
                    the_list[i] = i

    ..  shortanswer:: prog-lists-performance-activity-01-test_4

        ..  code-block:: python

            def test_4():
                N = 10000
                the_list = [n for n in range(N)]

    ..  shortanswer:: prog-lists-performance-activity-01-test_5

        ..  code-block:: python

            def test_5():
                N = 10000
                the_list = list(range(N))


..
    ..  shortanswer:: prog-lists-performance-activity-01-test_1

        Moyenne du temps d'exécution de la fonction ``test_1`` sur 10 exécutions
        consécutives:

    ..  shortanswer:: prog-lists-performance-activity-01-test_2

        Moyenne du temps d'exécution de la fonction ``test_2`` sur 10 exécutions
        consécutives:

    ..  shortanswer:: prog-lists-performance-activity-01-test_3

        Moyenne du temps d'exécution de la fonction ``test_3`` sur 10 exécutions
        consécutives:

    ..  shortanswer:: prog-lists-performance-activity-01-test_4

        Moyenne du temps d'exécution de la fonction ``test_4`` sur 10 exécutions
        consécutives:

    ..  shortanswer:: prog-lists-performance-activity-01-test_5

        Moyenne du temps d'exécution de la fonction ``test_5`` sur 10 exécutions
        consécutives:

Activité 2
----------

..  mchoice:: prog-lists-performance-activity-02

    D'après les mesures prises dans l'activité précédente cochez les cases qui
    conviennent 

    * Pour créer une liste, il est plus efficace de commencer avec une liste qui
      contient dès le début le bon nombre d'éléments que de partir d'une liste
      vide et d'utiliser ``list.append()``

      + Vrai. Le gain de performance est assez significatif. Cela vient du fait
        que, pour faire un ``.append()``, il faut agrandir la liste, ce qui
        implique parfois de déplacer tout le contenu de la liste pour trouver
        une plage d'emplacements mémoire suffisamment grande pour accueillir
        tous les éléments.

    * Il est plus efficace d'utiliser une compréhension de liste pour créer une
      nouvelle liste que d'écrire soi-même une boucle qui remplit un à un les
      éléments de la liste.

      + Vrai. Les compréhension de listes permettent à Python d'optimiser des
        tas de choses, en particulier la boucle qui va remplir la liste est
        interne à Python.

    * Peu importe la manière de créer une liste. Toutes les manières se valent
      au niveau performance.

      - Faux. Avez-vous vraiment fait les mesures?


..  admonition:: Avertissement

    L'interprétation des mesures se fera en classe et dans la section
    :ref:`prog-lists-c-implementation-discussion-performances`. Il s'agira de
    bien comprendre le lien entre le fonctionnement interne des listes et les
    performances des différentes opérations.


..  reveal:: 7DDC18E1-29BB-4C59-BE9F-7F746B380B9A
    :showtitle: Idées 
    :instructoronly:

    ..  admonition:: Idée

        Aller voir dans le code source de Python sur github la manière dont les
        listes sont implémentées.

        https://github.com/python/cpython

    * Création de liste
    * en partant d'une liste vide
    * en partant d'une liste de la bonne taille et en employant les html_domain_indices
    * compréhension de liste

    * Ajout des éléments en fin de liste
    * Insertion des éléments en début de liste
    * Insertion des éléments en milieu de liste