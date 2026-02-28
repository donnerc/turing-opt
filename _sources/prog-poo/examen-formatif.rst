.. _poo_examen-formatif.rst:

Examen formatif de POO
######################

..  contents:: Questions
    :depth: 3

Question 1
==========

Variable d'instance vs variable de classe
-----------------------------------------

..  shortanswer:: poo-exa-formatif-instance-vs-class-var

    Expliquez la différence entre une **variable d’instance** et une **variable
    de classe**. Dans quel cas faut-il utiliser une variable de classe plutôt
    qu’une variable d’instance ?

..  reveal:: 2fa20df4-07f0-4238-b979-5e2a5bd0e375
    :showtitle: Réponse

    ..  admonition:: Réponse

        -   Variable d’instance : spécifique à chaque instance, avec un
            emplacement mémoire distinct pour chaque instance. On y accède avec
            instance.variable

        -   Variable de classe : variable unique partagée par toutes les
            instances de la classe. On y accède avec classe.variable

Méthode d'instance vs méthode statique
--------------------------------------

..  shortanswer:: poo-exa-formatif-instance-vs-static-method

    Expliquez la différence entre une **méthode de classe** et une **méthode
    statique**. Dans quel cas faut-il utiliser l’une plutôt que l’autre ?

..  reveal:: 5fecfb99-c08e-4ae9-b40c-56a1cffd6d78
    :showtitle: Réponse

    ..  admonition:: Réponse

        •   Méthode de classe : n’accède jamais aux variable d’instance, mais
            peut accéder aux variables de classe.
        •   Méthode statique : n’accède ni aux variables d’instance, ni aux
            variables de classe.


``__str__`` vs ``__repr__``
---------------------------

..  shortanswer:: poo-exa-formatif-str-vs-repr

    Expliquez l’utilité de la méthode ``__str__`` dans une classe et la différence
    avec ``__repr__``

..  reveal:: 222781b1-6335-4a33-8fb2-2e0e5fa23144
    :showtitle: Réponse

    ..  admonition:: Réponse

        La méthode ``__str__`` : permet d’appeler ``str(x)`` alors que
        ``__repr__`` permet d’appeler ``repr(x)`` sur instance ``x`` de la
        classe. Par convention la représentation doit permettre de recréer une
        instance en copiant la représentation dans le code Python.

Méthode ``__init__``
--------------------

..  shortanswer:: poo-exa-formatif-init

    Expliquez précisément le rôle de la méthode ``__init__`` dans une classe
    
..  reveal:: 8b428332-2d7d-4248-bb2a-692fab8cf88f
    :showtitle: Réponse

    ..  admonition:: Réponse
    
        Il s'agit du "constructeur". Cette méthode est exécutée automatiquement
        lors de l’instanciation. Permet d’initialiser les variables d’instance
        et modifier les variables de classe.

Analyse de programme POO
------------------------

..  shortanswer:: poo-exa-formatif-sortie-poo

    Sans utiliser Python, écrivez exactement la sortie produite par le programme
    de l’encadré

    ..  code-block:: python
        :linenos:

        class A:
            n = 0
            def __init__(self, a):
                self._a = a
                A.n += 1
            def tell(s):
                c = s.__class__.__name__
                print(f"tell from {c}: {s._a}")

            def x(self):
                print("x: ", self.n)

        class B(A):
            def __init__(self, a, b=3):
                super().__init__(a)
                self._b = b

        for it in [A(3), B(4, 5), A(6)]:
            it.tell()
            it.x()
            print("=" * 4)


..  reveal:: 0e3dc971-1a2d-4b9f-8f4c-e8a38a306eb8
    :showtitle: Réponse

    ..  admonition:: Réponse
    
        Utilisez Python pour vérifier votre réponse.

Avantages de la POO
-------------------

..  shortanswer:: poo-exa-formatif-avantages-poo

    Citez deux avantages majeurs de la programmation orientée objets par rapport
    à la programmation impérative.


..  reveal:: 7c4e6a43-a39b-4048-a401-c66b990c426d
    :showtitle: Réponse

    ..  admonition:: Réponse

        1.  Permet de mieux organiser le code en regroupant les données et les «
            algorithmes » liés à un problème / situation / entité dans un même «
            espace » (la classe). Force les développeurs à bien architecturer le
            problème en décomposant le problème par responsabilité et à penser
            les interactions entre les composants
        2.  Permet une meilleure réutilisabilité du code, grâce à l’héritage
            notamment.
        3.  Permet d’éviter d’avoir à utiliser des variables globales (Le
            langage Java, langage phare du paradigme POO ne possède même 

Question 2 (Exceptions)
=======================

Voici une liste d'exceptions

A.	``ArithmeticError``
B.	``IndexError``
C.	``KeyError``
D.	``OverflowError``
E.	``ZeroDivisionError``
F.	``TypeError``
G.	``MemoryError``
H.	``ValueError``

Voici la hiérarchie entre les exceptions

::

    BaseException
    └── Exception
        ├── ArithmeticError
        │    ├── OverflowError
        │    └── ZeroDivisionError
        ├── LookupError
        │    ├── IndexError
        │    └── KeyError
        ├── MemoryError
        ├── OSError
        │    ├── FileExistsError
        │    ├── FileNotFoundError
        │    └── PermissionError
        └── ValueError

..  shortanswer:: poo-exa-formatif-exceptions-01

    Indiquez le ou les types d’exception que peut produire le programme
    ci-dessous.

    ..  code-block:: python
        :linenos:

        a = float(input("Numérateur: "))
        b = float(input("Numérateur: "))
        c = a / b 

..  shortanswer:: poo-exa-formatif-exceptions-02

    Indiquez le ou les types d’exception que peut produire le programme
    ci-dessous.

    ..  code-block:: python
        :linenos:

        n = randint(10, 50)
        L = [randint(1, 100) for i in range(n)]
        print(L[n / 2])


..  shortanswer:: poo-exa-formatif-exceptions-03

    Indiquez le ou les types d’exception que peut produire le programme
    ci-dessous.

    ..  code-block:: python
        :linenos:

        a = [randint(1, 10) 
        for _ in range(int(1e12))]


..  shortanswer:: poo-exa-formatif-exceptions-04

    Indiquez le ou les types d’exception que peut produire le programme
    ci-dessous.

    ..  code-block:: python
        :linenos:

        L = [1,2,3,4]
        # randint(a, b) tirer un nombre entier 
        # entre a et b compris
        print(L[randint(0, 4)])

Question 3 (compréhension bloc ``try``)
=======================================

On donne le programme ci-dessous


..  code-block:: python
    :linenos:

    try:
        filename = input("Fichier à ouvrir: ")
        with open(filename, 'r') as f:
            for line in f:
                fields = line.split(';')
                print(fields[1])
    except FileNotFoundError as e:
        print("A")
    except Exception as e:
        print("B")
    else:
        print("C")
    finally:
        print("D")              

..  shortanswer:: poo-exa-formatif-exceptions-05-A

    Déterminez la sortie produite par le programme si le fichier lu par la
    fonction ``input`` n'existe pas.
    
..  shortanswer:: poo-exa-formatif-exceptions-05-B

    Déterminez la sortie produite par le programme si le fichier lu par la
    fonction ``input`` existe et contient des lignes de la forme
    
    ::
        
        nom;prenom 
    

..  shortanswer:: poo-exa-formatif-exceptions-05-C

    Déterminez la sortie produite par le programme si le fichier existe et
    contient des lignes de la forme
    
    ::
        
        nom,prenom 
    

