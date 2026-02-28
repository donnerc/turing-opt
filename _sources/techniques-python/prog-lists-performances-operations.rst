..  _prog-lists-performances-operations:


Résumé de l'efficacité des opérations sur les listes
####################################################

..  contents:: Contenu de la page
    :depth: 3


Les concepteurs de Python ont dû faire de nombreux choix lorsqu'ils ont
implémenté la structure de données liste. Chacun de ces choix pouvait avoir un
impact sur la rapidité des opérations de liste. Pour faire des choix judicieux,
ils ont étudié les façons dont les gens utiliseraient le plus souvent les
listes. Ils ont optimisé l'implémentation des listes pour que les opérations les
plus courantes soient très rapides. Ils ont également essayé d'optimiser les
opérations moins courantes rapides, mais quand un compromis devait être fait les
performances d'une opération moins courante ont souvent été sacrifiées au profit
de l'opération la plus courante.

Les deux opérations les plus courantes sont l'indexation (accès à l'élément se
trouvant à une certaine position) et l'affectation d'une valeur à une certaine
position de la liste. Ces deux opérations demandent donc un temps constant,
quelle que soit la taille de la liste. Lorsque l'efficacité d'une opération ne
dépend pas de la taille de la liste, on dit qu'elle est en :math:`O(1)`.

Une autre opération très courante consiste à agrandir une liste. La méthode
``append`` est en :math:`O(1)` alors que la concaténation de deux listes et en
:math:`O(k)``, où :math:`k` est la taille de la liste à concaténer. Il est
important de garder cette information en tête pour faire des choix judicieux.

.. _tbl_listbigo:

.. table:: **Efficacité Grand-O des opérations sur les listes Python**

    ============================= ==================
             Opération                Efficacité Grand-O
    ============================= ==================
         indexation ``[]``                   O(1)
      affectation à un élément               O(1)
                ``append``                   O(1)
                 ``pop()``                   O(1)
                ``pop(i)``                   O(n)
        ``insert(i,item)``                   O(n)
    suppression avec ``del``                 O(n)
             itération                       O(n)
         appartenance (``in``)               O(n)
       get slice ``[x:y]``                   O(k)
             ``del slice``                   O(n)
             ``set slice``                   O(n+k)
               ``reverse``                   O(n)
           concaténation                     O(k)
                 tri                         O(n log n)
    multiplication par un nombre             O(nk)
    ============================= ==================

Exercices
=========

Exercice 1
----------

Écrivez un programme qui chronomètre les trois façons suivantes de vider une
liste (pour une liste ``list(range(int(1e4)))`` de 10'000 éléments)

* Supprimer à chaque fois le dernier élément de la liste jusqu'à ce qu'elle soit vide
* Supprimer à chaque fois le premier élément de la liste jusqu'à ce qu'elle soit vide
* Supprimer à chaque fois l'élément du milieu de la liste jusqu'à ce qu'elle soit vide

..  admonition:: Indication

    Pour chaque façon de vider la liste, définissez une fonction ``test_N`` qui
    effectue l'opération et que vous chronométrez avec la fonction ``timeit``
    développée dans la section :ref:`prog-lists-performances-creation`.

..  activecode:: list-performances-operations-exercice-01

    ..  admonition:: Avertissement

        N'oubliez pas qu'il n'est pas possible d'importer le moduler ``timeit``
        dans l'éditeur ci-dessous et qu'il faut utiliser futurecoder.io.

    ~~~~

..  reveal:: 0715c0a9-44c5-4117-b33e-c5703ec8ee3d
    :showtitle: Solution

    ..  admonition:: Solution

        ..  code-block:: python

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
                the_list = list(range(N))
                
                while len(the_list) > 0:
                    the_list.pop()
                    
            def test_2():
                the_list = list(range(N))
                
                while len(the_list) > 0:
                    the_list.pop(0)
                    
            def test_3():
                the_list = list(range(N))
                
                while len(the_list) > 0:
                    the_list.pop(len(the_list) // 2)
                    
            # chronomètre les fonctions les unes après les autres
            for func in [test_1, test_2, test_3]:
                timeit(func)



Exercice 2
==========

On veut établir la relation entre le temps nécessaire pour faire un
``list.pop()`` et un ``list.pop(0)`` pour des listes de différentes tailles.
Faire l'expérience en prenant à chaque fois le meilleur temps de 20 runs, pour
les tailles de listes suivantes : :math:`N = 10'000, 20'000, 30'000, ....
200'000`.

Utilisez Excel ou le module ``matplotlib`` pour représenter
graphiquement les mesures dans un graphique de type "Scatter x/y".

..  activecode:: list-performances-operations-exercice-02

    ..  admonition:: Avertissement

        N'oubliez pas qu'il n'est pas possible d'importer le moduler ``timeit``
        dans l'éditeur ci-dessous. Utilisez l'éditeur
        https://console.basthon.fr/.


    ~~~~

