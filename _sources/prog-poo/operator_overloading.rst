Surcharge d'opérateurs
######################

..  contents:: Contenu de la page
    :depth: 3


Concept de surcharge d'un opérateur (*Operator overloading*)
============================================================

La **surcharge d'opérateurs** permet de donner différents sens aux opérateurs
utilisés dans les expressions en fonction du type des opérandes sur lesquels ils
opèrent. 

..  admonition:: Exemple : surcharge de l'opérateur ``+``

    L'opérateur ``+`` a un sens différents et effectue des opérations différents
    selon que les opérandes sont ...

    * ... des nombres entiers (``int``), comme dans l'expression ``3 + 4``, auquel
      cas l'opérateur ``+`` effectue une addition des nombres entiers et
      retourne un nombre entier.
      
    * ... des chaînes de caractères (``str``), comme dans l'expression ``"parle"
      + "ment"`` auquel cas l'opérateur effectue une opération de concaténation
      et retourne la valeur ``"parlement"``). 

    * ... des vecteurs dans :math:`\mathbb{R}^2`. Dans ce cas, l'opérateur ``+``
      effectue une addition vectorielle composante à composante.

    On peut encore imaginer des tas d'autres manières de surcharger l'opérateur
    d'addition. Dans tous les cas, l'opérateur est le même mais l'opération
    effectuée est différente. En anglais, on parle alors de **overloading.** 
    
Exemple 1 (addition vectorielle)
================================
    
En Python, la surcharge d'un opérateur se fait de la même manière que la
définition d'une méthode, sauf que le nom de la méthode à définir est imposé par
Python. Ainsi, pour surcharger l'opérateur ``+`` de telle sorte qu'il puisse
également additionner deux objets de type ``Vector2D``, il suffit de définir une
méthode ``__add__`` dans la classe ``Vector2D`` :

..  activecode:: 9d96b9c3-2497-45b8-a1d0-7ec12dc11270

    class Vector2D:
        "Implémentation d'un vecteur de R^2"

        def __init__(self, x: int, y: int) -> None:
            self.x: int = x
            self.y: int = y

        def __repr__(self) -> str:
            return f"Vector2D({self.x}, {self.y})"

        def __add__(self, other: 'Vector2D') -> 'Vector2D':
            x_res = self.x + other.x
            y_res = self.y + other.y
            res = Vector2D(x_res, y_res)
            return res

    A = Vector2D(4, 7)
    B = Vector2D(-2, 5)
    C = A + B
    print("Vecteur somme:", C)

..  admonition:: Remarque

    L'addition ``A + B`` de la ligne 19 est automatiquement convertie par Python
    sous la forme d'un appel à la méthode ``__add__``, c'est-à-dire sous la
    forme ``A.__add__(B)``. 

    ..  list-table:: Appel de la méthode ``__add__``
        :header-rows: 1
        :align: left
        :widths: 10, 50
    
        * - Expression en notation **infix**
          - Traduction sous forme d'appel de la méthode spéciale ``__add__``
    
        * - ``A + B``
          - ``A.__add__(B)``
    
    
La surcharge d'opérateurs facilite la lisibilité du code, tout en étendant les
fonctionnalité de certains opérateurs. La plupart des opérateurs Python peuvent
être surchargés de cette manière en donnant une implémentation pour la méthode
correspondante. Parmi les plus importants, nous retiendrons surtout les
opérateurs suivants :

..  list-table:: Surcharge des opérateurs arithmétiques
    :header-rows: 1
    :align: left
    :widths: 20, 10, 30, 80

    *   - Opération
        - Arité
        - Méthode appelée
        - Signification et résultat habituel sur les nombres

    *   - ``a + b``
        - 2
        - ``a.__add__(b)``
        - Somme :math:`a + b`

    *   - ``a - b``
        - 2
        - ``a.__sub__(b)``
        - Différence :math:`a - b`

    *   - ``-a``
        - 1
        - ``a.__neg__()``
        - Opposé :math:`-a`

    *   - ``a * b``
        - 2
        - ``a.__mul__(b)``
        - Produit :math:`a \cdot b`

    *   - ``a ** b``
        - 2
        - ``a.__pow__(b)``
        - Puissance :math:`a ^ b`

    *   - ``a / b``
        - 2
        - ``a.__truediv__(b)``
        - Division standard :math:`\frac{a}{b}`

    *   - ``a // b``
        - 2
        - ``a.__floordiv__(b)``
        - Division entière :math:`\left\lfloor \frac{a}{b} \right\rfloor` de :math:`a` par
          :math:`b`

    *   - ``a % b``
        - 2
        - ``a.__mod__(b)``
        - Reste de la division entière de :math:`a` par :math:`b`

