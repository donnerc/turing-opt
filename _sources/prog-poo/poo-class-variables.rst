.. _poo-class-variables.rst:

Variables de classe
###################

..  contents:: Contenu de la page
    :depth: 3

Présentation vidéo
==================

..  youtube:: BJ-VvGyQxho
    :divid: poo-corey-schafer-class-variables
    :width: 800
    :height: 430

Définition
==========

Il est possible de définir des variables qui n'appartiennent pas en propre à
chaque instance d'une classe, mais qui sont partagées par toutes les instances.
On parle dans ce cas de **variable de classe**. On définit une variable de
classe directement dans la classe, en dehors de toute méthode, en particulier
avant le constructeur. On accède en lecture ou en écriture à une variable de
classe en mettant ``NomClasse.nom_variable_de_classe``.

..  code-block:: python
    :linenos:

    class Employee:

        # variable de classe num_of_employees
        x = 0

    >>> e = Employee()
    # on peut accéder à une variable de classe par le biais d'une instance
    >>> e.x
    0
    # mais on n'a pas besoin d'avoir une instance ... on peut aussi passer
    # par la classe elle-même.
    >>> Employee.x
    0

    # Une variable de classe n'est pas stockée dans les instances    
    >>> x in e.__dict__
    False
    # ... mais uniquement dans la classe
    >>> x in Employee.__dict__
    True


Exercices
=========

Exercice 1
----------

..  activecode:: poo-class-variables-exercice-1-implementation
    :language: webtp

    -   Modifiez la classe ``Employee`` de la page précédente en rajoutant une
        **variable de classe** ``raise_amount: float`` qui représente le
        pourcentage d'augmentation de chaque employé lorsqu'on appelle la
        méthode ``apply_raise() -> None``. Au début, ce taux d'augmentation vaut
        1.04 (correspond à une augmentation de 4%).

    -   Définissez la méthode d'instance ``apply_raise() -> None`` qui applique
        une augmentation de salaire indiquée par la variable de classe
        ``raise_amout``.

    -   Définissez une **variable de classe** ``num_of_employees: int`` qui est
        automatiquement augmentée de 1 à chaque fois qu'un employé est créé
        (instancié).



    ..  admonition:: Doctests

        Voici des doctests pour tester votre classe si vous travaillez dans
        futurecoder par exemple:

        ::

            >>> Employee.num_of_employees
            0
            >>> a = Employee('A', 'B', 'C', 200)
            >>> Employee.num_of_employees
            1
            >>> b = Employee('AAA', 'BBB', 'CCC', 200)
            >>> Employee.num_of_employees
            2
            >>> Employee.raise_amount
            1.04
            >>> a.pay
            200.0
            >>> a.apply_raise()
            >>> a.pay
            208.0

    ~~~~

    class Employee:
        
        def __init__(self, firstname, lastname, email, pay=200_000):
            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            self.pay = pay
            
        def fullname(self):
            return f"{self.firstname} {self.lastname}"

    try:
        import doctest
        doctest.testmod()
    except:
        print("Utilisez le Python standard pour bénéficier des doctests (Thonny, Basthon, Futurecoder ...)")

..
    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

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

            for i, test in enumerate(testcases):
                a = Employee(*test)
                feedback = f"La variable de classe `num_of_employees` est incrémentée lors de chaque instanciation"
                self.assertEqual(Employee.num_of_employees, i + 1, feedback=feedback)

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

        def test_class_variable_defined(self):
            try:
                feedback = f"Variable de classe 'raise_amout' initialisée correctement"
                self.assertEqual(Employee.raise_amount, 1.04, feedback=feedback)

            except Exception as e:
                explain = str(e)
                feedback = f"Variable de classe pas définie: {explain}"
                success = False
                self.assertTrue(success, feedback=feedback)


        def test_apply_raise(self):
            testcases = [
                (100, 104), 
                (200, 208),
            ]

            try:
                method = Employee.apply_raise
                success = True
                reason = ''
            except Exception as e:
                success = False
                reason = str(e)

            feedback = f"La méthode d'instance 'apply_raise' est bien définie: {reason}"
            self.assertTrue(success, feedback=feedback)

            for pay, new_pay in testcases:
                e = Employee('A', 'B', 'C', pay)
                e.apply_raise()
                feedback = f"Le salaire est augmenté correctement par `raise_amount`"
                self.assertEqual(e.pay, new_pay, feedback=feedback)

                

    myTests().main()

..  reveal:: f3dbea68-3039-4ef7-b7f0-96b6995e4d40
    :showtitle: Solution

    ..  code-block:: python

        class Employee:
            
            raise_amount = 1.04
            num_of_employees = 0

            def __init__(self, firstname, lastname, email, pay=200_000):
                self.firstname = firstname
                self.lastname = lastname
                self.email = email
                self.pay = pay

                Employee.num_of_employees += 1

            def fullname(self):
                return f"{self.firstname} {self.lastname}"
            
            def apply_raise(self):
                self.pay *= Employee.raise_amount