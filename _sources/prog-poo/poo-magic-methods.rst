.. _poo-magic-methods.rst:

Méthodes magiques
#################

..  contents:: Contenu de la page
    :depth: 3

Présentation vidéo
==================

..  youtube:: 3ohzBxoFHAY
    :divid: poo-corey-schafer-dunder-methods
    :width: 800
    :height: 430

Résumé
======

Les méthodes magiques (ou "dunder methods", car elles sont toutes préfixées et
suffixées des "double underscores" ``__``) permettent de spécifier dans les
classes certains comportements standards, tels que

- ``__init__(self)`` : Le constructeur 
- ``__del__(self)`` : Le destructeur est appelé juste avant qu'une instance soit
  détruite par le ramasse-miettes, lorsque le compteur de références atteint 0.

  ..  admonition:: Références

      - https://realpython.com/python-del-statement/#unraveling-del-vs-garbage-collection

- ``__len__(self)`` : La longueur d'une instance, afin de fonction ``len(x)`` sur une
  instance ``x`` de la classe.
- ``__str__(self)`` : La conversion en chaîne avec la fonction (``str(x)``) pour une
  instance ``x`` de la classe
- ``__repr__(self)`` : pour utiliser la fonction ``repr(x)`` sur une instance ``x`` de
  la classe et pour que l'affichage soit "joli" dans le REPL si l'on fait, pour
  une instance ``x`` de la classe:

  ::

      >>> x
      ClassName(attr1=..., attr2=..., ...)

- ``__hash__(self)`` : pour indiquer à Python comment calculer une valeur de hachage à
  partir d'une instance ``x`` de la classe, afin de pouvoir utiliser les
  instances ``x`` comme clés dans un dictionnaire (uniquement avec des instances
  qui ne changent jamais)

- ``__add__(self, other)`` : pour indiquer comment additionner deux instances de la
  classe, par exemple des fractions ou des vecteurs

..  note::

    Il existe encore plein d'autres méthodes magiques pour réimplémenter toutes
    les opérations arithmétiques, les opérateurs de comparaison, les opérateurs
    sur les bits etc ...

    Fondamentalement, tous les opérateurs de Python peuvent être redéfinis pour
    pouvoir être appliqués aux instances d'une classe.

    Références :

    - https://mathspp.com/blog/pydonts/dunder-methods#:~:text=What%20are%20dunder%20methods%3F,__%20or%20__add__%20.
    - https://www.geeksforgeeks.org/dunder-magic-methods-python/

..
    Exercices
    =========

    Les exercices pour cette partie se trouvent dans :ref:``