..  list-table:: Surcharge des opérateurs de comparaison
    :header-rows: 1
    :align: left
    :widths: 20, 10, 30, 80

    *   - Opération
        - Arité
        - Méthode appelée
        - Signification et résultat habituel sur les nombres

    *   - ``a < b``
        - 2
        - ``a.__lt__(b)``
        - Inférieur à (:math:`a < b`)

    *   - ``a <= b``
        - 2
        - ``a.__le__(b)``
        - Inférieur ou égal à (:math:`a \leq b`)

    *   - ``a > b``
        - 2
        - ``a.__gt__(b)``
        - Supérieur à (:math:`a > b`)

    *   - ``a >= b``
        - 2
        - ``a.__ge__(b)``
        - Supérieur ou égale à (:math:`a \geq b`)

    *   - ``a == b``
        - 2
        - ``a.__eq__(b)``
        - Égalité (:math:`a = b`)

    *   - ``a != b``
        - 2
        - ``a.__ne__(b)``
        - Différent de (:math:`a \neq b`)

..  list-table:: Surcharge des opérateurs bit à bit
    :header-rows: 1
    :align: left
    :widths: 20, 10, 30, 80

    *   - Opération
        - Arité
        - Méthode appelée
        - Signification et résultat habituel sur les nombres

    *   - ``a | b``
        - 2
        - ``a.__or__(b)``
        - Combine les nombres ``a`` et ``b`` bit à bit en effectuant sur chaque
          paire de bits un OU logique

          ::

              1100 (a)
              0101 (b)
              ----
              1101 (a | b)

    *   - ``a & b``
        - 2
        - ``a.__and__(b)``
        - Combine les nombres ``a`` et ``b`` bit à bit en effectuant sur chaque
          paire de bits un ET logique

          ::

              1100 (a)
              0101 (b)
              ----
              0100 (a & b)
    
    *   - ``a ^ b``
        - 2
        - ``a.__xor__()``
        - Combine les nombres ``a`` et ``b`` bit à bit en effectuant sur chaque
          paire de bits un OU EXCLUSIF (XOR)

          ::

              1100 (a)
              0101 (b)
              ----
              1001 (a ^ b)

    *   - ``~b``
        - 1
        - ``a.__invert__()``
        - Inverse tous les bits du nombre ``a``

          ::

              01 (a)
              ----
              10 (~a)


    
Références
==========

Vous trouverez plus de détails sur la surcharge d'opérateurs dans les sources / références suivantes

*   https://www.geeksforgeeks.org/operator-overloading-in-python/
*   https://www.python-course.eu/python3_magic_methods.php
*   Tutoriel très complet sur la surcharge d'opérateurs :
    https://www.geeksforgeeks.org/operator-overloading-in-python/

Exercices
=========
          
Exercice 1 (opérations sur les vecteurs)
----------------------------------------


