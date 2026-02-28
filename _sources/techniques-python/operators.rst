..  _operators:

Combiner des expressions avec des opérateurs
############################################

..  contents:: Contenu de la page
    :depth: 3


Nous avons vu que les expressions sont des briques syntaxiques qui permettent de
créer des valeurs à partir de rien (littéraux) ou à partir de valeurs
existentes. Dans cette section, nous allons voir comment créer des expressions
complexes à partir d'expressions plus simples. En d'autres termes, on peut
combiner des expressions simples pour construire des expressions plus complexes.

Qu'est-ce qu'un opérateur?
==========================

En programmation, un opérateur est un symbole ou une suite de symboles qui
désigne une opération effectuées sur une ou plusieurs valeurs. Un opérateur
permet donc de combiner une ou plusieurs expressions, pour former une expression
plus complexe. Les opérateurs se caractérisent par leur ``arité``, qui désigne
le nombre de valeurs sur lesquelles ils opèrent.

..  admonition:: Définition de la notion d'arité d'un opérateur

    L'arité d'un opérateur est un nombre entier déterminant le nombre
    d'expressions que l'opérateur en question est capable de combiner. En termes
    mathématiques, l'**arité d'un opérateur** est le nombre d'**opérandes** sur
    lesquels il **opère**. On distingue essentiellement les **opérateurs
    unaires** qui n'opèrent que sur un seul opérande, les opérateurs binaires
    qui opère sur deux opérandes (la majorité des opérateurs) et les opérteurs
    ternaires opérant sur trois opérandes.

..  admonition:: Exemples d'opérateurs unaires

    Dans la catégorie des opérateurs unaires, on a par exemple l'opérateur ``-``
    qui signifie l'opposé d'un nombre.

    ::

        >>> - 10
        -10

    L'opérateur logique ``not`` est aussi unaire :

    ::

        if not (x > 3):
            print("x est plus petit ou égal à 3")
        else:
            print("x est plus grand que 3")

..  admonition:: Exemples d'opérateurs binaires

    La plupart des opérateurs que vous connaissez sont binaires, notamment les
    opérateurs arithmétiques ``+``, ``-``, ``*``, ``/``, ``//``, ``%``, ``**``
    et les opérateurs booléens ``and`` et ``or``.

    Les opérateurs de comparaison ``==``, ``<``, ``>``, ``<=``, ``>=`` sont
    également binaires.

    Les opérateurs suivants, qui opèrent sur les bits individuels, sont
    également binaires ``<<``, ``>>``, ``&``, ``|``, ``^``. Nous étudierons ces
    opérateurs dans la section :ref:`bitwise-operators`.

..  admonition:: Exemples d'opérateurs ternaires

    L'expression conditionnelle est construite à partir de l'opérateur ternaire
    ``... if ... else ...``. Voici un exemple de code utilisant cet opérateur
    ternaire:

    ..  activecode:: C4E2BD91-4111-41C0-B43C-C860CC7469A4

        age = int(input("Indiquez votre âge: "))
        categorie = 'mineur' if age < 18 else 'majeur'
        print(f"Tu es {categorie}")

Expressions atomiques ou "atomes"
=================================

