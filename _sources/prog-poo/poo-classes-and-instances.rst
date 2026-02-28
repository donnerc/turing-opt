.. _poo-classes-vs-instances:

Classes et instances
####################

..  contents:: Contenu de la page
    :depth: 3

Cette section a pour but de démsystifier le fonctionnement des classes et des
instances de classes (objets) en Python.

..  note::

    Les concepts présentés sont également valables dans les autres langages de
    programmation orientée objets.

Vidéo de présentation
=====================

Visionnez la vidéo suivante en essayant de suivre à partir du code de base
ci-dessous et reproduisant la classe ``Employee`` présentée à l'exercice 1. Vous
avez plusieurs options. 

#.  Commencer par regarder la vidéo et faire
    l':ref:`poo-classes-vs-instances-exo-01` ensuite pour implémenter la classe
    ``Employee``

#.  Faire l':ref:`poo-classes-vs-instances-exo-01` en même temps que vous
    visionnez la vidéo.

..  youtube:: ZDa-Z5JzLYM
    :divid: poo-corey-schafer-classes-and-instances
    :width: 800
    :height: 430

Résumé de la vidéo
==================

Exercices
=========

.. _poo-classes-vs-instances-exo-01:

Exercice 1
----------

..  activecode:: poo-classes-and-instances-exercice-1-implementation
    :language: webtp

    Implémentez la classe ``Employee`` présentée dans la vidéo en implémentant
    les aspects suivants de la classe ``Employee```:

    -   Le contructeur, afin de pouvoir initialiser un employer comme suit:

        ::

            emp = Employee("Guido", "Van Rossum", "guido@python.org", 1_000_000)

    -   Faites en sorte que le salaire soit facultatif et qu'il y ait un salaire
        par défaut de 200'000 dollars. 

    -   Définissez une méthode d'instance ``fullname() -> str`` qui retourne le
        nom complet (concaténation du prénom et du nom de famille)

    ..  admonition:: Doctests
        :class: note
    
        Voici des doctests pour tester votre classe :

        ::

            >>> e1 = Employee("Guido", "Van Rossum", "guido@python.org", 1_000_000)
            >>> e1.firstname
            'Guido'
            >>> e1.lastname
            'Van Rossum'
            >>> e1.email
            'guido@python.org'
            >>> e1.pay
            1000000
            >>> e1.fullname()
            'Guido Van Rossum'

            >>> e2 = Employee("Grace", "Hopper", "grace@compilers.net")
            >>> e2.pay
            200000


    ~~~~

    class Employee:
        pass

    emp_1 = Employee()
    emp_2 = Employee()

    print(emp_1)
    print(emp_2)

    emp_1.firstname = "Guido"
    emp_1.lastname = "Van Rossum"
    emp_1.email = "guido@python.org"
    emp_1.pay = 1_000_000

    emp_2.firstname = "Grace"
    emp_2.lastname = "Hopper"
    emp_2.email = "grace@compilers.net"
    emp_2.pay = 300_000

    print(emp_1.email)
    print(emp_2.email)

    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez le Python standard pour bénéficier des doctests (Thonny, Basthon, Futurecoder ...)")

..
    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def test_constructor_ok(self):
            try:
                e1 = Employee("AA", "BB", "bla@example.com", 10)
                feedback = "Le constructeur prend le bon nombre de paramètres"
                success = True

            except Exception as e:
                explain = str(e)
                feedback = f"Les paramètres du constructeur ne sont pas OK: {explain}"
                success = False

            self.assertTrue(success, feedback=feedback)

        def test_attributes_initialized_ok(self):
            attributes = [
                ('firstname', 'AA'), 
                ('lastname', 'BB'), 
                ('email', 'bla@example.com'), 
                ('pay', 1000000)
            ]
            e1 = Employee(*[value for attr, value in attributes])
            for attr, value in attributes:
                feedback = f"Présence de l'attribut {attr}"
                self.assertTrue(attr in e1.__dict__, feedback=feedback)
                feedback = f"L'attribut {attr} vaut bien {value}"
                self.assertEqual(e1.__dict__.get(attr), value, feedback=feedback)

        def test_pay_default_value(self):
            e1 = Employee('A', 'B', 'C@example.com')
            default = 200_000
            feedback = f"Le paramètre `pay` vaut {default} par défaut"
            self.assertEqual(e1.pay, default, feedback=feedback)

        def test_pay_fullname_method(self):
            e1 = Employee('A', 'B', 'C@example.com')
                    
            try:
                expected = "A B"
                result = e1.fullname()
                feedback = f"La méthode fullname() fonctionne correctement"
                self.assertEqual(result, expected, feedback=feedback)
            except Exception as e:
                feedback = f"La méthode fullname() n'est pas définie correctement: {str(e)}"
                self.assertTrue(False, feedback=feedback)
            
    myTests().main()


..  reveal:: 246c77eb-f27d-4612-a94e-4c723738c12f
    :showtitle: Solution

    ::

        class Employee:
            
            def __init__(self, firstname, lastname, email, pay=200_000):
                self.firstname = firstname
                self.lastname = lastname
                self.email = email
                self.pay = pay
                
            def fullname(self):
                return f"{self.firstname} {self.lastname}"