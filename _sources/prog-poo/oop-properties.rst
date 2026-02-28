.. _oop-properties.rst

Propriétés
##########

..  admonition:: Résumé
    
    Cette section présente la classe ``property`` et
    comment l'utiliser pour définir les propriétés d'une classe.

Introduction et motivation
==========================

Le programme suivant définit une classe ``Person`` qui a deux attributs ``name``
et ``age``, et crée une nouvelle instance de la classe ``Person`` :

..  activecode:: 3fdd1af2-79c5-4e8a-8be0-a4caa175b8cd

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age


    john = Person('John', 18)

Comme ``age`` est un attribut d'instance de la classe ``Person```, on peut
modifier l'âge d'une personne comme suit:

..  activecode:: 52b7d0a7-417b-44f1-a06e-682361ace44b
    :include: 3fdd1af2-79c5-4e8a-8be0-a4caa175b8cd

    john.age = 19

Il se trouve cependant que l'assignation suivante ne pose aucun problème à
Python, bien qu'elle n'ait aucun sens du point de vue sémantique.

..  activecode:: 413378e9-0cee-4f09-aa29-089252b9c068
    :include: 3fdd1af2-79c5-4e8a-8be0-a4caa175b8cd

    john.age = -1

Getters and setters
===================

Pour éviter ce genre de problèmes, on peut procéder de la manière suivante:

* Faire en sorte que l'attribut ``age`` soit privé
* Définir des méthodes spéciales appelées **setters** à travers lesquelles il
  faut passer pour modifier les attributs.

Dans le code suivant, comme l'attribut ``__age`` commence par ``__``, on ne peut
pas y accéder depuis l'extérieur de manière triviale:


..  activecode:: 8d0d3bda-70c1-483e-bd88-dfded818ff4f

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.__age = age

    martin = Person("Martin", 10)
    martin.__age = 15


De ce fait, pour pouvoir modifier l'attribut ``__age``, on définit un
**setter**, à savoir une méthode ``set_age`` dont le seul but est de modifier la
valeur de l'attribut ``__age``, tout en s'assurant que l'âge fourni soit
correct. On définit également un **getter**, à savoir une méthode dont le but
est de lire la valeur de l'attribut ``__age``.

..  activecode:: 0698ab78-6571-4b06-9423-357107c9e149

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.set_age(age)

        def set_age(self, age):
            if age <= 0:
                raise ValueError('The age must be positive')
            self.__age = age

        def get_age(self):
            return self.__age

