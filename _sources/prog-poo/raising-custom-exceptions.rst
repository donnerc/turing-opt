.. _raising-custom-exceptions.rst:

Définir et lever ses propres exceptions
#######################################

..  contents:: Contenu de la page
    :depth: 3

Pour l'instant, nous avons vu comment gérer des exceptions levées par Python
pour signaler que quelque chose ne va pas.

Il est aussi possible de lever soi-même une exception lorsque l'on détecte une
anomalie.

Les exceptions définies par Python fonctionnent bien pour gérer les problèmes
habituels qui se posent dans la plupart des programmes. Cependant, lorsqu'on
développe un programme spécifique, il arrive souvent que les exceptions
intégrées à Python soient trop génériques pour traiter les problèmes spécifiques
qui peuvent survenir dans notre programme spécialisé dans une tâche
particulière.

Python permet de ce fait de définir ses propres exceptions. Il suffit pour cela
de définir une nouvelle classe qui dérive directement ou indirectement de la
classe `Exception`.

Exemple 1 (motivation)
======================

Dans un programme de dessin, on veut définir une classe ``Rectangle`` pour
modéliser un rectangle.

..  activecode:: raise-exceptions-rectangle.py

    class Rectangle:

        def __init__(width: float, height: float) -> None:
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def __repr__(self):
            width = self.width
            height = self.height
            return f"Rectangle(width={width}, height={height})"

        def __str__(self):
            return repr(self)

    r1 = Rectangle(width=10, height=20)
    r2 = Rectangle(width=10, height=-20)

    for r in [r1, r2]:
        print(f"Le rectangle {r} a une aire de {r.area()}")

Comme le montrent les exemples en fin de programme, la classe ``Rectangle``
fonctionne correctement tant que l'utilisateur introduit des valeurs
raisonnables lors de l'instanciation de la classe, mais produit des résultats
qui n'ont aucun sens si l'utilisateur introduit des valeurs négatives pour la
largeur ou la hauteur du rectangle.

Lever une exception
===================

On pourrait évidemment afficher un message à l'utilisateur avec ``print`` pour
indiquer que les paramètres ne sont pas corrects, mais cela n'est pas
recommandé. La bonne pratique consiste à lever une exception pour interrompre le
flux normal de l'exécution du programme et permettre une bonne gestion du
problème.

Voici une meilleure version de la classe ``Rectangle`` qui signale le problème
lors de l'instanciation de la classe en levant une exception ``ValueError`` avec
un message approprié.

..  admonition:: Lever une exception

    Pour lever une exception, on utilise le mot-clé ``raise`` suivi d'une
    exception dérivant de la classe ``Exception``. De manière optionnelle, on
    peut fournir un message d'erreur compréhensible par l'utilisateur et donnant
    plus de précisions.

    ::

        raise Exception("Error message")

..  activecode:: raise-exceptions-rectangle-raises-value-error.py

    class Rectangle:
        def __init__(self, width: float, height: float) -> None:
            if width < 0 or height < 0:
                raise ValueError(
                    f"The width and height should be non negative (width={width}, height={height})"
                )
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def __repr__(self):
            width = self.width
            height = self.height
            return f"Rectangle(width={width}, height={height})"

        def __str__(self):
            return repr(self)


    r1 = Rectangle(width=10, height=20)
    r2 = Rectangle(width=10, height=-20)

    for r in [r1, r2]:
        print(f"Le rectangle {r} a une aire de {r.area()}")

Définir un nouveau type d'exception
===================================

Au lieu de lever une exception ``ValueError`` utilisée de manière générique pour
indiquer qu'un paramètre possède une valeur qui n'a pas de sens, on peut définir
une exception spécialisée, par exemple ``NegativeDistanceError``. Il suffit pour
cela d'étendre la hiérarchie de classe des exceptions en créant une classe qui
dérive de ``Exception`` ou d'une de ses sous-classes.

..  admonition:: Remarque

    La classe ``GeometryError`` dérive de la classe ``Exception``, ce qui permet
    de lever des exceptions de type ``GeometryError`` avec ``raise
    GeometryError``. La classe est vide et ne contient aucune définition. La
    seule chose qui compte est qu'elle dérive de ``Exception`` ou d'une autre
    exception plus spécialisée.

    La classe ``NegativeDistanceError`` dérive de la classe ``GeometryError`` et
    est évalement vide.

..  activecode:: custom_exception_negative_distance_error.py

    class GeometryError(Exception):
        pass


    class NegativeDistanceError(GeometryError):
        pass


    class Rectangle:
        def __init__(self, width: float, height: float) -> None:
            if width < 0 or height < 0:
                raise NegativeDistanceError(
                    f"The width and height should be non negative (width={width}, height={height})"
                )
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def __repr__(self):
            width = self.width
            height = self.height
            return f"Rectangle(width={width}, height={height})"

        def __str__(self):
            return repr(self)


    r1 = Rectangle(width=10, height=20)
    r2 = Rectangle(width=10, height=-20)

    for r in [r1, r2]:
        print(f"Le rectangle {r} a une aire de {r.area()}")

Exemple 2
=========

Pour illustrer cela, on peut créer un programme qui demande à l'utilisateur de
créer un rectangle et qui affiche sont aire.

..  warning::

    Le programme ne s'exécute pas tout-à-fait comme il faut dans l'environnement
    de ce site. Pour bien comprendre l'exécution, exécutez le programme dans
    Thonny ou dans l'environnement https://futurecoder.io/course/#ide.

..  raw:: html 

    <div class="hidden">

..  
    activecode:: b692b529
    :hiddencode:

    # prefix code to make the I/O work in real time and avoid buffering
    from time import sleep

    old_input = input
    def input(msg):
        sleep(0.1)
        user_input = old_input(msg)
        sleep(0.1)
        return user_input

..  raw:: html 

    </div>

..  activecode:: custom_exceptions_user_input.py

    class GeometryError(Exception):
        pass


    class NegativeDistanceError(GeometryError):
        pass


    class Rectangle:
        def __init__(self, width: float, height: float) -> None:
            width = float(width)
            height = float(height)

            if width < 0 or height < 0:
                raise NegativeDistanceError(
                    f"The width and height should be non negative (width={width}, height={height})"
                )
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def __repr__(self):
            width = self.width
            height = self.height
            return f"Rectangle(width={width}, height={height})"

        def __str__(self):
            return repr(self)


    print("This program computes the area of a rectangle")
    while True:
        try:
            width = input("Rectangle width: ")
            if width.lower().strip() == "exit":
                break
            height = input("Rectangle height: ")

            rect = Rectangle(width, height)
        except ValueError as e:
            print(f"Invalid dimensions: {e}")
        except NegativeDistanceError as e:
            print(f"Invalid dimensions: {e}")
        else:
            area = rect.area()
            print(f"The area of the rectangle {rect} is {area}")


Pour aller plus loin et références
==================================

* https://www.programiz.com/python-programming/user-defined-exception#:~:text=In%20Python%2C%20users%20can%20define%20custom%20exceptions%20by,built-in%20exceptions%20are%20also%20derived%20from%20this%20class.