..  activecode:: 04c483d2-0f46-4a5a-8eb2-9bf9115210a5

    Complétez la classe ``Vector`` ci-dessous en surchargeant les opérateurs
    mentionnés dans le tableau ci-dessous pour opérer sur des vecteurs de
    :math:`\mathbb{R}^3`, instances de la classe ``Vector``.

    Les exemples du tableau ci-dessous supposent l'existence des vecteurs

    ::

        v1 = Vector(1, 1, 1)
        v2 = Vector(2, 2, 2)
        v3 = Vector(0, -2, 4)

    ..  list-table:: Opérateurs à surcharger sur les vecteurs dans :math:`\mathbb{R}^3`
        :header-rows: 1
        :align: left
        :widths: 10, 5, 50

        *   - Opérateur
            - Arité
            - Opération

        *   - ``+``
            - 2
            - Addition vectorielle ``v1 + v2`` (:math:`\vec{v_1} + \vec{v_1}`)
                
        *   - ``-``
            - 1
            - Vecteur opposé ``- v1`` (:math:`- \vec{v_1}`)

        *   - ``-``
            - 2
            - Différence vectorielle ``v2 - v1`` (:math:`\vec{v_2} - \vec{v_1}`)
            
        *   - ``*``
            - 2
            - Produit scalaire ``v1 * v2`` (:math:`\vec{v_1} \cdot \vec{v_2}`)

        *   - ``//``
            - 2
            - Déterminer si les vecteurs sont colinéaires (parallèles) ``v1 // v2``

              ..  admonition:: Rappel
  
                  On peut utiliser le produit scalaire et la norme des vecteurs pour
                  savoir s'ils sont parallèles. Deux vecteurs :math:`\vec{v_1}` et
                  :math:`\vec{v_2}` sont parallèles si et seulement si leur produit
                  scalaire :math:`\vec{v_1} \cdot \vec{v_2}` est égal au produit de
                  leur norme.

        *   - ``<, <=, >, >=``
            - 2
            - Comparaison des normes des vecteurs. Par exemple, ``v1 < v2`` doit
              retourner ``True`` si et seulement si 
            
              ..  math:: 
                  
                  \lVert \vec{v_1} \rVert < \lVert \vec{v_2} \rVert
  
              ..  admonition:: Rappel
  
                  Pour calculer la norme d'un vecteur dans un système orthonormé, on
                  peut utiliser le théorème de Pythagore.

        *   - ???
            - 1
            - Calcul de la norme du vecteur. Choisissez un opérateur encore libre
              qui conviendrait pour effectuer le calcul de la norme d'un vecteur.

              ..  admonition:: Conseils
  
                  - L'opérateur en question doit être d'arité 1
                  - L'opérateur en question doit avoir une précédence supérieure à
                      tous les autres opérateurs
  

    ..  admonition:: Remarque (instruction ``assert``)

        L'instruction ``assert expression_booléenne`` utilisée dans le fonction
        ``test`` lève une exception (crée une erreur) si l'expression booléenne
        ``expression_booléenne`` est ``False`` et ne fait rien sinon. Le but de
        l'exercice est donc de faire en sorte que l'appel ``test()`` ne crée
        aucun problème.

    ~~~~
    
    class Vector:

        def __init__(self, x: int, y: int, z: int) -> None:
            self.x: int = x
            self.y: int = y
            self.z: int = z

        def __repr__(self) -> str:
            return f'Vector({self.x}, {self.y}, {self.z})'

    def test():
        v1 = Vector(1, 1, 1)
        v2 = Vector(2, 2, 2)
        v3 = Vector(0, -2, 4)

        # Addition vectorielle
        v = v1 + v2
        # Tester l'égalité de deux vecteurs
        assert v == Vector(3, 3, 3)
        # Différence entre deux vecteurs
        v = v - v2
        assert v == v1
        # Opposé du vecteur v1
        assert -v1 == Vector(-1, -1, -1)
        # Produit scalaire
        assert v1 * v2 == 6
        # Tester si deux vecteurs sont parallèles
        assert v1 // v2 == True
        assert v1 // v3 == False
        # Calculer la norme d'un vecteur
        assert ~v1 - v1 * v1 < epsilon
        assert ~(v1 + v2) - 27 ** .5 < epsilon
        # Comparaison de vecteurs
        assert v1 < v2
        assert v1 <= v1
        assert v1 <= v2
        assert v1 != v2
        assert v2 > v1
        assert v2 >= v1 

    test()


..  reveal:: 7e9b9d01-7aad-4c67-a23c-19e0a43d71e4
    :showtitle: Corrigé

    ..  admonition:: Corrigé
        
        Voici le code corrigé, y compris une fonction de test qui permet de tester que
        le code est fonctionnel. Voici quelques remarques concernant le code:

        -   l'utilisation de la fonction intégrée ``all(conditions)`` qui prend en
            paramètre une liste de booléens (ou expressions booléennes) et qui retourne
            ``True`` si et seulement si tous les éléments de la liste sont ``True``.

        -   Les annotations de type pour le paramètre ``other`` qui doit être une
            instance de la classe ``Vector`` sont indiquées sous forme de chaîne de
            caractères et non comme ``Vector``.

        -   On a utilisé l'opérateur ``~`` pour représenter la norme d'un
            vecteur. Il s'agit d'un opérateur unaire a fort précédence, ce qui
            convient bien pour représenter la norme.

        ..  literalinclude:: code/vector_corrige.py
            :language: python