Les opérateurs permettent de construire des expressions plus complexes à partir
d'expressions simples. Les **expressions atomiques** ou simplement **atomes**
sont les expressions les plus élémentaires, que l'on ne peut pas décomposer
davantage. Pour l'instant, nous considérons que les atomes sont les littéraux et
les identifiants (noms de variables). En réalité, les choses sont bien plus
compliquées (voir la documentation officielle
https://docs.python.org/fr/3/reference/expressions.html#atoms). 

..  admonition:: Exemple

    Les expressions suivantes sont des atomes, en supposant l'existence d'une
    variable ``x: int = 200`` :

    ::

        >>> 10
        10
        >>> 23e-5
        0.00023
        >>> x
        200

..  admonition:: Documentation officielle

    Lien vers la documentation officielle de Python sur les expressions
    atomiques : https://docs.python.org/fr/3/reference/expressions.html#atoms.
    Il n'est pas nécessaire de maîtriser le contenu de cette page Web, car de
    nombreuses informations sont parfaitement inutiles à ce stade.

Les opérateurs permettent de combiner des expressions pour former des
expressions plus complexes.

..  admonition:: Exemple

    Dans l'expression ``- (23e-5 + x * x) - 10 * 23e-5``, on utilise l'opérateur
    unaire ``-`` et les opérateurs binaires ``+``, ``-``, ``*`` pour combiner
    les atomes suivants:

    * ``23e-5`` (littéral de type ``float``)
    * ``x`` (identifiant)
    * ``10`` (littéral de type ``int``)

Priorité des opérations
=======================

Vous savez du cours de mathématiques que tous les opérateurs n'ont pas la même
**priorité**. La plupart des opérateurs sont évalués de gauche à droite, en
suivant la priorité des opérateurs. Par exemple, les expressions suivantes sont
équivalentes

::

    3 * 10 ** 2 / 3 + 2
    ((3 * (10 ** 2)) / 3) + 2

La visualisation ci-dessous montre l'évaluation de l'expression en détails. 

..  showeval:: E1FC6BD7
    :trace_mode: true

    x = 10
    y = 2
    ~~~~
    3 * {{x}}{{10}} ** y / 3 + y
    3 * 10 ** {{y}}{{2}} / 3 + y
    3 * {{10 ** 2}}{{100}} / 3 + y
    {{3 * 100}}{{300}} / 3 + y
    {{300 / 3}}{{100.0}} + y
    100.0 + {{y}}{{2}}
    {{100.0 + 2}}{{102.0}}
    

Les règles sont les suivantes:

..  admonition:: Règles d'évaluation des expressions

    1.  On tient compte de la priorité des opérations en évaluant d'abord les
        opérandes des opérateurs les plus prioritaires. 
        
    2.  Les opérateurs de même priorité sont évalués de gauche à droite. On évalue
        donc d'abord l'opérande de gauche, puis celui de droite, sauf pour les
        exceptions suivantes

        *   Pour les opérateurs unaires ``+``, ``-`` et ``~`` où l'on évalue
            évidemment d'abord la partie de droite puisqu'il n'y a pas de partie de
            gauche.


Chaque opérateur a une certaine priorité (*precedence* en anglais). La priorité
est un nombre entier. Plus la priorité d'un opérateur est grande, plus il sera
effectué avant les autres.

Nous entrons plus en détails dans la structure des expressions et la priorité
des opérations dans la section :ref:`fondements-priorite-operations.rst`.

Conversion de types
===================

Afin de comprendre comment les expressions Python sont évaluées, il est
important de comprendre la notion de conversion de type (*type casting* en
anglais), qui est très souvent faite par Python de manière implicite. À ce
titre, lisez le deuxième article ci-dessous.

En attendant que le contenu des deux articles suivants soient intégrés dans le
cours, lisez ces deux articles.

- Conversions de types explicites : https://www.scaler.com/topics/type-casting-in-python/
- Conversions de type implicites :
  https://www.scaler.com/topics/python/implicit-type-conversion-in-python/

Exemple 1 : opérations arithmétiques mélangeant ``int`` et ``float``    
--------------------------------------------------------------------

..  admonition:: Représentation de nombres ``int`` et ``float``

    Le processeur ne peut additionner que des données compatibles. Par exemple,
    le processeur n'utilise pas les mêmes circuits électroniques pour
    additionner les nombres entiers ou les nombres à virgule, car ces derniers
    ne sont pas représentés de la même manière en binaire.

    - **Nombre entier 127** sur 32 bits : ``0000000 0000000 0000000 11111111``
    - **Nombre à virgule flottante 127.0** sur 32 bits au format IEEE 754 :
      ``01000010 11111110 00000000 00000000``

    Nous étudierons plus exactement la représentation des nombres à virgule plus
    tard dans le cours. Vous pouvez utiliser le site
    https://www.h-schmidt.net/FloatConverter/IEEE754.html pour voir la
    représentation binaire IEEE 754 d'une nombre ``float``.

Lors d'une opération arithmétique impliquant un opérande de type ``int`` et un
opérande de type ``float``, Python va d'abord convertir le nombre ``int`` en
``float`` avant de faire l'opération

..  list-table:: Conversions implicites (opérateurs arithmétiques)
    :header-rows: 1
    :widths: 1 1
    :align: left

    * - Expression
      - Conversion de type effectuée

    * - ``4.5 + 6``
      - ``4.5 + float(6)``
      
    * - ``4.5 * 6``
      - ``4.5 * float(6)``

    * - ``100 / 2``
      - ``float(100 / 2)`` : les nombres entiers sont divisés et l'opérateur
        ``/`` retourne un ``float``

    * - ``50.0 / 2``
      - ``float(50.0) / float(2)`` : conversion des opérandes en un type commun,
        retourne un ``float``

    * - ``4.7 // 1.5`` retourne ``3.0``
      - ``float(4.7) // float(1.5)``. Dans ce cas, on veut savoir combien de
        fois on peut mettre entièrement 1.5 dans 4.7. Même si la réponse est un
        nombre entier (3), l'opérateur retourne le nombre float ``3.0``, car un
        des deux opérandes est ``float``.

    * - ``4.7 % 1.5`` retourne ``0.2``
      - ``float(4.7) % float(1.5)``. L'opérateur ``%`` calcule le reste de la
        division "entière" de 4.7 par 1.5. Comme :math:`4.7 = 3.0 \cdot 1.5 +
        0.2`, l'opérateur modulo retourne ``0.2`` (plus précisément
        ``0.20000000000000018`` sur ma machine, car il n'est pas possible de
        représenter la plupart des nombres à virgule)