..  reveal:: f45daf58-4963-49b3-b8cd-9e9730d9595f
    :showtitle: Solution

    ..  admonition:: Variante avec Excel

        Voici un code qui affiche les données au format CSV pour être importées
        dans Excel.

        ..  activecode:: 50a08d2e-4573-4847-8695-86f9d2e0f34e

            from timeit import default_timer as timer

            def average(data):
                return sum(data) / len(data)

            def timeit(func, data, ntimes=10):
                
                running_times = []
                for _ in range(ntimes):
                    data_copy = data[:]
                    start = timer()
                    func(data_copy)
                    end = timer()
                    running_times.append(end - start)
                    
                measures = [
                    round(f(running_times) * 1000, 4) 
                        for f in [average, min, max]
                ]
                    
                #print(f"Moyenne sur {ntimes} exécutions de {func.__name__}: {avg_time} ms")
                return measures


            def pop_tail(data):
                return data.pop()
                
            def pop_start(data):
                return data.pop(0)
                
            def benchmark(func, sizes):
                measures = []
                for size in sizes:
                    data = list(range(size))
                    avg_time, min_time, max_time = timeit(func, data)
                    data_point = (size, avg_time)
                    measures.append(data_point)
                    
                return measures
                
            def csv(data, headers=None, sep=';'):
                csv = ''
                
                if headers:
                    csv += sep.join(headers) + '\n'
                    
                for row in data:
                    csv += sep.join([str(d) for d in row]) + '\n'
                    
                return csv
                
            sizes = range(10_000, 200_001, 10_000)
            funcs = [pop_tail, pop_start]
            measures = {f'{f.__name__}' : benchmark(f, sizes) for f in funcs}
            print(measures)

            for key in measures:
                print(csv(measures[key], headers=['List size', key]))


    ..  admonition:: Variante avec le module ``matplotlib``

        Voici un code similaire qui visualise les données avec ``matplotlib``.

        ..  activecode:: 63024880-6e84-46fa-8926-c3c10984492d

            import matplotlib.pyplot as plt
            from timeit import Timer

            sizes = []
            pop_head_times = []
            append_times = []


            pop_head = Timer("x.pop(0)", "from __main__ import x")
            pop_tail = Timer("x.pop()", "from __main__ import x")
            print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
            for i in range(10_000, 200_001, 10_000):
                sizes += [i]
                
                x = list(range(i))
                head_t = pop_head.timeit(number=1000)
                pop_head_times += [head_t]
                
                x = list(range(i))
                append_t = pop_tail.timeit(number=1000)
                append_times += [append_t]
                
                print(f"{i:<10d}{head_t:>15.5f}{append_t:>15.5f}")
                
            # Plotting the data with matplotlib
            fig, ax = plt.subplots()
            ax.scatter(sizes, pop_head_times, label="pop(0)")
            ax.scatter(sizes, append_times, label="pop()")
            ax.set_xlabel("List size")
            ax.set_ylabel("Time [ms]")
            ax.set_title("Comparison between pop(0) and pop()")
            ax.legend()
            ax.grid(True)
            plt.show()



..  reveal:: 9E00EAE1-CD7A-4C3A-A885-1BC94FA4F02A
    :showtitle: Idée d'exercice (``pop(0)`` vs ``pop()``)
    :instructoronly:

    As a way of demonstrating this difference in performance let’s do
    another experiment using the ``timeit`` module. Our goal is to be able
    to verify the performance of the ``pop`` operation on a list of a known
    size when the program pops from the end of the list, and again when the
    program pops from the beginning of the list. We will also want to
    measure this time for lists of different sizes. What we would expect to
    see is that the time required to pop from the end of the list will stay
    constant even as the list grows in size, while the time to pop from the
    beginning of the list will continue to increase as the list grows.

    :ref:`Listing 4 <lst_popmeas>` shows one attempt to measure the difference
    between the two uses of pop. As you can see from this first example,
    popping from the end takes 0.0003 milliseconds, whereas popping from the
    beginning takes 4.82 milliseconds. For a list of two million elements
    this is a factor of 16,000.

    There are a couple of things to notice about :ref:`Listing 4 <lst_popmeas>`. The
    first is the statement ``from __main__ import x``. Although we did not
    define a function we do want to be able to use the list object x in our
    test. This approach allows us to time just the single ``pop`` statement
    and get the most accurate measure of the time for that single operation.
    Because the timer repeats 1000 times it is also important to point out
    that the list is decreasing in size by 1 each time through the loop. But
    since the initial list is two million elements in size we only reduce
    the overall size by :math:`0.05\%`

    .. _lst_popmeas:

    **Listing 4**

    ::

        pop_zero = Timer("x.pop(0)", "from __main__ import x")
        pop_end = Timer("x.pop()", "from __main__ import x")

        x = list(range(2000000))
        print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} milliseconds")

        x = list(range(2000000))
        print(f"pop(): {pop_end.timeit(number=1000):11.5f} milliseconds")

        pop(0):    2.09779 milliseconds
        pop():     0.00014 milliseconds

    While our first test does show that ``pop(0)`` is indeed slower than
    ``pop()``, it does not validate the claim that ``pop(0)`` is
    :math:`O(n)` while ``pop()`` is :math:`O(1)`. To validate that claim
    we need to look at the performance of both calls over a range of list
    sizes. :ref:`Listing 5 <lst_poplists>` implements this test.

    .. _lst_poplists:

    **Listing 5**

    ::

        pop_zero = Timer("x.pop(0)", "from __main__ import x")
        pop_end = Timer("x.pop()", "from __main__ import x")
        print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
        for i in range(1_000_000, 100_000_001, 1_000_000):
            x = list(range(i))
            pop_zero_t = pop_zero.timeit(number=1000)
            x = list(range(i))
            pop_end_t = pop_end.timeit(number=1000)
            print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")

    :ref:`Figure 3 <fig_poptest>` shows the results of our experiment. You can see
    that as the list gets longer and longer the time it takes to ``pop(0)``
    also increases while the time for ``pop`` stays very flat. This is
    exactly what we would expect to see for a :math:`O(n)` and
    :math:`O(1)` algorithm.

    Some sources of error in our little experiment include the fact that
    there are other processes running on the computer as we measure that may
    slow down our code, so even though we try to minimize other things
    happening on the computer there is bound to be some variation in time.
    That is why the loop runs the test one thousand times in the first place
    to statistically gather enough information to make the measurement
    reliable.

    .. _fig_poptest:

    .. figure:: Figures/poptime.png

    Figure 3: Comparing the Performance of ``pop`` and ``pop(0)``