..
    Exercice 2 (Opérations sur les fractions)
    -----------------------------------------

    ..  activecode:: 112d37e5-5a49-48b0-b954-aaa50e5962f8

        Implémenter une classe ``Fraction`` qui doit pouvoir s’utiliser de la
        manière suivante :

        ~~~~

        class Fraction:
            
            '''
            Classe Fraction : représente une fraction 
            '''

            def __init__(self, num, denom):
                self.num = num
                self.denom = denom
                

            def __str__(self):
                pass

            def __repr__(self):
                pass

        
                                            
        def gcd(m,n):
            while m%n != 0:
                oldm = m
                oldn = n

                m = oldn
                n = oldm%oldn
            return n

        def test():
            assert Fraction(4, -6) == Fraction(-2, 3)
            assert Fraction('-5/6') == Fraction(-5, 6)
            assert Fraction('4') == Fraction(4, 1)
            assert Fraction('4.2') == Fraction(21, 5)
            f1, f2 = Fraction(6, 3), Fraction(2, 5)
            assert repr(f1) == 'Fraction(6, 3)'
            
            assert (f1 + f2) == Fraction(12, 5)
            assert (f1 - f2) == Fraction(8, 5)
            assert (f1 * f2) == Fraction(4, 5)
            assert (f1 / f2) == Fraction(5, 1)
            assert (f2 < f1) == True
            assert (f2 > f1) == False
            assert Fraction(1, 2) <= Fraction(2, 4)
            assert Fraction(1, 2) >= Fraction(2, 4)
            assert f1 == f2 == False
            assert (f1 <= f2) == False
            assert (f1 >= f2) == True

        test()

    Code de base
    ++++++++++++

    ..  literalinclude:: code/my_fraction_base.py
        :language: python
        :linenos:

    ..  
        ..  admonition:: Téléchargement
            :class: attention

            :download:`code/my_fraction_base.py`


        ..  admonition:: Remarque
            :class: note

            Remarquez les lignes

            ::

                if __name__ == '__main__':
                    import doctest
                    doctest.testmod()

            à la fin du fichier. Ces lignes ne sont exécutées que lorsque l'on
            exécute directement le script python mais pas lorsqu'il est importé en
            tant que module dans un autre programme Python. Le module ``doctest``
            utilise les exemples présents dans la docstring pour effectuer des tests
            sur la classe.

            Ainsi, tant que toutes les méthodes ne sont pas implémentées
            correctement, l'exécution du script va causer des erreurs.


    Indications
    +++++++++++

    *   Compléter le code de la classe ``Fraction`` présenté plus haut
        (:download:`code/my_fraction_base.py`) et qui dispose déjà d’une fonction
        ``pgcd`` qui calcule le PGCD de deux nombres entiers à l’aide de
        l’algorithme d’Euclide

    *   Le module intégré ``fractions`` contient une classe ``Fraction`` qui
        présente ces caractéristiques. Il est donc possible d’importer la classe
        ``Fraction`` avec ``from fractions import Fraction``.
    *   Une fraction négative est représentée par un numérateur négatif et un
        dénominateur positif.
    *   Veiller à définir une méthode ``reduce()`` qui divise le numérateur et le
        dénominateur par leur PGCD.
    *   Surcharger les fonctions spéciales ``__add__``, ``__mul__``, ``__div__`` etc
        … pour implémenter les opérations mathématiques sur les fractions
    *   Surcharger les opérations de comparaison pour pouvoir comparer des fractions
        (cf. la documentation pour savoir comment s’appellent ces méthodes
        spéciales, comme par exemple ``__le__`` pour ``<``.
    *   Tester le type de la valeur donnée au constructeur et lever des erreurs de
        manière appropriée, par exemple si le dénominateur vaut 0, si la chaine de
        caractère ne représente pas un nombre, etc …


    ..  reveal:: f5b53ee5-f2fe-496d-8c1f-fe354acf90f3
        :showtitle: Solution
        :instructoronly:

        ..  admonition::: Solution

            Voici un corrigé possible pour la classe ``Fraction``.

            ..  warning:: 

                Étudier particulièrement le constructeur ``__init__`` qui utilise
                quelques fonctionnalités intéressantes telles que la fonction
                ``isinstance(instance, classinfo)`` qui permet de tester si l'objet
                ``instance`` est une instance de la classe ``classinfo``

                Exemples d'utilisation :

                ::

                    >>> isinstance('salut', str)
                    True
                    >>> isinstance('salut', int)
                    False

            ..  literalinclude:: code/my_fraction_corrige.py
                :language: python
                :linenos: