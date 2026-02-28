.. _poo-class-and-static-methods.rst:


Méthodes de classe et méthodes statiques
########################################

..  contents:: Contenu de la page
    :depth: 3

Présentation vidéo
==================

..  youtube:: rq8cL2XMM5M
    :divid: poo-corey-schafer-class-and-static-methods
    :width: 800
    :height: 430

Diagramme de classe
===================

On peut modéliser une classe par un **diagramme de classe**. Ce diagramme fait
apparaître

- les attributs (variables d'instances et de classe)
- les méthodes (d'instance, de classe et statiques)

..  admonition:: Accessibilité

    Le ``+`` devant un attribut ou une méthode indique qu'il s'agit d'un
    attribut **public**, à savoir qu'il est accessible librement de l'extérieur
    de la classe. Nous verrons dans la section sur l'encapsulation la différence
    entre un attribut public et privé.

..  figure::  https://www.plantuml.com/plantuml/svg/RP2_QiCm4CPtFuL6brBedA6aq0vTklG1nCK-1n7TdT2T26x8knUhIQs4RlRt1_tkswf1jaAnqqFW11d83H5KNyros1N3Zq7uAtoZU-wguTufHPaHJvrpZoSri32SCmH53oI5RUEcA62jpOMyJ1ulLTsum3S1oNi_2a7WZLFBYpM5hCP0wFwa2FSA4eIu_YQOczUd4kCIxn_Sqyir0Yd5sLVUN_rJ65iKHVFjEJtZyVQoVsjJ5l9gEV2-HqgNpqfMyzVPsavGVvHy667knuNy3GnhU2SIxvdMYIfHizRAS-wso6EX-0C0
    :align: center
    :width: 70%

    Diagramme de classe de la classe ``Employee``

Méthodes de classe
==================

Une **méthode de classe** est une méthode qui n'accède à aucune variable
d'instance, mais qui accède à au moins une variable de classe. On utilise le
décorateur intégré ``@classmethod`` pour spécifier qu'une méthode est **de
classe**. Dans ce cas, le premier paramètre automatiquement passé par Python
n'est pas l'instance ``self``, mais une référence à la classe, que l'on nomme
traditionnellement ``cls``.

..  admonition:: Notion de décorateur

    En Python, un décorateur est une fonction permettant de décorer une autre
    fonction. Un décorateur n'est en principe rien d'autre qu'une fonction (ou
    un objet se comportant comme une fonction = *callable*).

    Pour plus de précisions sur le fonctionnement des décorateurs, vous pouvez
    vous reporter à l'excellent tutoriel
    https://realpython.com/primer-on-python-decorators/.

..  admonition:: Syntaxe

    ..  code-block:: python

        class MyClass:

            x = 0

            def __init__(self):
                ...

            @classmethod
            def my_class_method(cls):
                cls.x = cls.x * 2
     

Méthodes statiques
==================

On définit une méthode comme statique si elle n'accède ni aux variables
d'instance, ni aux variables de classe. Elle fait partie de la classe, mais pour
des raisons purement architecturales. En effet, elle pourrait très bien
également être une simple fonction définie à l'extérieur de la classe,
puisqu'elle n'accède à aucun attribut de la classe.

..  admonition:: Particularités

    Les méthodes statiques ne prennent pas de premier paramètre implicite, au
    contraire des méthodes d'instance (paramètre ``self``) et méthodes de classe
    (paramètre implicite ``cls``)

..  admonition:: Syntaxe

    ..  code-block:: python

        class MyClass:

            x = 0

            def __init__(self):
                ...

            @staticmethod
            def my_static_method(x):
                return x ** 2

Exercices
=========

Exercice 1
----------

..  activecode:: poo-class-and-static-methods-exercice-1-implementation
    :language: webtp

    ..  note::

        Dans cet exercice, nous allons modifier la manière de créer les instances.
        On considère tous les employés comme membres d'une même organisation dont le
        nom de domaine est stocké dans une variable de classe ``org_domain``. Les
        adresses de courriel sont donc automatiquement déterminées à partir du
        prénom, du nom et du nom de domaine.

    -   Modifiez le constructeur pour qu'il soit également possible de créer un
        employé en passant le salaire sous forme de chaîne de caractères. Il
        doit néanmoins être stocké sous forme de ``float``. Dans cette version,
        il n'y a plus lieu de spécifier le courriel lors de la création des
        employés, car il doit être déterminé à partir des éléments suivants

        - prénom (``firstname``)
        - nom de famille (``lastname``)
        - nom de domaine de l'organisation (``org_domain``)

    -   Créez une variable de classe ``org_domain: str`` qui contient le nom de
        domaine de l'organisation à laquelle les employés appartiennent. Par
        défaut, cette variable doit valoir ``'example.org'``.

    -   Créez une méthode de classe ``set_org_domain(domain: str) -> None`` qui
        ajuste la variable de classe ``org_domain``.

    -   On imagine que l'on ne veut créer que des employés pour l'Etat de
        Fribourg. Modifiez le constructeur de la classe pour que l'email soit
        toujours au format ``firstname.lastname@domain``. Il n'y a donc pas
        besoin de spécifier le courriel lors de la création des instances.

        ..  note::

            Veillez mettre tout l'email en minuscules et à traiter le cas des
            noms de famille ou prénoms composés (en supprimant les espaces).

        ::

            >>> Employee.org_domain
            'example.org'
            >>> emp = Employee('Guido', 'Van Rossum', 100)
            >>> emp.email
            'guido.vanrossum@example.org'
            >>> Employee.set_org_domain('edufr.ch')
            >>> Employee.org_domain
            'edufr.ch'
            >>> emp.email
            'guido.vanrossum@example.org'
            >>> emp1 = Employee('Grace', 'Hopper', '200')
            >>> emp1.email
            'grace.hopper@edufr.ch'
            >>> emp1.pay
            200.0

    -   Définissez une **méthode de classe** ``set_raise_amount(amount: float) ->
        None`` qui modifie la variable de classe ``raise_amount`` en lui
        affectant la nouvelle valeur ``amount``.

        ::

            >>> emp = Employee('Guido', 'Van Rossum', 100_000)
            >>> emp1 = Employee('Grace', 'Hopper', 200_000)
            >>> emp.pay
            100000
            >>> emp.apply_raise()
            >>> emp.pay
            104000
            >>> Employee.set_raise_amount(1.06)
            >>> emp1.apply_raise()
            >>> emp1.pay
            212000


    -   Définissez une **méthode de classe** ``from_string(emp_str)`` qui prend
        des chaînes de caractères au format ``firstname-lastname-pay`` et qui
        retourne une nouvelle instance de la classe ``Employee`` avec les
        valeurs indiquées par la chaîne en question. Par exemple, pour ``emp_str
        = 'A-B-100'``, l'instance retournée devrait être 

        ::

            >>> e = Employee.from_string('A-B-100')
            >>> e.firstname
            'A'
            >>> e.lastname
            'B'
            >>> e.pay
            100.0

        ..  note::

            Dans la vidéo, le salaire n'est pas converti correctement en un
            float. Il faut modifier le constructeur pour que cela se fasse
            correctement.

    -   Créez une **méthode statique** ``is_workday(day: int) -> bool`` qui
        prend en paramètre un objet de type ``date`` (module ``datetime``) et
        qui retourne ``True`` si ``day`` est un jour de la semaine et ``False``
        sinon.

        ..  note:: 
            
            Consultez la documentation du module ``datetime`` ou la vidéo pour plus de
            précisions.

        ..  admonition:: Doctests

            Voici des doctests pour tester votre classe
            
            ::


                >>> Employee.org_domain
                'example.org'
                >>> a = Employee('A', 'BcD', 100)
                >>> b = Employee('F', 'G', '200')
                >>> b.pay
                200.0
                >>> a.email
                'a.bcd@example.org'
                >>> Employee.num_of_employees
                2
                >>> Employee.set_org_domain('edufr.ch')
                >>> Employee.org_domain
                'edufr.ch'
                >>> c = Employee('I', 'J', 300)
                >>> c.email
                'i.j@edufr.ch'

                >>> Employee.raise_amount
                1.04
                >>> a.apply_raise()
                >>> a.pay
                104.0

                >>> Employee.set_raise_amount(1.06)
                >>> Employee.raise_amount
                1.06
                >>> b.apply_raise()
                >>> b.pay
                212.0

                >>> e = Employee.from_string('A-B-100')
                >>> e.firstname
                'A'
                >>> e.lastname
                'B'
                >>> e.email
                'a.b@edufr.ch'
                >>> e.pay
                100.0

                >>> e2 = Employee.from_string('F-G-200')
                >>> Employee.num_of_employees
                5

                >>> import datetime
                >>> Employee.is_workday(datetime.date(2023, 11, 24))
                True
                >>> Employee.is_workday(datetime.date(2023, 11, 25))
                False
                >>> Employee.is_workday(datetime.date(2023, 11, 26))
                False
                >>> Employee.is_workday(datetime.date(2023, 11, 27))
                True

                >>> e.fullname()
                'A B'
    ~~~~

    class Employee:

        raise_amount = 1.04
        num_of_employees = 0
        
        def __init__(self, firstname, lastname, email, pay=200_000):
            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            self.pay = pay

            # incrémentation automatique du nombre d'employés
            Employee.num_of_employees += 1
            
        def fullname(self):
            return f"{self.firstname} {self.lastname}"


    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez le Python standard pour bénéficier des doctests (Thonny, Basthon, Futurecoder ...)")

..    
    ====

..
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def assert_method_defined(self, cls, method_name):
            method = cls.__dict__.get(method_name)
            is_method_defined = method and callable(method)
            feedback = f"Méthode {method_name} définie correctement"
            self.assertTrue(is_method_defined, feedback=feedback)

        def assert_function_ok(function, expected, *args):
            result = function(*args)
            self.assertEqual(result, expected)


        # mettre 00 dans le nom pour qu'elle soit exécutée en premier
        def test_00_num_of_employees(self):
            try:
                feedback = f"la variable de classe `num_of_employees` est initialisée à 0"
                self.assertEqual(Employee.num_of_employees, 0, feedback=feedback)
            except Exception as e:
                feedback = f"la variable de classe `num_of_employees` n'est pas définie correctement: {str(e)}"
                self.assertTrue(False, feedback=feedback)

            testcases = [
                ('A', 'B', 'C', 100),
                ('AA', 'BB', 'CC', 200),
                ('AAA', 'BBB', 'CCC', 300),
            ]

..  reveal:: ed7c8a2a-6d65-4380-ade5-9896779f204b
    :showtitle: Solution

    ..  literalinclude:: scripts/employee/employee3.py
        :linenos: