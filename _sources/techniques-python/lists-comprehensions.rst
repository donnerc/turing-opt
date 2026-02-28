..  _prog-lists-comprehensions:

Listes en compréhension
#######################

..  contents:: Contenu de la page
    :depth: 3


Dans cette section, nous allons introduire une technique très élégante et
efficace pour définir des listes. Il s'agit du concept de **compréhension de
liste** (ou **compréhensions de listes**) qui ressemble fortement à la notation
permettant de définir une collection en mathématiques.

Activité 1
==========

Avant d'aborder le concept de création de listes, essayez de résoudre le
problème ci-dessous, qui ne devrait pas vous poser de problème.

..  activecode:: prog-lists-comprehension-first_n_odds

    Définissez une fonction ``first_n_odds(n: int) -> list[int]`` qui retourne
    les ``n`` premiers nombres naturels impairs.

    ..  admonition:: Exemples d'utilisation

        ::

            >>> first_n_odds(5)
            [1, 3, 5, 7, 9]
            >>> first_n_odds(2)
            [1, 3]
            >>> first_n_odds(0)
            []
       
    ~~~~
    
    def first_n_odds(n: int) -> list[int]:
        result = []
        
        return result

    def test():
        print(first_n_odds(5))
        print(first_n_odds(2))
        print(first_n_odds(0))

    # test()

    ====        

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):   

        def test_correct_annotations(self):
            tests = [
                (5, [1, 3, 5, 7, 9]),
                (2, [1, 3]),
                (0, []),
            ]

            for n, exected in tests:
                result = first_n_odds(n)
                feedback = f"Retourne la liste des n premiers nombres impairs"
                self.assertEqual(result, exected, feedback)
            
    myTests().main()

..  reveal:: E6667D1E-A1C4-4086-A09F-1CBCA2A57B28
    :showtitle: Réponse

    ..  code-block:: python
        :linenos:

        def first_n_odds(n: int) -> list[int]:
            result = []
            
            for i in range(n):
                result.append(2*i + 1)

            return result


Activité 2
==========

..  activecode:: prog-lists-comprehension-activity-first_n_odd_squares

    Définissez, sans utiliser la nouvelle syntaxe de compréhension de listes,
    une fonction ``only_greater_than(numbers: list[int], a: int) -> list[int]``
    qui retourne la liste des nombres présents dans la liste ``numbers`` qui
    sont strictement supérieure à ``a``, en conservant l'ordre des éléments.

    ..  admonition:: Exemples d'utilisation

        ::

            >>> only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 4)
            [5, 5, 6, 7, 6]
            >>> only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 6)
            [7]
            >>> only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 7)
            []
            >>> only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 0)
            [3, 5, 3, 5, 6, 7, 3, 6]

    ~~~~

    def only_greater_than(numbers: list[int], a: int) -> list[int]:
        return []

    def test():
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 4))
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 6))
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 7))
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 0))

    # test()

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):   

        def test_correct_annotations(self):
            tests = [
                (
                    ([3, 5, 3, 5, 6, 7, 3, 6], 4),
                    [5, 5, 6, 7, 6]
                ),
                (
                    ([3, 5, 3, 5, 6, 7, 3, 6], 6),
                    [7]
                ),
                (
                    ([3, 5, 3, 5, 6, 7, 3, 6], 7),
                    []
                ),
                (
                    ([3, 5, 3, 5, 6, 7, 3, 6], 0),
                    [3, 5, 3, 5, 6, 7, 3, 6]
                ),
            ]

            for args, exected in tests:
                result = only_greater_than(*args)
                feedback = f"La liste retournée est correcte"
                self.assertEqual(result, exected, feedback)
            
    myTests().main()

..  reveal:: F6DEDE6F-0E7A-43C3-AA54-C6B2B1278704
    :showtitle: Réponse

    ..  code-block:: python
        :linenos:

        def only_greater_than(numbers: list[int], a: int) -> list[int]:
            result = []
            
            for x in numbers:
                if x > a:
                    result.append(x)
                    
            return result



Compréhensions de listes
========================

..  youtube:: 3IDMOC6qhlM
    :width: 800
    :height: 430

Une **compréhension de liste** (on parle aussi de **liste en compréhension**)
est une syntaxe spéciale qui permet d'imiter la notation mathématique de
**compréhension d'ensemble** que vous utilisez souvent au cours de
mathématiques. Par exemple, on peut désigner l'ensemble des nombres naturels
impairs par la compréhension

