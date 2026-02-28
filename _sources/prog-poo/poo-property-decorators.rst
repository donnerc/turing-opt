.. _poo-property-decorators.rst:

Propriétés et décorateur ``@property``
######################################

..  contents:: Contenu de la page
    :depth: 3

Vidéo de présentation
=====================

La vidéo suivante présente le décorateur ``@property`` et son utilité pour
définir des attributs (propriétés) de manière plus flexible et puissante.

..  youtube:: jCzT9XFZ5bw
    :divid: poo-corey-schafer-properties
    :width: 800
    :height: 430

Résumé de la vidéo
==================

La vidéo montre comment modifier la classe ``Employee`` pour que l'attribut
``email`` se mette à jour automatiquement lorsque l'on modifie le nom ou le
prénom de l'employé.

Code de départ
--------------

..  activecode:: ea75e4bf-cf34-4224-b0e3-16c5b1fba31c
    :language: webtp

    class Employee:

        def __init__(self, first, last):
            self.first = first
            self.last = last
            self.email = first + '.' + last + '@gmail.com'

        def fullname(self):
            return f"{self.first} {self.last}"

    emp1 = Employee('John', 'Smith')

    # Si on modifie l'email
    emp1.first = "Guido"

    # L'email ne change pas
    print("l'email ne s'adapte pas:", emp1.email)

    # Ce qui n'est pas le cas avec la méthode fullname() où le nom
    # complet est à chaque fois recalculé automatiquement à partir
    # de .first et .last
    print("Alors que le nom complet s'adapte: ", emp1.fullname())

Le problème
-----------

Si modifie le nom ou le prénom directement avec ::

    emp1.first = "Guido"

l'attribut ``emp1.email`` ne va pas se modifier et sera incohérent par rapport à
l'attribut ``emp1.first``, contrairement à ``fullname()``, qui est une méthode,
et qui va se recalculer automatiquement à partir de ``.first`` et ``.last``:

..  activecode:: a2144a94-d9e6-454f-bafd-9632eb6f6f2a
    :language: webtp

    class Employee:
        
        def __init__(self, first, last):
            self.first = first
            self.last = last
            self.email = first + '.' + last + '@gmail.com'
            
        def fullname(self):
            return f"{self.first} {self.last}"

    emp1 = Employee('John', 'Smith')

    # Si on modifie l'email
    emp1.first = "Guido"
    
    # L'email ne change pas
    print(emp1.email)

    # Ce qui n'est pas le cas avec la méthode fullname() où le nom 
    # complet est à chaque fois recalculé automatiquement à partir 
    # de .first et .last
    print(emp1.fullname())

Le problème est que si l'on modifie la classe ``Employee`` en remplaçant
l'attribut ``.email`` par une **méthode** ``.email()`` fonctionnant comme
``fullname()``, la classe ne fonctionnera plus de la même manière et on **casse
l'interface (le contrat)** de la classe. Autrement dit, le code qui utilisait
jusqu'à présent la classe ``Employee`` devra également être modifié. 

Getters et setters
------------------

Dans la plupart des langages orientés objets, comme Java, il y a une véritable
religion qui consiste à définir, pour chaque attribut, des **accesseurs**
(méthodes à l'aide desquelles on accède (**getters**) en lecture ou en écriture
(``setters``) aux attributs), qui sont, eux, sensés ne pas être accédés
directement depuis l'extérieur de la classe, afin d'éviter le problème qu'on
rencontre.

Solution naïve (mauvaise)
=========================

La première solution serait donc de modifier la classe ``Employee`` en
transformant l'attribut ``.email`` en une méthode, comme suit:

..  activecode:: 903064fa-a3f6-4d5f-8c28-25f7f947f353
    :language: webtp

    Le code suivant produit donc une erreur, car ``email`` est à présent une
    méthode et on ne peut plus y accéder comme à une méthode avec
    ``emp1.email``.

    ~~~~

    class Employee:
        
        def __init__(self, first, last):
            self.first = first
            self.last = last

        def email(self):
            return self.first + '.' + self.last + '@gmail.com'
            
        def fullname(self):
            return f"{self.first} {self.last}"

    emp1 = Employee('John', 'Smith')

    # Si on modifie l'email
    emp1.first = "Guido"
    
    # Cela ne fonctionne plus, car email est à présent une méthode
    print(emp1.email)

Meilleure solution (avec ``@property``)
=======================================

Une meilleure solution consiste à transformer la méthode ``email`` en une
**propriété** en lui rajoutant le décorateur ``@property``.

..  activecode:: 62188ad6-fcb4-43e9-afc0-ea6c71027f31
    :language: webtp

    Le code suivant ne produit plus d'erreur, car même si ``email`` est
    implémenté comme une méthode, on peut y accéder comme à un attribut, grâce
    au décorateur ``@property``.

    ~~~~

    class Employee:
        
        def __init__(self, first, last):
            self.first = first
            self.last = last

        @property
        def email(self):
            return self.first + '.' + self.last + '@gmail.com'
            
        @property
        def fullname(self):
            return f"{self.first} {self.last}"

    emp1 = Employee('John', 'Smith')

    # Si on modifie l'email
    emp1.first = "Guido"
    
    # Cela fonctionne à nouveau et se met à jour automatiquement
    print(emp1.email)
    # On transforme aussi fullname en propriété (supprimer les parenthèses)
    print(emp1.fullname)



Implémenter un **setter**
=========================

Étant donné qu'on peut accéder au nom complet avec ``emp1.fullname``, sans les
parenthèses, comme un attribut, on pourrait être tenté de vouloir modifier le
nom complet en faisant

::

    emp1.fullname = "John Doe"

Cela ne fonctionne cependant pas, car ``fullname``, avec le décorateur
``@property`` se comporte comme un attribut **en lecture seule**. On peut
modifier cela, en créant un **setter** pour l'attribut ``fullname``, comme dans
l'exemple suivant :

..  activecode:: 173b7cbd-9b76-461f-9985-82b5c4ded345
    :language: webtp

    Le décorateur ``@fullname.setter`` permet de modifier la propriété
    ``fullname`` pour qu'elle soit modifiable:

    ~~~~

    class Employee:
        
        def __init__(self, first: str, last: str) -> None:
            self.first = first
            self.last = last

        @property
        def email(self) -> str:
            return self.first + '.' + self.last + '@gmail.com'
            
        @property
        def fullname(self) -> str:
            return f"{self.first} {self.last}"

        @fullname.setter
        def fullname(self, name: str) -> None:
            first, last = name.split(" ")
            self.first = first
            self.last = last

    emp1 = Employee('John', 'Smith')

    # On peut maintenant modifier fullname
    emp1.fullname = "John Doe"

    print(emp1.fullname)

    # l'attribut .last a été modifié automatiquement
    print(emp1.last)


Supprimer un attribut
=====================

..  
    admonition:: Attention
        
..  warning::

    Attention, l'utilisation du décorateur ``.deleter`` n'est pas forcément
    super pertinent dans notre cas, mais il est inclus ici par souci
    d'exhaustivité.

On peut également définir ce qui doit se passer lorsqu'on veut supprimer
l'attribut ``fullname`` de la classe:

::
    
    # suppression de l'attribut fullname
    del emp1.fullname

Pour ce faire, il faut utiliser un décorateur ``<attribut>.deleter`` où
``<attribut>`` représente l'attribut à supprimer.

..  activecode:: 5df05f2e-c37e-4054-961f-1170c9820631
    :language: webtp

    Le décorateur ``@fullname.deleter`` permet de modifier la propriété
    ``fullname`` pour qu'on puisse la supprimer.

    ..  note::

        Ceci n'est généralement pas recommandé. Dans le cas présent, cela ne
        fait pas grand sens et c'est juste pour la démonstration de la
        fonctionnalité.

    ~~~~

    class Employee:
        
        def __init__(self, first: str, last: str) -> None:
            self.first = first
            self.last = last

        @property
        def email(self) -> str:
            return self.first + '.' + self.last + '@gmail.com'
            
        @property
        def fullname(self) -> str:
            return f"{self.first} {self.last}"

        @fullname.setter
        def fullname(self, name: str) -> None:
            first, last = name.split(" ")
            self.first = first
            self.last = last

        @fullname.deleter
        def fullname(self) -> None:
            self.first = None
            self.last = None

    emp1 = Employee('John', 'Smith')

    print(emp1.fullname)

    # Suppression de l'attribut fullname
    del emp1.fullname

    # Les noms et prénoms sont maintenant None
    print(emp1.first, emp1.last)

    