..  note:: 
    
    Pour la division ``/``, les opérandes sont convertis vers un type commun et le
    résultat est forcément un ``float``.


Exemple 2 : Opérations arithmétiques avec des booléens    
------------------------------------------------------

Il est possible d'effectuer des opérations arithmétiques sur les expressions
booléennes, car Python fait une conversion implicite de la valeur ``bool`` en
``int`` avant de faire les calculs.

..  note:: 

    Toute valeur bool est d'abord converti en ``int`` ou ``float`` lors de
    l'utilisation des opérateurs arithmétiques.

..  list-table:: Conversions implicites 
    :header-rows: 1
    :widths: 1 1
    :align: left

    * - Expression
      - Conversion de type effectuée

    * - ``True + True`` vaut ``2``
      - ``int(True) + int(True)``
      
    * - ``True * 5`` vaut ``5``, car ``int(True) -> 1`` et ``int(False) -> 0``
      - ``int(True) * 5*``
      
Exemple 3 : Conversion implicite en l'absence d'ambiguité uniquement
--------------------------------------------------------------------

Il y a aussi des cas où aucune conversion implicite n'est effectuée par Python,
par exemple lors d'addition d'un nombre et d'une chaîne de caractères, comme
nous l'avons déjà vu. Cela vient du fait qu'on considère le cas trop "limite" et
trop ambigu pour risquer de d'effectuer une conversion qui pourrait ne pas faire
sens.

..  list-table:: Pas de conversions implicites dans ces cas
    :header-rows: 1
    :widths: 1 1 1
    :align: left

    * - Expression
      - Erreur causée par le code
      - Conversion de type explicite

    * - ``10 + "10"``
      - ``TypeError: unsupported operand type(s) for +: 'int' and 'str'``
      - ``10 + int("10")``
      
    * - ``10 << 3.0``
      - ``TypeError: unsupported operand type(s) for <<: 'int' and 'float'``
      - ``10 << int(3.0)``

..
    Ordre d'évaluation
    ==================

    Chaque opérateur implique un ordre d'évaluation bien précis. La question est
    cruciale pour un opérateur binaire : évalue-t-on d'abord la partie de gauche ou
    la partie de droite? La plupart des opérateurs sont évalués de gauche à droite.