..  math::

    E = \{
        2i + 1 \mid i \in \mathbb{N}\text{ et } i < 10
    \}

En Python, on peut exprimer exactement la même chose avec la syntaxe

::

    [<expression> for <variable> in <iterable> if <filter_condition>]

où 

* ``<iterable>`` représente n'importe quelle expression dont l'évaluation donne
  un objet **itérable** (Liste, chaîne de caractères, tuple, dictionnaire,
  fonction qui retourne un itérable, etc ...)

* ``<filter_condition>`` est une condition qui permet de filtrer les éléments
  issus de ``<iterable>``

* ``<expression>`` est une expression quelconque qui peut impliquer la variable
  ``<variable>`` définie entre le ``for`` et le ``in``.

Exemple 1
=========

Pour exprimer la liste des ``n`` plus petits nombres naturels impairs, on peut
utiliser la syntaxe de **compréhension de liste**

::

    [expression(x) for x in <iterable>]

où ``<iterable>`` désigne un objet itérable (que l'on peut parcourir avec une
boucle ``for`` normale).


..  activecode:: EDE64174-E5FB-485D-8088-DB42016FBDAE

    Cela permet d'écrire la fonction ``first_n_odds(n)`` de manière bien plus
    simple et efficace de la manière suivante:

    ~~~~

    def first_n_odds(n: int) -> list[int]:
        return [2*i + 1 for i in range(n)]

    n = 10
    print(f"Voici les {n} premiers nombres impairs: {first_n_odds(n)}")


Exemple 2
=========

On peut simplifier le code de la fonction ``only_greater_than`` définie à
l'activité précédente avec une compréhension de liste de la manière suivante:

..  activecode:: B534F257-1F6E-4C22-A325-E221E7C53C78

    def only_greater_than(numbers: list[int], a: int) -> list[int]:
        return [x for x in numbers if x > a]

    def test():
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 4))
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 6))
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 7))
        print(only_greater_than([3, 5, 3, 5, 6, 7, 3, 6], 0))

    test()

    

Questions de compréhension
==========================

..  mchoice:: prog-lists-comprehension-q1
    :answer_a: [4,2,8,6,5]
    :answer_b: [8,4,16,12,10]
    :answer_c: 10
    :answer_d: [10]
    :correct: d
    :feedback_a: Les éléments de ``alist`` sont doublés avant d'être insérés dans blist.
    :feedback_b: Certains éléments de alist ne sont pas inclus dans blist. Regardez la clause if.
    :feedback_c: Le résultat est nécessairement une liste.
    :feedback_d: Oui. 5 est le seul nombre impair dans la liste alist. Il est doublé avant d'être inséré dans blist.    
    :random:
    
    Qu'affiche le programme ci-dessous?

    ..  code-block:: python
        :linenos:

        alist = [4, 2, 8, 6, 5]
        blist = [x * 2 for x in alist if x % 2 == 1]
        print(blist)


