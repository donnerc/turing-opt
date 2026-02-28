.. _poo-inheritance.rst:

Héritage
########

..  contents:: Contenu de la page
    :depth: 3

Présentation vidéo
==================

..  youtube:: RSl87lqOXDE
    :divid: poo-corey-schafer-inheritance
    :width: 800
    :height: 430


Introduction
============

L'héritage est un mécanisme fondamental de la POO qui permet de réutiliser le
code des classes de base (classe parent) dans les classes dérivées (classes
enfant). La relation d'héritage entre deux classes est du type "IS A". 

Dans le cas de notre exemple avec les employés d'une entreprise, la classe
``Employee`` est une classe de base qui possède tous les attributs est toutes
les méthodes communs à tous les employés. Parmi les employés, il y a cependant
des développeurs, des managers, du personnel admonistratif, du personnel
technique, etc. Comme un développeur EST UN employé, ``Employee`` est la classe
de base et ``Developer`` est une classe dérivée de ``Employee``. On dit qu'elle
**hérite** (comme une sorte d'héritage génétique dans un arbre généalogique) les
attributs et les méthodes de la classe parente.

.. _employee-inheritance:

..  figure:: https://www.plantuml.com/plantuml/svg/ZP4nJyD038Nt_8eRWr0bvWYX8fM10HP6X4vkuuHJVUVexBGAfV-T9gJ9jM9WI-plwTvxNef2rDPJ9biN6eZWpOP0v54rkdMh-BpXyEQ-qDnbmy8y-OQuGpnanjmUH47TvXZ12Lhmt0OjJ4KCcgv3worN5aUf5CQ52u1ZRKlsu49XH6E_gbmK3U3HJ2E2wmcU93J_Dj0bhrSjKO_dDsRnS4QWQQYplTzn_ie1Kok2QjCuUS3zPR8_PLLaRqMZ2tMElXa_1sSzFzMMQfpOFSTj2LrUzivNe3Z0QsQwzZHND3XAsfhz7BFnI2lS8N63qVHdEXKJkRO4eHwxci0N252Fs8bBBaHEzFti-kDt3MKv7R5FMKonPWy36D7p3l_7oYVl9rBoYpHdYRd_NYpcL5VpCKIsn52sddu0
    :align: center
    :width: 70%

    Diagramme de classe montrant la relation d'héritage entre la classe de base
    ``Employee`` et les classes dérivées ``Developer`` et ``Manager``.

..
    @startuml

    skinparam classAttributeIconSize 0

    class Employee{
    +{static}raise_amount: float
    +{static}num_of_employees: int
    +{static}org_domain: str
    +firstname : str
    +lastname : str
    +email : str
    +fullname() -> str
    +apply_raise() -> None
    +{static}set_raise_amount(new_amount: float) -> None
    +{static}from_string(emp_string: str) -> Employee
    +{static}is_workday(day: Date) -> bool
    +{static}set_org_domain(new_domain: str) -> None
    }


    class Developer {
    +prog_lang : str
    }

    class Manager {
        +employees: list[Employee]
        +add_employee(emp: Employee) -> None
        +remove_employee(emp: Employee) -> None
        +show_employees() -> None
    }

    Employee <|-- Developer
    Employee <|-- Manager

    @enduml

MRO (Method Resolution Order)
=============================

Lorsqu'on appelle une méthode d'une classe fille, comme dans 

::

    >>> dev = Developer('Guido', 'Van Rossum', 100000, 'Python')
    >>> dev.fullname()

Python procède comme suit pour déterminer la méthode à appeler:

- Regarde d'abord dans la classe fille s'il y a une méthode portant ce nom. Si
  c'est le cas, c'est cette méthode qui est appelée.

- Si ce n'est pas le cas, il va ensuite dans la classe parente et cherche une
  méthode portant le nom en question. 

- Si ce n'est pas le cas, il remonte la hiérarchie de classes, jusqu'à ce qu'il
  trouve une méthode portant le nom demandé. Dans le cas de 

  ::

      >>> dev.fullname()

  Python ne trouve pas la méthode ``fullname()`` dans la classe ``Developer`` et
  va donc remonter la hiérarchie, pour finalement trouver la méthode en question
  dans la classe ``Employee``

..  note::

    On peut accéder au MRO d'une classe en utilisant la fonction
    ``help(NomClasse)``:

    ::

        >>> help(Developer)
        class Developer(Employee)
       |  Developer(firstname: str, lastname: str, pay: str | float = 200000, prog_lang: str = 'Python')
       |  
       |  Method resolution order:
       |      Developer
       |      Employee
       |      builtins.object
       |  


Exercices
=========

Exercice 1
----------

..  activecode:: poo-inheritance-exercice-1-implementation
    :language: webtp

    Rajoutez une classe ``Developer`` et une classe ``Manager`` qui dérivent de
    ``Employee`` selon le diagramme de classe de la figure
    :ref:`employee-inheritance`.

    - Dans la classe ``Developer``, le taux d'augmentation par défaut doit être de
      10% au lieu de 4% pour les employés en général.

    - Dans la classe ``Manager``, rajoutez

      - Une variable d'instance ``employees: list[Employee]`` pour stocker la
        liste des employés gérés par le manager en question.

      - Les méthodes d'instance suivantes pour gérer les employés sous la
        responsabilité d'un manager:

        - ``add_employee(new_emp: Employee) -> None`` pour ajouter un employé à
          la liste ``employees``

        - ``remove_employee(new_emp: Employee) -> None`` pour supprimer un
          employé à la liste ``employees``

        - ``show_employees() -> None`` pour afficher la liste des employés à
          l'écran avec un joli affichage, comme dans la vidéo.

    ..  note::

        Testez vous-même vos classes avec des doctests dans la docstring de chaque
        classe définie. Assurez-vous que toutes les fonctionnalités demandées soient
        bien testées.

    ~~~~

    class Employee:
        """
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

        """

        raise_amount = 1.04
        num_of_employees = 0
        org_domain = "example.org"

        def __init__(self, firstname, lastname, pay=200_000):
            self.firstname = firstname
            self.lastname = lastname
            self.email = "{fname}.{lname}@{domain}".format(
                fname=self.transform_name(firstname),
                lname=self.transform_name(lastname),
                domain=self.org_domain
            )
            self.pay = float(pay)

            # incrémentation automatique du nombre d'employés
            Employee.num_of_employees += 1

        def apply_raise(self):
            self.pay *= Employee.raise_amount

        @staticmethod
        def transform_name(name: str) -> str:
            return name.lower().replace(" ", "")

        @classmethod
        def from_string(cls, emp_string, sep="-"):
            try:
                firstname, lastname, pay = emp_string.split(sep)
                return cls(firstname, lastname, pay)
            except Exception as e:
                raise ValueError(
                    f"Invalid format: ({emp_string})"
                )

        @staticmethod
        def is_workday(day):
            return day.weekday() not in [5, 6]

        @classmethod
        def set_org_domain(cls, new_domain):
            cls.org_domain = new_domain

        @classmethod
        def set_raise_amount(cls, new_amount):
            cls.raise_amount = new_amount

        def fullname(self):
            return f"{self.firstname} {self.lastname}"


    if __name__ == '__main__':
        import doctest
        doctest.testmod()


Exercice 2
----------

Complétez / corrigez le code de l'exercice 1 pour que tous les doctests
ci-dessous passent sans accroc.

..  reveal:: b9826386-5cf5-48ab-b35b-3d14a815c7b6
    :showtitle: Doctests à faire passer

    ..  activecode:: ca46bf82-cb90-49cc-9f52-22c7fffa5f78


        '''
        >>> ################# Doctests for inheritance ######################

        >>> issubclass(Developer, Employee)
        True
        >>> issubclass(Manager, Employee)
        True
        >>> Developer.raise_amount
        1.1
        >>> d1 = Developer('A', 'B', 1, 'Python')
        >>> d2 = Developer('AA', 'BB', 2, 'Python')
        >>> d3 = Developer('AAA', 'BBB', 3, 'Javascript')
        >>> m1 = Manager('Elon', 'Musk', 1, [d1, d2])
        >>> [e1, e2] = m1.employees
        >>> e1
        Developer(firstname='A', lastname='B', pay=1.0, prog_lang='Python')
        >>> e2
        Developer(firstname='AA', lastname='BB', pay=2.0, prog_lang='Python')
        >>> m2 = Manager('Jeff', 'Besos', 10000000000)
        >>> m2
        Manager(firstname='Jeff', lastname='Besos', pay=10000000000.0, employees=[])
        >>> m2.employees
        []
        >>> m2.add_employee(d3)
        >>> m2.add_employee(d3)
        >>> m2.employees
        [Developer(firstname='AAA', lastname='BBB', pay=3.0, prog_lang='Javascript')]
        >>> m2.remove_employee(d3)
        >>> m2.employees
        []
        >>> m2.remove_employee(d3)
        >>> m1.show_employees()
        --> A B
        --> AA BB

        >>> ################# Reset everything for legacy tests ######

        # reset num of employees
        >>> Employee.num_of_employees = 0

        >>> ################# Old functionality ######################

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

        '''