..  mchoice:: prog-lists-comprehension-q2
    :answer_a: [100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
    :answer_b: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    :answer_c: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    :answer_d: [121, 169, 225, 289, 361]
    :answer_e: [100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    :correct: d
    :feedback_a: Non, uniquement des nombres impairs passent le filtre de la clause if.
    :feedback_b: Les éléments sont d'abord élevés au carré avant d'être inclus dans le résultat.
    :feedback_c: Les éléments sont d'abord élevés au carré avant d'être inclus dans le résultat. De plus, la borne supérieure du range n'est pas incluse.
    :feedback_d: Ce programme produit en effet la liste des carrés parfaits impairs compris entre 100 et 400 (non compris).
    :feedback_e: Non, uniquement des nombres impairs passent le filtre de la clause if. De plus, la borne supérieure du range n'est pas incluse.
    :random:
    
    Qu'affiche le programme ci-dessous?

    ..  code-block:: python
        :linenos:
        
        result = [x ** 2 for x in range(10, 20) if x ** 2 % 2 == 1]
        print(result)


..  mchoice:: prog-lists-comprehension-q3
    :answer_a: [0, 0, 1, -1, 2, -2, 3, -3, 4, -4]
    :answer_b: [[0, -0], [1, -1], [2, -2], [3, -3], [4, -4]]
    :answer_c: [0, 0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
    :answer_d: [[0, -0], [1, -1], [2, -2], [3, -3], [4, -4], [5, -5]]
    :correct: b
    :feedback_a: Non, les éléments insérés dans la liste finale sont des listes de deux éléments 
    :feedback_b: Oui, c'est juste.
    :feedback_c: Non, les éléments insérés dans la liste finale sont des listes de deux éléments. De plus, la borne supérieure du range n'est pas incluse.
    :feedback_d: Oui, c'est presque juste, mais la borne supérieure du range n'est pas incluse.
    :random:
    
    Qu'affiche le programme ci-dessous?

    ..  code-block:: python
        :linenos:
            
        result = [[x, -x] for x in range(5)]
        print(result)


    
..  shortanswer:: prog-lists-comprehension-q4
    
    Sans exécuter le programme ci-dessous, essayez de prédire ce qu'il affiche et ce
    qu'il fait de manière générale avec la fonction :math:`f(x) = x^2 - 1`.

    ..  code-block:: python
        :linenos:

        def xvalues(xmin, xmax, n):
            step = (xmax - xmin) / n
            return [(xmin + n * step) for n in range(n+1)]

        def f(x):
            return x ** 2 - 1

        print(xvalues(-2, 2, 8))
        print([[x, f(x)] for x in xvalues(-2, 2, 8)])


Exercices
=========

Exercice 0
----------

..  activecode:: prog-lists-comprehension-exercise-00

    Définissez une fonction ``perfect_squares_between(a:int , b: int) ->
    list[int]`` qui retourne la liste de tous les carrés parfaits :math:`n =
    x^2` pour :math:`x \in \mathbb{N}` et :math:`a \leq n < b`. Si :math:`b <=
    a`, la fonction doit retourner la liste vide.

    La fonction doit utiliser une compréhension de liste et ne faire qu'une
    seule ligne.

    ..  admonition:: Indication

        Vous devez utiliser la fonction ``ceil(x)`` du module ``math`` pour
        arrondir un nombre à l'entier supérieur.

        Il faut, pour cela commencer par importer la fonction en question avec

        ::

            from math import ceil

    ..  admonition:: Exemples d'utilisation

        ::

            >>> perfect_squares_between(0, 30)
            [0, 1, 4, 9, 16, 25]
            >>> perfect_squares_between(0, 25)
            [0, 1, 4, 9, 16]
            >>> perfect_squares_between(20, 40)
            [25, 36]
            >>> perfect_squares_between(20, 20)
            []
            >>> perfect_squares_between(40, 20)
            []

    ~~~~

    def perfect_squares_between(a:int , b: int) -> list[int]:
        return []

    def test():
        print(perfect_squares_between(0, 30))
        print(perfect_squares_between(0, 25))
        print(perfect_squares_between(20, 40))
        print(perfect_squares_between(20, 20))
        print(perfect_squares_between(40, 20))

    test()

    ====        

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):   
        
        def test_correct(self):

            tests = [
                ((0, 30), [0, 1, 4, 9, 16, 25]),
                ((0, 25), [0, 1, 4, 9, 16]),
                ((20, 40), [25, 36]),
                ((20, 20), []),
                ((40, 20), []),
            ]

            for args, expected in tests:
                result = perfect_squares_between(*args)
                self.assertEqual(result, expected, feedback="La liste retournée est correcte")
            
            
    myTests().main()    



..  reveal:: 7D69872B-D107-4663-8F01-C5B5B9198505
    :showtitle: Solution

    La solution ci-dessous n'est pas la solution la plus optimisée.

    ..  code-block:: python

        from math import ceil

        def perfect_squares_between(a:int , b: int) -> list[int]:
            return [x ** 2 for x in range(int(ceil(a ** .5)), int(b ** .5) + 1) if x ** 2 < b]

Exercice 1
----------

..  activecode:: prog-lists-comprehension-exercise-01

    Transformez la fonction ci-dessous en utilisant une compréhension de liste.
    Le code de la fonction ne doit pas faire plus d'une ligne, mais doit
    fonctionner à l'identique.

    ~~~~

    def only_females(students):
        result = []

        for student in students:
            gender = student[1]
            if gender == 'f':
                result.append(student[0])

        return result

    students = [
        ["Marie", 'f'],
        ["Carla", 'f'],
        ["Boris", 'm'],
        ["Laetitia", 'f']
    ]

    print(only_females(students))

    ====        

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):   

        def test_correct(self):
            students = [
                ["Marie", 'f'],
                ["Boris", 'm'],
                ["Laetitia", 'f'],
                ["Christophe", 'm'],
                ["Nicolas", 'm'],
            ]
            expected = ['Marie', 'Laetitia']

            result = only_females(students)

            self.assertEqual(result, expected, feedback="La liste retournée est identique")

        def test_oneliner(self):
            code = self.getEditorText()

            lines = [x for x in code.split("\n") if len(x) > 0]
            def_line = [l for l in lines if l.startswith('def only_females')][0]
            def_lineno = lines.index(def_line)
            
            count_body_lines = 0
            for k in range(def_lineno + 1, len(lines)):
                line = lines[k]

                if len(line) > 0 and (line.startswith('    ') or line.startswith('\t')):
                    count_body_lines += 1
                else:
                    break
                    
            self.assertEqual(count_body_lines, 1, feedback="Nombre de lignes non vides du corps de la fonction")
                    
            
    myTests().main()    




Exercice 2
----------

..  activecode:: prog-lists-comprehension-exercise-02

    Développez une fonction ``get_good_students(student_grades: list[any], grade: float) ->
    list[str]`` qui prend en paramètre une liste dont les éléments sont au format 
    
    ::

        [str, list[float]]

    dont le premier élément est le nom d'un élève et le deuxième élément une
    liste de notes. La fonction doit retourner une liste des élèves ayant une
    moyenne supérieure à la moyenne indiquée par le paramètre ``grade``.
    
    ~~~~

    def get_good_students(student_grades: list[any], grade: float) -> list[str]:
        return []


    student_grades = [
        ["Marie", [5.5, 3.5, 2.5, 6.0, 5.0]],
        ["Carla", [3.0, 4.3, 5.0, 5.5, 4.5, 3.5]],
        ["Boris", [5.0, 5.2, 5.4, 4.1, 4.8]],
        ["Laetitia", [5.1, 5.4, 4.1, 6.0, 5.5]]
    ]

    print(get_good_students(student_grades, 5.0))

    ====        

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):   

        def test_correct(self):
            student_grades = [
                ["Marie", [5.5, 3.5, 2.5, 6.0, 5.0]],
                ["Carla", [3.0, 4.3, 5.0, 5.5, 4.5, 3.5]],
                ["Boris", [5.0, 5.2, 5.4, 4.1, 4.8]],
                ["Laetitia", [5.1, 5.4, 4.1, 6.0, 5.5]],
                ["Marc", [2, 2, 3, 6, 5, 4]],
            ]
            tests = [
                [5, ['Laetitia']],
                [4.5, ['Boris', 'Laetitia']],
                [4.45, ['Marie', 'Boris', 'Laetitia']],
                [4.2, ['Marie', 'Carla', 'Boris', 'Laetitia']],
            ]
            for grade, expected in tests:
        
                result = get_good_students(student_grades, grade)
                feedback = f"La liste retournée est identique"
                self.assertEqual(result, expected, feedback=feedback)

        def test_oneliner(self):
            code = self.getEditorText()

            lines = [x for x in code.split("\n") if len(x) > 0]
            def_line = [l for l in lines if l.startswith('def get_good_students')][0]
            def_lineno = lines.index(def_line)
            
            count_body_lines = 0
            for k in range(def_lineno + 1, len(lines)):
                line = lines[k]

                if len(line) > 0 and (line.startswith('    ') or line.startswith('\t')):
                    count_body_lines += 1
                else:
                    break
                    
            self.assertEqual(count_body_lines, 1, feedback="Nombre de lignes non vides du corps de la fonction")
                    
            
    myTests().main()    


..  reveal:: 1B762FF3-4048-4E6B-A6D7-2729A44F9733
    :showtitle: Solution

    ..  code-block:: python

        def get_good_students(students_grades: list[any], grade: float) -> list[str]:
            return [student[0] for student in students_grades if sum(student[1]) / len(student[1]) > grade]


        student_grades = [
            ["Marie", [5.5, 3.5, 2.5, 6.0, 5.0]],
            ["Carla", [3.0, 4.3, 5.0, 5.5, 4.5, 3.5]],
            ["Boris", [5.0, 5.2, 5.4, 4.1, 4.8]],
            ["Laetitia", [5.1, 5.4, 4.1, 6.0, 5.5]]
        ]

        print(get_good_students(student_grades, 4.5))


Pour aller plus loin
====================

Vous trouverez de plus amples informations concernant les listes en
compréhension dans les ressources ci-dessous.

- L'article de blog suivant montre comment formater des listes en compréhension
  complexes pour éviter quelles ne deviennent totalement illisibles :
  https://treyhunner.com/2019/03/abusing-and-overusing-list-comprehensions-in-python/